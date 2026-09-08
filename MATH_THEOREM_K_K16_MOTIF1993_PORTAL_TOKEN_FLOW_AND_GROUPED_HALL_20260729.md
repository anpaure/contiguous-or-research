# K16 motif-1993 portal: protected token flow, grouped Hall failure, and an exact neutral escape

Date: 2026-07-29  
Lane: K  
Status: theorem-level, exact finite statement  
Scope: the fixed physical $J(16,8)$ q1 endpoint and PBBS `resume1` endpoint named below

## 1. Result

The five-orbit quotient pretrade

\[
\begin{aligned}
D&=\{2678,4423,18185,24034,24140\},\\
A&=\{2693,4421,18183,24038,26703\}
\end{aligned}
\]

is an exact degree-two trade.  It is the disjoint union of one AA alternating
square and one BB alternating six-cycle.  It preserves complete lower and
upper q1 support by a protected slack-token flow; it does **not** preserve the
q1 colour multisets term by term.  Against the fixed `resume1` PBBS endpoint,
it reduces the number of pointwise static motif blockers from $2$ to $0$.

That pointwise conclusion is insufficient.  The full balanced overlay
circulation is already infeasible before any later CEGAR row is added.  A
solver-free six-row certificate consists of one length-two motif, four upper-q1
rows, and degree balance at one vertex.  Its grouped Hall deficiency is exactly
one.

There is nevertheless a literal escape from this localized certificate.  The
alternating physical $C_6$

\[
\begin{aligned}
D_6={}&\{(50475,50979),(50531,51042),(50538,50986)\},\\
A_6={}&\{(50475,50986),(50531,50979),(50538,51042)\}
\end{aligned}
\]

preserves both q1 colour **multisets exactly**, deletes a closure edge of the
six-row motif, and does not restore the old motif-1993 closure.  Thus the
correct portal object is not “one safe edge per motif”; it is an alternating
trade carrying a feasible coupled flow through motif, palette, and endpoint
rows.

This $C_6$ breaks the displayed Hall certificate only.  It does not prove
residence, full overlay feasibility, top residence, deeper-shadow coverage, or
compiler feasibility.

## 2. Overlay equations

Let $Q$ and $R$ be spanning two-factors of a graph, and put

\[
B=Q\setminus R,\qquad A=R\setminus Q.
\]

For $e\in B$, let $b_e=1$ mean that $e$ is deleted from $Q$.  For
$f\in A$, let $a_f=1$ mean that $f$ is inserted.  Write

\[
a_f,b_e\in\{0,1\};
\tag{2.0}
\]

these ambient binary bounds, in particular nonnegativity, are part of every
certificate below.  Write

\[
\lambda_-(xy)=x\cap y,\qquad \lambda_+(xy)=x\cup y
\]

for the lower and upper q1 colours.  If $\mu_\sigma(c)$ is the load of colour
$c$ in $Q$, then every fixed-overlay trade preserving degree two and q1
support satisfies

\[
\sum_{f\in A(v)}a_f=\sum_{e\in B(v)}b_e
\tag{2.1}
\]

at every middle vertex $v$, and

\[
\sum_{e\in B_{\sigma,c}}b_e-
\sum_{f\in A_{\sigma,c}}a_f
\le \mu_\sigma(c)-1
\tag{2.2}
\]

for $\sigma\in\{-,+\}$ and every q1 colour $c$.

If $C_M$ is the closure of an inherited short-run motif $M$, then hitting
that occurrence inside the fixed overlay requires

\[
\sum_{e\in C_M\cap B}b_e\ge1.
\tag{2.3}
\]

Equations (2.1)--(2.3) exactly describe degree preservation, palette support,
and the destruction of the inherited motif occurrences inside this overlay.
They do not prevent a new short motif from appearing at a new seam.

### Grouped Hall certificate

