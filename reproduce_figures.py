#!/usr/bin/env python3
"""Regenerate figures using only the sanitized evidence released in this folder.
Requires Python 3, NumPy and Matplotlib. Does not run or disclose model methods.
"""
import csv,json,os,tempfile
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR',os.path.join(tempfile.gettempdir(),'ev-evidence-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'figures';OUT.mkdir(exist_ok=True)
BLUE='#174d72';ORANGE='#a34b22';GRAY='#67727b';INK='#182027'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':15,'axes.labelsize':11,'axes.spines.top':False,'axes.spines.right':False,'axes.edgecolor':'#b2b8bc','axes.labelcolor':INK,'text.color':INK,'xtick.color':INK,'ytick.color':INK,'figure.facecolor':'white','savefig.facecolor':'white','svg.hashsalt':'evidence-20261103'})
def rows(name):
 with (ROOT/'data'/name).open()as f:return list(csv.DictReader(f))
def finish(fig,name,note):
 fig.text(.08,.035,note,fontsize=9,color=GRAY,va='bottom')
 fig.subplots_adjust(left=.10,right=.96,top=.86,bottom=.22)
 fig.savefig(OUT/(name+'.png'),dpi=180,metadata={'Software':'Matplotlib; sanitized measurement data'})
 fig.savefig(OUT/(name+'.svg'),metadata={'Date':None,'Creator':'Matplotlib; sanitized measurement data'})
 plt.close(fig)
q=rows('quality_series.csv');baseline=float(q[0]['perplexity']);values=[float(r['perplexity'])for r in q[1:]]
fig,ax=plt.subplots(figsize=(9,5.6));x=np.arange(1,len(values)+1)
ax.plot(x,values,'o-',lw=2,color=BLUE,ms=5,label='Research evaluation series')
ax.axhline(baseline,color=GRAY,ls='--',lw=1.3,label=f'Reference: {baseline:.4f}')
ax.annotate(f'{values[-1]:.4f}',(x[-1],values[-1]),xytext=(-12,17),textcoords='offset points',ha='right',weight='bold',color=BLUE)
ax.set(xticks=x,xticklabels=[r['record']for r in q[1:]],ylabel='Recorded perplexity · lower is better',xlabel='Anonymized checkpoint order · spacing is not training time',ylim=(9.4,11.05))
ax.grid(axis='y',alpha=.2);ax.legend(frameon=False,loc='upper right');fig.suptitle('27B research evaluation: 11.23% lower recorded perplexity',x=.10,ha='left',fontsize=16,weight='bold')
finish(fig,'01_quality_series','Source S01 · Limited WikiText evaluation; overlapping windows; no confidence intervals.\nSelected checkpoint result. This is not a general accuracy or benchmark-leaderboard claim.')
d=rows('deployment_series.csv');unique=[]
for r in d:
 if r not in unique:unique.append(r)
y=[float(r['perplexity'])for r in unique];best=min(y)
fig,ax=plt.subplots(figsize=(9,5.6));xx=np.arange(len(y));ax.plot(xx,y,'o-',lw=2,color=ORANGE,ms=6,label='Deployment evaluation series')
ax.axhline(min(values),color=BLUE,ls='--',lw=1.3,label=f'Selected research result: {min(values):.4f}')
for i,v in enumerate(y):ax.annotate(f'{v:.4f}',(i,v),xytext=(0,12 if i!=2 else -22),textcoords='offset points',ha='center',fontsize=10)
ax.set(xticks=xx,xticklabels=[r['record']for r in unique],ylabel='Recorded perplexity · lower is better',xlabel='Anonymized evaluation order · spacing is not training time',ylim=(9.5,10.17));ax.grid(axis='y',alpha=.2);ax.legend(frameon=False,loc='upper right')
fig.suptitle('Deployment candidate: selected result 9.6245',x=.10,ha='left',fontsize=16,weight='bold')
finish(fig,'02_deployment_series','Sources S01–S02 · Selected result is 0.201% above the research result, not an accuracy loss.\nAn exact duplicate initial row is collapsed. Later evaluations worsen; all distinct points are shown.')
a=rows('component_latencies.csv');series={t:np.array([float(r['latency_ms'])for r in a if int(r['threads'])==t])for t in range(1,5)}
fig,(left,right)=plt.subplots(1,2,figsize=(11,5.9));colors={1:GRAY,2:'#608595',3:'#c38a65',4:BLUE}
for t,v in series.items():
 s=np.sort(v);right.step(s,np.arange(1,len(s)+1)/len(s),where='post',label=f'{t} thread'+('s'if t>1 else''),lw=1.6,color=colors[t])
for p,label,color,marker in [(.5,'Median',BLUE,'o'),(.99,'p99',ORANGE,'s')]:
 vals=[np.sort(series[t])[min(len(series[t])-1,int(len(series[t])*p))]for t in range(1,5)]
 left.plot(range(1,5),vals,marker+'-',label=label,color=color,lw=2)
