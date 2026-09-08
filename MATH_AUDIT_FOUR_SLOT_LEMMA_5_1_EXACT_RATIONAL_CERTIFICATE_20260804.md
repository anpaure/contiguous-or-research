# Independent audit: four-slot Lemma 5.1 and its exact rational certificate

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_FOUR_SLOT_TWO_EFFICIENT_NORMALIZED_SUBRANGE_AND_PULSE_GATE_20260804.md`  
**Scope:** Lemma 5.1, including all sixteen rational inequalities in
(5.13).  
**Verdict:** **PASS**.  Every calculus implication has the stated direction,
and every rational certificate is strictly positive.  No numerical search,
floating-point approximation, or external solver is used.

## 1. The periodized-tail bound

Put

\[
 h(u)=ue^{-au^2},\qquad a={\pi\over4},
 \qquad x=1+t+s.
\]

On the domain

\[
 {1\over2}\le t\le{2\over3},\qquad0\le s\le{t\over2},
\]

one has `x>=3/2`.  Since

\[
 h'(u)=(1-2au^2)e^{-au^2},
\]

the function is decreasing on `[3/2,infinity)`.  Separate the first two
terms of the tail.  For every later right endpoint, monotonicity gives

\[
 t h(x+kt)
 \le\int_{x+(k-1)t}^{x+kt}h(u)\,du\qquad(k\ge2).
\]

Consequently

\[
\begin{aligned}
 \sum_{q\ge1}h(1+s+qt)
 &=h(x)+h(x+t)+\sum_{k\ge2}h(x+kt)\\
 &\le h(x)+h(x+t)+{1\over t}\int_{x+t}^{\infty}h(u)\,du\\
 &=h(x)+h(x+t)+{e^{-a(x+t)^2}\over2at}.
\end{aligned}
\]

This is exactly (5.2); the integral begins at the correct mesh point and
has the correct upper-bound direction.  Substitution gives
`W_t(s)>=H_t(s)`.

## 2. Strict concavity of the lower function

Write

\[
 v=1-t-s,qquad
 E_t(s)={e^{-a(x+t)^2}\over2at}.
\]

Twice differentiating (5.3) gives the exact identity

\[
 H_t''(s)=h''(1-s)-h''(1+s)+h''(v)
           -h''(x)-h''(x+t)-E_t''(s).              \tag{A.1}
\]

The derivative formulas are

\[
 h''(u)=2au(2au^2-3)e^{-au^2},
\]

\[
 h'''(u)=2ae^{-au^2}(-4a^2u^4+12au^2-3),           \tag{A.2}
\]

and, with `z=x+t>=2`,

\[
 E_t''(s)={2az^2-1\over t}e^{-az^2}>0.             \tag{A.3}
\]

The ranges used in the theorem are exact:

\[
 1-s,1+s\in[2/3,4/3],\quad
 v\in[0,1/2],\quad x\ge3/2,\quad x+t\ge2.         \tag{A.4}
\]

On `[2/3,4/3]`, put `q=au^2`.  The rational bounds

\[
 {157\over200}<a<{11\over14}
\]

give

\[
 {1\over3}<{157\over450}\le q
 <{88\over63}<{3\over2}.
\]

The polynomial `p(q)=-4q^2+12q-3` has

\[
 p'(q)=12-8q>0,qquad p(1/3)={5\over9}>0.
\]

Thus `h'''(u)>0` throughout that interval, and

\[
 h''(1-s)-h''(1+s)\le0.                             \tag{A.5}
\]

Also `h''(v)<=0`.  At the other end,

\[
 2a(3/2)^2-3
 >2{157\over200}{9\over4}-3={213\over400}>0,
\]

so `h''(x),h''(x+t)>0`.  Equations (A.1)--(A.5), and especially the
strictly positive term (A.3) which is subtracted, prove

\[
                         H_t''(s)<0.
\]

A concave function lies above its endpoint chord, so its minimum on
`[0,t/2]` is attained at an endpoint.  The theorem's endpoint reduction is
therefore valid.

## 3. Audit of every endpoint monotonicity choice

The positive arguments in (5.11)--(5.12) lie in `[0,3/4]`.  On this
interval

\[
 2au^2<2{11\over14}{9\over16}={99\over112}<1,
\]

so `h` is increasing.  Every negative `h` term has argument at least
`5/4`, and

\[
 2a(5/4)^2>2{157\over200}{25\over16}={157\over64}>1,
\]

so `h` is decreasing there.

It follows, for `t in [ell_i,u_i]`, that the positive terms take their
valid lower endpoint bounds at

\[
 1-u_i,qquad 1-u_i/2,qquad 1-3u_i/2,
\]

while the negative terms take their valid upper bounds at

\[
 1+\ell_i,quad1+2\ell_i,quad1+\ell_i/2,quad
 1+3\ell_i/2,quad1+5\ell_i/2.
\]

The final tail term decreases with `t`: both its factor `1/t` and its
Gaussian factor decrease, while its argument is respectively `1+2t` or
`1+5t/2`.  Evaluating its upper bound at `ell_i` is therefore also in the
correct direction.  This reproduces (5.11) and (5.12) without an omitted
case or a reversal.

## 4. Taylor bounds

For `z>=0`, Taylor's theorem with Lagrange remainder gives

\[
 e^{-z}-Q_5(z)={e^{-\xi}z^6\over6!}>0
 \quad(0<\xi<z).
\]

Also `e^z>=P_8(z)>0`, hence `e^{-z}<=1/P_8(z)`.  Combining these with
`157/200<a<11/14` proves, for every `u>=0`,

\[
 h_-(u)\le h(u)\le h_+(u).
\]

Thus all terms in (5.11)--(5.12) are replaced in the proof-safe direction.

## 5. Independent exact recomputation of all sixteen inequalities

All polynomial evaluations below were expanded over the rationals.  For
each `i`, write in lowest terms

\[
 B_i^{(0)}-{1\over1000}={N_i^{(0)}\over D_i^{(0)}},
 \qquad
 B_i^{(1)}-{1\over50}={N_i^{(1)}\over D_i^{(1)}}.
\]

Every denominator is positive: `ell_i>0`, and every `P_8` value is a sum
of positive rational terms.  The exact reduced numerators are as follows.

### Row `B_i^(0)-1/1000`

```text
i=0  20542968598823496078377775465897054293714771451344765090601138344775398423
i=1  14045765238315142881483067764305208846996558372955467747764912448129646394898164848117003455143259638364365720046598560317
i=2  580354222779803053992521638113128328908465625294205621672774681575293955987533161896382433697281
i=3  119325915708558209372671057400988078809390511563288301820788819641957454620270931225090285217
i=4  23024058752538750008143978929570775603839578890474443566885454538637889153874131090153749913556976780707
i=5  746439047163919005911672329628888012703486968598250548930983719243170621533714566637699780429935542209437267741619869
i=6  3518651963649991709233777658609973846662502698021080949929828217047711471337324132419029406922995079
i=7  25265299015317545010844736221428170091187348130978451015508581802015813252803199621244757878538590705401
```

### Row `B_i^(1)-1/50`

```text
i=0  114254231289401896081271969431410894190644489808178797810780309906421663045503709098651291392708822036352160619970074931
i=1  449565655679318488126624398403409133982372810971671398527383432339131405722130894621979452580343381413786910148846929668712316873060846615478343313159047609767097081746130019196797277599
i=2  378323037915507237682538644702824405783949335322741616268908349549388353271121899571988388257223828667707883998106116178463927065325193605080751211801175546832202141174121
i=3  217858071481684908324060449236920726713425837342449732347641264969205968517056374119946797985637210562465711774823065749009860765490112342798157735436174422011933537911
i=4  2423246196620063586739125726845374290715384611732359533908539080730473980728225522566561022763385421878010647534894018931576636530778631915002852759
i=5  3073619626859184419258699771066872655283008630768011776904794302831609201156312963429661389917199388574030975041761108949212522353690935608849743390273261572258261754824507
i=6  11979019716325505994988473208625242776315283878069190869209607230739128305987064062489563676421467163407059681685766006447502900351488636241195292936090469533
i=7  4734693756556780527600519821763678281290629763185732338805507580919470361451386950791353558096837709234342824647274795826887147215950804075149762945270505176642994641920097
```

All sixteen integers are positive, independently verifying every checkmark
in (5.13).

The exact smallest margin in the first row occurs at `i=0` and is

\[
 {20542968598823496078377775465897054293714771451344765090601138344775398423
  \over
  125631541096196862368181725235366431847109930423867223481884565881122455552000}.
                                                               \tag{A.6}
\]

It is strictly larger than `1/7000`, because cross-multiplication leaves
the positive integer

```text
18169239095567610180462703025912948208893469735546132152323402532305333409000.
```

The exact smallest margin in the second row occurs at `i=7` and is

\[
 {4734693756556780527600519821763678281290629763185732338805507580919470361451386950791353558096837709234342824647274795826887147215950804075149762945270505176642994641920097
  \over
  1985199630122639468687156534075233927279746572535902985737323185809519188977812654605783272524891700078639162329519471619497529362426783309497443989878121367883459809743334150}.
                                                               \tag{A.7}
\]

It is strictly larger than `1/450`, because cross-multiplication leaves
the positive integer

```text
145412560327911768733077385718421299301036820897676566725155225604242473675311473250325828618685269076815108761754186502601686884751078524319949335493605961605887779120709500.
```

Consequently the certificate actually proves the stronger uniform bounds

\[
 \boxed{B_i^{(0)}>{1\over875},\qquad
        B_i^{(1)}>{1\over45}\quad(0\le i<8).}       \tag{A.8}
\]

Indeed, `1/1000+1/7000=1/875` and
`1/50+1/450=1/45`.

## 6. Conclusion and scope

Strict concavity reduces `H_t` to its two endpoints, the rational endpoint
bounds are valid uniformly on all eight intervals, and (A.6)--(A.8) give
strict positivity with room to spare.  Therefore

\[
 H_t(s)>0\quad\Longrightarrow\quad W_t(s)>0
\]

on the full rectangle of Lemma 5.1.  The deduction of Theorem 5.2 from
`dF_{At}(As)/ds=-2A^2W_t(s)` then has the correct strict sign.

This audit certifies Lemma 5.1 and its use in the low-period closure.  It
does not assert the stronger global pulse inequality or, by itself, settle
the other four-slot efficiency regimes.