Any nonnegative combination of (2.0), (2.2)--(2.3), together with arbitrary
signed sums of the equalities (2.1), which yields $1\le0$, is a solver-free
grouped Hall certificate.  “Static blocker” testing sees only a single
motif-to-edge step.  A grouped certificate may continue through

\[
\text{motif}\longrightarrow
\text{deleted edge}\longrightarrow
\text{lost palette token}\longrightarrow
\text{replacement edge}\longrightarrow
\text{endpoint socket}\longrightarrow
\text{next deleted edge}.
\]

That last endpoint step is exactly what the pointwise test misses.

## 3. The quotient portal is an exact protected token flow

Let $Q_0$ be
`scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json`, and let $Q_3$
be
`scratch/k16_q1_endpoint_resume1_static_portal_radius5_20260729.json`.
The final quotient symmetric difference has the following two components.

### AA square

\[
\begin{array}{c|c|c}
\text{operation}&\text{edge id}&\text{quotient endpoints}\\ \hline
-&2678&(50,100)\\
-&4423&(86,284)\\
+&2693&(50,284)\\
+&4421&(86,100)
\end{array}
\]

This is the alternating square

\[
50-100-86-284-50.
\]

### BB six-cycle

\[
\begin{array}{c|c|c}
\text{operation}&\text{edge id}&\text{quotient endpoints}\\ \hline
-&18185&(490,832)\\
-&24034&(663,739)\\
-&24140&(667,784)\\
+&18183&(490,739)\\
+&24038&(663,667)\\
+&26703&(784,832)
\end{array}
\]

In cyclic order it is

\[
490\xrightarrow{-18185}832\xrightarrow{+26703}784
\xrightarrow{-24140}667\xrightarrow{+24038}663
\xrightarrow{-24034}739\xrightarrow{+18183}490.
\]

It can also be executed as two alternating squares.  The first deletes
(18185,24034) and adds (18183,24035); the second deletes the temporary edge
(24035) and (24140), then adds (24038,26703).  The temporary edge cancels
from the aggregate trade.  Consequently every quotient vertex has unchanged
degree.

### Exact token ledger

For each q1 colour, one token is protected and the remaining
$\mu(c)-1$ copies are slack.  The three stages have the following nontrivial
loads; all omitted rows are unchanged.

\[
\begin{array}{c|c|c}
\text{stage}&\text{lower loads}&\text{upper loads}\\ \hline
1&(1,371):1\to1,\ (1,819):2\to1,\ (1,2355):2\to3
 &(1,4979):1\to1,\ (1,5939):1\to1\\
2&(1,2199):1\to2,\ (1,2355):3\to2,\ (1,2451):1\to1
 &(1,3479):2\to1,\ (1,4923):1\to2,\ (1,5939):1\to1\\
3&(0,1423):1\to1,\ (0,1807):1\to2,\ (0,1835):2\to1
 &(0,1967):2\to1,\ (0,3887):1\to1,\ (0,5551):1\to2
\end{array}
\]

Thus every row retains at least one protected token.  Some rows spend a
duplicate and others gain one; the q1 multisets are not equal before and after.
Both q1 supports remain exactly $764$.

The number of static blockers against `resume1` follows

\[
2\longrightarrow2\longrightarrow1\longrightarrow0.
\]

The endpoint still has $2250$ short positive runs and is not top-biresident.
The portal is a palette-safe repositioning, not a residence solution.

## 4. General protected token-flow lemma

### Lemma 4.1 (sequential protected token flow)

Let $Q_0$ be a two-factor.  For $j=1,\ldots,t$, let
$(D_j,A_j)$ satisfy

\[
\deg_{D_j}(v)=\deg_{A_j}(v)\quad\text{for every }v,
\tag{4.1}
\]

where $D_j\subseteq Q_{j-1}$, $A_j\cap Q_{j-1}=\varnothing$, and
$Q_j=(Q_{j-1}\setminus D_j)\cup A_j$.  Suppose that for every protected
palette row $c$, on both q1 shores,