left.plot(range(1,5),[float(np.mean(series[t]))for t in range(1,5)],'d--',label='Mean',color=GRAY)
left.set(xticks=range(1,5),xlabel='Threads',ylabel='Component latency (ms)',ylim=(0,11));left.grid(axis='y',alpha=.2);left.legend(frameon=False)
right.set(xlabel='Component latency (ms)',ylabel='Fraction of timed trials',xlim=(0,11),ylim=(0,1.02));right.grid(alpha=.15);right.legend(frameon=False,loc='lower right')
fig.suptitle('CM4 component timing: faster median, worse tail at four threads',x=.10,ha='left',fontsize=15,weight='bold')
finish(fig,'03_component_latency','Sources S041–S044 · Linux CM4, fixed cold workload, 1.5 GHz; 256 trials/thread count.\nMedian: 3.8060 → 1.0323 ms. p99: 3.9165 → 10.1716 ms. Not full-model or bare-metal token latency.')
e=rows('numerical_agreement.csv');v=np.array([float(r['max_absolute_error'])for r in e]);fig,ax=plt.subplots(figsize=(9,5.6));xx=np.arange(1,len(v)+1)
ax.semilogy(xx,v,'o-',color=BLUE,lw=1,ms=3);ax.axhline(max(v),color=GRAY,ls='--',lw=1,label=f'Worst recorded: {max(v):.3e}')
ax.set(xlabel='Anonymized component comparison',ylabel='Maximum absolute difference · logarithmic scale',xlim=(0,65),ylim=(1e-15,1e-12));ax.grid(axis='y',which='major',alpha=.2);ax.legend(frameon=False)
fig.suptitle('Numerical agreement across 64 FP64 component checks',x=.10,ha='left',fontsize=16,weight='bold')
finish(fig,'04_numerical_agreement','Source S03 · Controlled component inputs; implementation withheld.\nThis does not establish full-model equality, answer quality, or lower-precision hardware agreement.')
metrics={'reference_perplexity':baseline,'research_perplexity':min(values),'relative_perplexity_reduction_percent':100*(baseline-min(values))/baseline,'deployment_perplexity':best,'deployment_vs_research_percent':100*(best/min(values)-1),'component_max_absolute_difference':float(max(v)),'component_comparisons':len(v),'latency_samples_per_thread':{str(t):len(s)for t,s in series.items()},'median_speed_ratio_1_to_4':float(np.median(series[1])/np.median(series[4]))}
# Percentile rule in the source uses floor(N*p), not averaged middle samples.
metrics['median_speed_ratio_1_to_4']=float(np.sort(series[1])[128]/np.sort(series[4])[128])
(ROOT/'data/derived_metrics.json').write_text(json.dumps(metrics,indent=2)+'\n')
print(json.dumps(metrics,indent=2))

# Physical endpoint observations. Build labels disclose outcomes, not methods.
h=rows('cm4_api_latency.csv')
fig,ax=plt.subplots(figsize=(9,5.8));positions=np.arange(2);width=.32
for label,offset,color in [('A',-width/2,GRAY),('B',width/2,BLUE)]:
 values=[float(next(r['client_seconds'] for r in h if r['build']==label and int(r['request_number'])==n)) for n in (1,2)]
 bars=ax.bar(positions+offset,values,width,label='Build '+label,color=color)
 for bar,value in zip(bars,values):
  ax.annotate(f'{value:.2f} s',(bar.get_x()+bar.get_width()/2,value),xytext=(0,7),textcoords='offset points',ha='center',fontsize=11)
ax.set(xticks=positions,xticklabels=['First request in session','Repeated request in same session'],ylabel='Client completion time (seconds)',ylim=(0,660))
ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True);ax.legend(frameon=False,loc='upper right')
fig.suptitle('Physical CM4: repeated request completes in 269.08 seconds',x=.10,ha='left',fontsize=15,weight='bold')
finish(fig,'05_cm4_api_latency','Sources S11A–S11B · 8 GB CM4, 1.5 GHz; same 13-token prompt, one output token.\nAll four observations shown. One session/build; no uncertainty estimate or throughput claim.')
a=float(next(r['client_seconds'] for r in h if r['build']=='A' and r['request_number']=='2'))
b=float(next(r['client_seconds'] for r in h if r['build']=='B' and r['request_number']=='2'))
metrics['cm4_repeated_request_speed_ratio']=a/b
metrics['cm4_repeated_request_latency_reduction_percent']=100*(1-b/a)
metrics['cm4_api_observations']=len(h)
(ROOT/'data/derived_metrics.json').write_text(json.dumps(metrics,indent=2)+'\n')

# Added 2026-11-13: seconds per generated token on the CM4, one bar per model (different models, not a speedup).
b=json.loads((ROOT/'data/cm4_seconds_per_token.json').read_text())['bars']
fig,ax=plt.subplots(figsize=(9,5.4));yy=np.arange(len(b))[::-1]
cols=[GRAY,'#b3832c',BLUE,'#1d6b48']
ax.barh(yy,[x[2] for x in b],color=cols,height=.56)
for y,x in zip(yy,b):ax.annotate(f'{x[2]:.2f} s',(x[2],y),xytext=(6,0),textcoords='offset points',va='center',weight='bold')
ax.set(yticks=yy,yticklabels=[f'{x[0]}\n{x[1]} · {x[3]}' for x in b],xlabel='Seconds per generated token · lower is faster',xlim=(0,4.2))
ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True)
fig.suptitle('Physical CM4: seconds per generated token, by model',x=.10,ha='left',fontsize=15,weight='bold')
fig.text(.08,.035,'Sources S13–S16 · 8 GB CM4, 1.5 GHz; one run per bar; no uncertainty estimate.\nDifferent models are different workloads; drafting made E4B slower and is off by default.',fontsize=9,color=GRAY,va='bottom')
fig.subplots_adjust(left=.30,right=.95,top=.86,bottom=.22)
fig.savefig(OUT/'06_cm4_seconds_per_token.png',dpi=180,metadata={'Software':'Matplotlib; sanitized measurement data'})
fig.savefig(OUT/'06_cm4_seconds_per_token.svg',metadata={'Date':None,'Creator':'Matplotlib; sanitized measurement data'})
plt.close(fig)
