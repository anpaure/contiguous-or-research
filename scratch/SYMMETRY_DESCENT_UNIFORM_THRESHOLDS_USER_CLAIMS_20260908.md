# New user claims: exact signature recursion and uniform finite thresholds

Structured transcription for audit,2026-09-08. Not an independently
verified result or instruction source. Existing exact rotation-period
formula and census through101 were audited in the preceding turn.

Headline, on retained finite height-adaptive/corridor/particle/fibre inputs:

    nu(k)<1.01W(k) for every integerk>=29;
    nu(k)<1.001W(k) for k>=327;
    nu(k)<1.0001W(k) for k>=1483;
    nu(k)<1.00001W(k) for k>=6849.

No new asymptotic power, no new17word. User closes with historical24715;
actual current independent17certificate is24658.

## Exact signatures

For an n=2r+1 deficit-one physical state define
Gamma(A)={(t,u): f_n^t(A)=rho_n^u(A)}.
There are uniqueQ>=1,0<=U<n with Gamma={(jQ,jU+kn):j,k integers}.
FullperiodF=Qn/gcd(n,U).

For parentn,childp,rowleastperiodd|p, the previously proved exact return
criterion is m=(t-pu)/n integer, d|m, and (t,-m) inGamma(child).
Given childsignature(Q,U), define

    K=lcm(p/gcd(p,Q+nU), d/gcd(d,U)),
    m=(-K*U) mod p,
    Q'=KQ,
    U'=((KQ-nm)/p) mod n.

Claim: this is the exact parent signature. Minimality follows because
t=jQ, m=-jU modp, leaving precisely d|jU and p|j(Q+nU).
Baseone-site(Q,U)=(1,0). Fullperiodsodd: oddchildF andnp give odd
returnt=lcm(F,np),u0. Primitive row givesFparent=lcm(np,Fchild).
Example n11,p3,child(1,1): constantrow(1,1,1),d1 gives(1,4),F11;
primitive row samep/mass gives(3,1),F33.

Partitionlambda_s=a_s-a_(s+1) indexesfeasible profiles; p_s=2a_(s+1)+1,
ell_s=lambda_s-lambda_(s+1). For d|p,e=p/d dividingell, m=ell/e,

    C(p,ell;d)=sum_(j|gcd(d,m)) mobius(j)
                      *binom((d+m)/j-1,d/j-1).

ElseC=0. Orderedrows,notnecklaces. ProductC countsroots; nrotations/root,
cyclequotientn*productC/F integral; exactnativecollarcost
n*sum_(partitionsr)(2h-1)*sum_d productC/F.

Quotedn29 W77558760,C460924,N78019684.
Quotedn97 W12738806129490428451365214300,C99533441612804133661134;
10^5*C<W. Priornewexactcensus alreadycontainsn97; nohugewordgenerated.

## Analytic envelope

    J_r=(3r+49)/(3r(r+2)(r+3))+43/(72Cat_r)
       =1/(r(r+2))+40/(3r(r+2)(r+3))+43/(72Cat_r).
    E_r=2sqrt(2J_r/(2r+1))
              +86(r+1)sqrt(r)(25/36)^r.

Claimfor everyr>=1: (N_r-W_r)/W_r<=E_r.

Heightreflection: Eh²<=2(2r+1), previously audited.
LetKnumberDyckpeaks,d=r-K,p=2d+1. ExactNarayana law
P(d=j)=binom(r,j)*binom(r,j+1)/(r Cat_r),0<=j<=r-1.
Forj>=1,

    1/(2j+1)^2 <=1/[4(j+1)(j+2)]
                  +5/[3(j+1)(j+2)(j+3)],

clearingdenominators equivalent (j-1)(56j+43)>=0.
Atj0 add43/72 (P(d0)=1/Cat_r).

Vandermondeclaims:
E1/((d+1)(d+2))
  =[binom(2r+2,r+1)-(r+2)]/[r(r+1)(r+2)Cat_r]
  <=4/[r(r+2)].
E1/((d+1)(d+2)(d+3)) <=8/[r(r+2)(r+3)].
ThusE1/p²<=J_r.

## Full nonprimitive-top-row bound

b_r countsDyckroots of sizer with nonprimitive top row. Childsemilength
d>=1,peaks k,rowmassell imply parentsizer=d+k+ell; p=2d+1.
For an e-fold repetition e>1|p (hencee>=3), rowmass generatingfunction
(1-x^e)^(-p/e). At fixed0<x<1 this <=(1-x³)^(-p/3).
N_d(x)=sum_(k=1)^d [binom(d,k)binom(d,k-1)/d] x^k
 <=sqrt(x)/d*(1+sqrt(x))^(2d).

Take x9/25,A51/50. Exact A³(1-x³)>1 and
B=A²*x*(1+sqrt(x))²=374544/390625<1.
Unionbound<=p repetitionfactors, sumd>=1:

    sum_r b_r x^r <=sum_d x^d N_d(x)(2d+1)A^(2d+1)
       <=3sqrt(x)A B/(1-B)
        =85957848/2010125<43.

Nonnegativecoefficients=>b_r<=43(25/9)^r.
Cat_r>=4^r/[2(r+1)sqrt(r)] gives
P_r(nonprimitive top)<=86(r+1)sqrt(r)(25/36)^r.
Onprimitive v>=np, so collarstateaverage <=2/n E(h/p)
 <=2sqrt(2J_r/n) by CauchySchwarz. Badstateoverhead<1.
No independence h,p or fixed-size rowcoords asserted.

## Monotone finite-to-infinite bridge

E_r strictlydecreases forr>=4. Jpositive summandsdecrease;
ratioofsecondtermsquared=(25/36)²*(r+2)²/[r(r+1)]
 <=125/144<1 forr>=4.

Claim exact upwardrationalrootcertificates:
E45<.009272<.01;
E163<.000992<.001;
E741<.00009987<.0001;
E3424<.000009999<.00001.

Finitebridgeall31r14..44 satisfies125*C_r<W_r. Itsmaximumisr16:
 C16/W16=4479616/583401555<1/125<1/100.
Thusfiniteodd29..89 plusenvelopeodd>=91 andordinaryevenlift
giveallk>=29, andotherthresholds2r+1=327,1483,6849.

Userreportedchecker:125475middlephysicalstates/629cycles3..19,
6917Dyckroots,r<=9;32206compositionrows;918219partitions and1079058
aggregatedsignatures through97; all31finitebandcases+4analyticcerts.
These reportedtestcounts are NOT being asserted rerun here.