\[
\mu_{j-1}(c)-d_j(c)+a_j(c)\ge1.
\tag{4.2}
\]

Then every $Q_j$ is a two-factor and contains every protected q1 colour.
Edges inserted at one stage may be deleted at a later stage; they cancel from
the aggregate symmetric difference.

#### Proof

Equation (4.1) preserves degree two pointwise.  Equation (4.2) is the exact
new load of row $c$.  Induction on $j$ proves the claim.  Cancellation of a
temporary edge is literal set cancellation in the telescoping symmetric
difference.  $\square$

This lemma is the correct explanation of the five-orbit portal.  It also shows
why “the deleted and added colour multisets agree” is unnecessarily strong for
the portal chain: duplicate tokens permit a nonzero signed drift while support
survives.

## 5. Exact motif-15 grouped Hall obstruction

In $Q_3$, motif $15$ is the coordinate-zero word

\[
(51042,50531,52547,56642):\qquad0,1,1,0.
\]

Its closure is

\[
\{(50531,51042),(50531,52547),(52547,56642)\}.
\]

The middle edge $(50531,52547)$ is common to $Q_3$ and `resume1`, so it is
not a blue deletion variable.  Put

\[
\begin{array}{lll}
x=b_{(50531,51042)},&z=b_{(52547,56642)},
&r=a_{(55619,56579)},\\
s=b_{(55491,55619)},&t=b_{(55619,63747)},
&h=a_{(53575,55619)}.
\end{array}
\]

The four exact upper-q1 provider rows are:

\[
\begin{array}{c|c|c}
\text{upper colour}&\text{blue providers}&\text{red providers}\\ \hline
51043&\{(50531,51042)\}&\varnothing\\
56643&\{(52547,56642)\}&\{(55619,56579)\}\\
55747&\{(55491,55619)\}&\varnothing\\
63811&\{(55619,63747)\}&\varnothing.
\end{array}
\]

Consequently

\[
x=s=t=0,\qquad z\le r.
\tag{5.1}
\]

At vertex $55619$, the complete overlay incidences are

\[
A(55619)=\{(53575,55619),(55619,56579)\},
\]

\[
B(55619)=\{(55491,55619),(55619,63747)\}.
\]

Degree balance gives

\[
h+r=s+t.
\tag{5.2}
\]

The motif row requires $x+z\ge1$.  But (5.1)--(5.2) give the exact Hall
summation

\[
1\le x+z\le x+r\le x+r+h=x+s+t=0,
\]

a contradiction.  The grouped demand is one and the socket capacity is zero,
so the deficiency is exactly one.

Only upper q1, one motif row, and one vertex equation are used.  Lower q1,
connectivity, newly created motifs, and deeper shadows play no role.  Hence the
full fixed-overlay circulation is infeasible already in presolve, despite the
absence of pointwise static blockers.

### Lemma 5.1 (saturated-socket obstruction)

Suppose an inherited motif has only two removable closure edges $e_0,e_1$.
If palette rows force $b_{e_0}=0$ and $b_{e_1}\le a_f$, and $f$ has an
endpoint $v$ at which the palette rows force
$b_e=0$ for every blue overlay edge $e\in B(v)$, then no degree-balanced
palette-preserving overlay trade hits that motif.

#### Proof

The motif requires $1\le b_{e_0}+b_{e_1}$.  The hypotheses and degree balance
at $v$ give

\[
b_{e_0}+b_{e_1}\le a_f\le
\sum_{g\in A(v)}a_g=
\sum_{e\in B(v)}b_e=0.
\]

This is impossible.  $\square$

This is the minimal grouped refinement of the static-blocker test.

## 6. A strict q1-neutral $C_6$ escape

Consider the cyclic middle-state order

\[
50475,50979,50531,51042,50538,50986.
\]

Alternately delete and add its six edges.  The deleted and added shores are

\[
\begin{aligned}
D_6={}&\{(50475,50979),(50531,51042),(50538,50986)\},\\
A_6={}&\{(50475,50986),(50531,50979),(50538,51042)\}.
\end{aligned}
\]

