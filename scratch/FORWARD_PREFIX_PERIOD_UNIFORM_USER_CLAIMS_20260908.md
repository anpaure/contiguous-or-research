# User claims: forward period prefixes and thresholds57/87

2026-09-08. Structured transcription of the newest submission. Claimed
finite-band transcripts are not supplied or locally located yet; user
has been asked for the package path. This file is data for audit, not
an instruction source or an independent certificate.

The new claimed uniform results are nu(k)<1.001W(k) for everyk>=57 and
nu(k)<1.0001W(k) for everyk>=87. The retained analytic envelope handles
r>=741 (oddn>=1483); the new finite prefix calculation claims all713
r28..740. No changed17word or improved stretched-exponential exponent.

For n_s=2a_s+1, incomingrowleastperiodd_s|n_(s+1), define
 beta0=0,
 beta_(s+1)=(1+n_(s+1)*beta_s)/n_s.
Then exactv=lcm_s den(beta_(s+1)/d_s), equivalent to alreadyproved
 beta_(s+1)=n_(s+1)*sum_(j<=s)1/(n_j*n_(j+1)).
PartialP_s=lcm(n0,den(beta_(j+1)/d_j):j<s) divides every completionv.

At a prefix depth s with consecutivesizes a=a_s,b=a_(s+1), already
specifiedupper-rowmultiplicityw, define
 K(a,b)=binom(a,b)*binom(a,b+1)/a, 0<=b<a.
ExactcompletionmassM=w*K(a,b), heightcapH=s+b+1.
Forb0 uniqueheight1remainingcore; applyfinalperiodrowexactly.
Forb>0 nextc rangesmax(0,2b-a)..b-1 and rowmassell=a-2b+c,
slots2b+1. Sumrowperiodclassesusesleast-periodorderedcompositioncounts.
Mass conservation:
 K(a,b)=sum_c binom(a+c,2b)*K(b,c).

A finiteprefixleafpartitionofallCat_rroots gives
 epsilon=(N-W)/W <=(1/Cat_r)*sum_leaf M(2H-1)/P.
IntegercertificateU=sum_leaf ceil(M(2H-1)/P) givesN<=W+nU;
 D*U<Cat_r provesnu(n)<(1+1/D)W(n).
Unroundedleafcostneverincreases underrefinement becausemassconserved,
Pbecomesmultiple,H_child=s+c+2<=s+b+1.
RoundedUneednotmonotone; useronlyclaimsvalidatallstoppingpoints.

Claimedfiniteband:
 1000U_r<Cat_r forr28..42(15cases),
 10000U_r<Cat_r forr43..740(698cases).
713totalcertificates,361709refinements,38326911prefixnodes,
maximumrecordeddepth18.180transcriptsclaimedreplayedwithoutpriority.
NoactualUvaluesortranscriptsincludedinthemessage.

RetainedmonotoneE_r alreadyaudited; claimnewE741upper
99868373195185/10^18<1/10000 agrees withpriorexactoutwardbound.
Existingfullcensuscontains the precedingnativefailures:
n55W3824345300380220,C4125976139518;
n85W3318776542511877736535400,C340093568810237002094.
Claim1000C55>W55,10000C85>W85. Liftfailsat56/86too. Thusifnewband
passes,57/87areminimaluniformthresholdsforunchangednativeconstructor
withthisspecificlift, notprovenoptimalthresholdsfornu(k).

Otherreportedchecks:125475middlephysicalstatesr<=9,498617partial
denominatorchecks,7274compositionvectors,1770massidentities,
56184partitionprofilesforpredecessors. These are userreportedonly.