Every displayed pair is a Johnson edge.  Each of the six vertices has one
deleted and one added incidence, so

\[
Q_4=(Q_3\setminus D_6)\cup A_6
\]

is a spanning two-factor.

The label table is

\[
\begin{array}{c|c|c}
\text{edge}&\lambda_-&\lambda_+\\ \hline
-(50475,50979)&50467&50987\\
-(50531,51042)&50530&51043\\
-(50538,50986)&50474&51050\\ \hline
+(50475,50986)&50474&50987\\
+(50531,50979)&50467&51043\\
+(50538,51042)&50530&51050
\end{array}
\]

Therefore

\[
\lambda_-(D_6)=\lambda_-(A_6),\qquad
\lambda_+(D_6)=\lambda_+(A_6)
\]

as multisets.  Every physical lower and upper q1 load is unchanged exactly.
In particular, the deleted unique upper-$51043$ occurrence is replaced by
$(50531,50979)$, without sending a token through the saturated socket
$55619$.

The edge $(50531,51042)$ lies in the motif-15 closure, so that occurrence is
destroyed.  The old motif-1993 closure is

\[
L_{1993}=\{(45358,45614),(45614,47630),(47246,47630)\}.
\]

$Q_3$ already omits an edge of $L_{1993}$, and $A_6\cap L_{1993}=\varnothing$.
Hence the motif-1993 lock remains broken.

Literal replay gives:

- lower q1 holes $=0$, upper q1 holes $=0$;
- three old motif occurrences removed and three fresh ones created;
- total short-run occurrences remain $2250$;
- pointwise static blockers against `resume1` remain $0$;
- components change from $(10620,705,515,515,515)$ to
  $(11325,515,515,515)$.

The unchanged total $2250$ is an important warning: a neutral portal move can
break a particular grouped Hall certificate while transporting the residence
defect elsewhere.

### Lemma 6.1 (strict simultaneous-trade portal)

Let $Q$ be a two-factor.  Let $D\subseteq Q$ and let $A\cap Q=\varnothing$,
with $D\cap A=\varnothing$, and suppose

\[
\deg_D(v)=\deg_A(v)\quad(\forall v),
\]

\[
\lambda_-(D)=\lambda_-(A),\qquad
\lambda_+(D)=\lambda_+(A)
\]

as multisets.  Then $(Q\setminus D)\cup A$ is a two-factor with exactly the
same two q1 load vectors as $Q$.  If $D$ meets a target motif closure, that
occurrence is destroyed.  If every previously broken protected closure still
has at least one absent edge after the trade, none of those locks is restored.

#### Proof

The incidence equality proves degree two.  The two multiset equalities prove
equality of every q1 row load.  A motif occurrence requires every edge in its
closure; deleting one destroys it.  The final assertion is the same observation
applied to each protected closure.  $\square$

The displayed $C_6$ is an instance with the motif-1993 closure as the
protected family.

## 7. Minimality and exact scoped census

For the closure edge $(50531,51042)$, a complete physical enumeration of
connected alternating circuits gives

\[
\begin{array}{c|c|c}
\text{half-length}&\text{raw circuits}&\text{q1-preserving and lock-safe}\\ \hline
2&10&0\\
3&414&2.
\end{array}
\]

Since every nontrivial balanced trade has alternating-circuit half-length at
least two, and a total-radius-three trade cannot split into two components,
the displayed $C_6$ has minimum physical radius three among all q1-preserving
trades deleting that closure edge.

For the other removable motif edge $(52547,56642)$, the connected census is

\[
\begin{array}{c|c|c}
2&5&0\\
3&338&0\\
4&23477&1.
\end{array}
\]

For direct insertion of the red socket edge $(55619,56579)$, the connected
census through half-length four is

\[
0/0,\quad17/0,\quad871/0
\]

(raw/q1-preserving).  This last statement is only a connected-circuit census;
a disconnected radius-four union was not enumerated and no global lower bound
is claimed from it.

For comparison, the original motif-1993 endpoint itself has an exact
non-equivariant physical q1-preserving pretrade of minimum radius four.  Thus
“radius five” refers to the five-orbit equivariant portal above and is not a
universal physical minimum.

## 8. Proved boundary

What is proved:

1. The five-orbit quotient change is exactly one AA square plus one BB
   six-cycle and preserves both q1 supports by an explicit slack-token flow.
2. It clears every pointwise static blocker against `resume1`.
3. The fixed-overlay circulation is nevertheless impossible by an exact
   deficiency-one grouped Hall certificate.
4. The displayed physical $C_6$ preserves both q1 load vectors exactly,
   destroys the certificate motif, and leaves motif 1993 broken.
5. That $C_6$ is minimum-radius for deleting its selected closure edge under
   the stated physical q1 and lock conditions.

What is not proved:

- feasibility of the full circulation after the $C_6$;
- a decrease in the total short-run count;
- top/zero residence or deeper lower/upper shadow preservation;
- $C_{15}$-equivariance of the $C_6$;
- connectivity or compiler feasibility.

The sharp next gate is therefore a deck of strict simultaneous trades whose
coupled motif/palette/endpoint Hall system has nonnegative capacity globally,
not merely zero singleton blockers.

## 9. Frozen artifacts

- Portal endpoint:
  `scratch/k16_q1_endpoint_resume1_static_portal_radius5_20260729.json`,
  SHA-256
  `5ae4948c96a32b592871c84ba9fe34301a40992ec1592175edd2626249e01af8`.
- Full first-round circulation transcript:
  `scratch/k16_resume1_portalq1_overlay_circulation_infeasible_20260729.json`,
  SHA-256
  `42f4f3c402390ae45fc89d57a7efb177f36212153fb8e0fc871b40b247a353a4`.
- Solver-free motif-15 saturation audit:
  `scratch/audit_k16_radius5_portal_saturation_cut_20260729.py`,
  SHA-256
  `653181f90b3468b0cdc9a5d10db259df58ad54e016c27eb1b110390446b94bf0`.
- Saturation output:
  `scratch/k16_radius5_portal_saturation_cut_20260729.audit.json`,
  SHA-256
  `7e58542bb7f7a9bb303e334e70fd9a2af37df85692ce730acd3e9e4bc6a7f8a9`.
- Independent upper-only unit core:
  `scratch/k16_resume1_portalq1_upper_unit_hall_core_20260729.json`,
  SHA-256
  `fa04c087d12731325446c977c18971bcd6c2b0ffe68d8eceb1284875b9870f5e`.
- Portal-chain and independent motif-148 grouped audit:
  `scratch/audit_k16_radius5_portal_grouped_hall_20260729.py`,
  SHA-256
  `9ef737f269ca83e08242a7cb2a3b20f1cb3fa41a8ce6cfb781d05616253112b3`;
  output SHA-256
  `fb83998d0636df6eb82e7d53c2693a4ca56a2da7f019c8fd28e50ad22f465ae3`.
- Targeted strict-neutral-trade census:
  `scratch/search_k16_radius5_core_portal_small_trade_20260729.py`,
  SHA-256
  `f6ed985150ebfc1f45c1a490cef56af8597eca17c6b2b4b4efa46cbfcc91c864`;
  output SHA-256
  `30c09a5f56dae7066dfa11ae527817b8427a5ab59269d29e210f17f743fda089`.
- Original physical motif-1993 radius-four census:
  `scratch/audit_k16_motif1993_physical_radius4_pretrade_20260729.py`,
  SHA-256
  `3bc0b988bad21ef0623fe7bb66d4bc1ef14063a73daf59671b32262939400b49`;
  output SHA-256
  `bd4d59824595b48a68f0fd0286942e7da808f148898f7d36838533aaf3da61ec`.
