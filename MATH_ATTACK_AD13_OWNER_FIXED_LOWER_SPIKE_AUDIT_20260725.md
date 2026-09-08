# AD13: audit and integration of the owner-fixed lower spike

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

Throughout, \(m\ge3\), \(n=2m+1\), and
\(W=\binom{n}{m}\). Sections 1--4 use
\(2\le q\le H\le m-1\); later statements display any different range
explicitly.

## 0. Verdict

Section 5 of
PAIR_OMISSION_OWNER_FIXED_SPIKE_CHART_20260725.md is algebraically correct,
with three required corrections.

1. Its exact range is

   \[
   2\le q\le H\le m-1,
   \tag{0.1}
   \]

   because \(L_q\) must be nonempty in order to choose \(a_i\in L_q\).

2. Different switched occurrences generally lie in different conjugate
   factors \(\sigma_iF_A\), not together in the original \(F_A\).
   Integrality is recovered by the explicit post-selection literal
   row-run construction in Section 4 below.

3. The claimed \(1/4\) Haar constant is correct for the squared norm,
   equivalently the doubled factorial-floor polynomial. For the ordinary
   undoubled binomial floor excess the exact constant is \(1/8\).

After those corrections, the direct construction proves:

- the central edge is unchanged;
- every upper flag is fixed;
- the lower cross-Gram is nonnegative, with pair contribution at least
  one at the common depth;
- a selected corner has at most \(2t\) additional row runs;
- the upper and lower owner-fixed spikes form an occurrencewise commuting
  four-state product on the same central edge.

Thus concentrated lower spikes do not require a second principal
\(W\)-family: after the corner is chosen they are concatenated into one
literal word. The unresolved issue is its seam cost. The global
\(o(W/H)\) run budget is not proved, and the crude overhead is linear in
the number of activated occurrences.

The integration goes further than the source spike statement. Arbitrary
permutations inside each lower root realize arbitrary nested lower chains,
and arbitrary permutations outside each completed middle owner realize
arbitrary nested upper chains. Integral downward and upward Boolean flows
then give exact lower token-core balance and exact full-owner upper
balance; the \(d\)-owner lower completion has weighted spill \(o(W)\).
These two rematchings commute occurrencewise on the same principal owner
set. This is an algebraic same-owner product, not yet a simultaneous
two-sided chronology theorem. The sole remaining direct constant-one gate
is to choose the two balanced flows jointly so that their lower-forward
and upper-reverse MTF recurrences fail on only \(o(W/H)\) path pieces.

## 1. Exact central-edge legality

Fix an omitted pair \(A\), an exact local factor \(F_A\) on
\([n]\setminus A\), and distinct selected token occurrences

\[
 e_i=(S_i,Y_i),\qquad S_i\subset Y_i,\qquad 1\le i\le t.
\tag{1.1}
\]

Suppose

\[
 L_q(e_i)=L
\tag{1.2}
\]

for every \(i\). Define

\[
 \{b_i\}=L_{q-1}(e_i)\setminus L,\qquad
 a_i\in L,\qquad
 \sigma_i=(a_i\ b_i).
\tag{1.3}
\]

Both \(a_i,b_i\) lie in \(S_i\), while the omitted pair \(A\) is disjoint
from the entire source row. Hence

\[
 \sigma_iS_i=S_i,\qquad
 \sigma_iY_i=Y_i,
\tag{1.4}
\]

and \(\sigma_iF_A\) is an exact factor on the same omitted-pair universe.
At the corresponding start of the conjugate row it supplies exactly the
same central edge \((S_i,Y_i)\).

Every upper flag contains \(S_i\), hence contains both transposed
coordinates and is fixed setwise by \(\sigma_i\). For the lower chain:

\[
 \sigma_iL_p(e_i)=
 \begin{cases}
 L_p(e_i),&p<q,\\[2mm]
 (L\setminus\{a_i\})\cup\{b_i\},&p=q,\\[2mm]
 L_p(e_i),&p>q,\ a_i\notin L_p(e_i),\\[2mm]
 (L_p(e_i)\setminus\{a_i\})\cup\{b_i\},
   &p>q,\ a_i\in L_p(e_i).
 \end{cases}
\tag{1.5}
\]

Indeed, every \(p<q\) flag contains \(L_{q-1}\), while every \(p>q\)
flag is contained in \(L\). This proves the same-edge and upper-fixity
claims exactly.

Arbitrary old/conjugate choices retain the same set of central edges, so
lower saturation and owner injectivity are pointwise unchanged. This is
token-matching legality. It does not yet say that all chosen rows belong
to one factor; literal integrality is addressed in Section 4.

## 2. Exact lower cross-Gram

Put

\[
 (d_i^-)_p=
 \delta_{\sigma_iL_p(e_i)}-\delta_{L_p(e_i)}.
\tag{2.1}
\]

For \(p<q\), this vector is zero. For \(p\ge q\), every old target lies in
the common set \(L\), whereas every nonzero new target contains
\(b_i\notin L\). Thus for \(i\ne k\) both mixed equalities are impossible:

\[
 \sigma_iL_p(e_i)\ne L_p(e_k),\qquad
 L_p(e_i)\ne\sigma_kL_p(e_k).
\tag{2.2}
\]

If both innovations are nonzero, expansion gives

\[
 \left\langle(d_i^-)_p,(d_k^-)_p\right\rangle
 =
 \mathbf 1_{\{L_p(e_i)=L_p(e_k)\}}
 +
 \mathbf 1_{\{\sigma_iL_p(e_i)=\sigma_kL_p(e_k)\}}
 \ge0.
\tag{2.3}
\]

If either innovation is zero, the inner product is zero. At the common
depth,

\[
 \left\langle(d_i^-)_q,(d_k^-)_q\right\rangle
 =
 1+\mathbf 1_{\{\sigma_iL=\sigma_kL\}}
 \ge1.
\tag{2.4}
\]

For arbitrary finite nonnegative signed-depth weights, define

\[
 \mathfrak A=
 \left\|\sum_{i=1}^td_i^-\right\|_w^2,\qquad
 \mathfrak V=\sum_{i=1}^t\|d_i^-\|_w^2.
\]

Then

\[
 \boxed{
 \mathfrak A-\mathfrak V
 =2\sum_{i<k}\langle d_i^-,d_k^-\rangle_w
 \ge w_q^-t(t-1).}
\tag{2.5}
\]

Every factor of two in (2.5) is exact.

## 3. Haar and factorial-floor constants

Let \(f^0\) be the all-old profile and
\(f^1=f^0+\sum_i d_i^-\) the all-conjugated profile. A fair independent
corner has

\[
 f^\varepsilon=
 \frac{f^0+f^1}{2}
 +\frac12\sum_i\varepsilon_i d_i^-,
 \qquad \varepsilon_i\in\{-1,1\}.
\tag{3.1}
\]

Therefore

\[
 \mathbb E\|f^\varepsilon\|_w^2
 =
 \left\|\frac{f^0+f^1}{2}\right\|_w^2
 +\frac14\mathfrak V,
\tag{3.2}
\]

while

\[
 \frac{\|f^0\|_w^2+\|f^1\|_w^2}{2}
 =
 \left\|\frac{f^0+f^1}{2}\right\|_w^2
 +\frac14\mathfrak A.
\tag{3.3}
\]

All corners have equal mass at every rank. Hence the average coherent
endpoint squared norm exceeds the expected corner squared norm by

\[
 \boxed{
 \frac14(\mathfrak A-\mathfrak V)
 \ge\frac14w_q^-t(t-1).}
\tag{3.4}
\]

For the ordinary factorial-floor excess

\[
 \Phi(f)=\sum_T\binom{f(T)}2,
\]

fixed mass gives

\[
 \Phi(f)=\frac12\|f\|_2^2-\frac12\sum_Tf(T).
\]

Thus the undoubled floor descent is

\[
 \boxed{
 \frac18(\mathfrak A-\mathfrak V)
 \ge\frac18w_q^-t(t-1).}
\tag{3.5}
\]

The \(1/4\) statement in the source is correct only when its energy is
explicitly the doubled polynomial \(2\Phi\), or the squared norm with the
fixed linear baseline removed.

The descent is relative to the average of the two coherent endpoints.
Equivalently, some integral corner lies the displayed amount below the
higher endpoint. No monotone descent from an arbitrarily prescribed
endpoint is proved.

## 4. Literal one-word construction and exact run ledger

The switch is not internal to the original \(F_A\): in general
\(\sigma_iF_A\ne F_A\). After choosing a corner, label every occurrence by
the exact row from which its flags are taken and split the selected owner
sequence into maximal consecutive runs inside those labelled rows.

Removing one switched occurrence from its old row increases the old-row
run count by at most one. Its occurrence in the conjugate row creates at
most one new run. Therefore

\[
 \boxed{J_\varepsilon\le J_0+2t.}
\tag{4.1}
\]

Each resulting run is integral inside one exact factor. The audited
two-sided row literalizer writes a run of \(s\) principal owners in exact
length

\[
 s+2H.
\tag{4.2}
\]

If the corner has \(M\) principal owner occurrences, concatenating its
\(J_\varepsilon\) run words gives one literal word of exact length

\[
 \boxed{M+2HJ_\varepsilon
 \le M+2HJ_0+4Ht.}
\tag{4.3}
\]

After full owner completion one takes \(M=W\), with the isolated-owner runs
already included in \(J_0\). Thus there is no second \(W\)-term. The
constant-one consequence from this crude ledger requires

\[
 t=o(W/H)
\tag{4.4}
\]

for the total activated occurrence count, unless a stronger packet
aggregation is proved. This is a post-selection literalization of each
corner, not one universal word containing every cube corner.

### Proposition 4.1 (sharp same-row no-coalescence for distinguished spikes)

For two consecutive starts \(i,i+1\) in one source row, their
\(q\)-distinguished transpositions can never be equal. If \(2m-1\ge5\),
the two conjugated cyclic rows are also distinct even up to rotation.

#### Proof

In the source row notation,

\[
 b_i=x_{i+q-2},\qquad b_{i+1}=x_{i+q-1}.
\]

If \((a_i\ b_i)=(a_{i+1}\ b_{i+1})\), the distinct boundary coordinates
force

\[
 a_i=b_{i+1},\qquad a_{i+1}=b_i.
\]

The first equality is admissible, but the second is not:
\(b_i\notin L_q(i+1)\), whereas \(a_{i+1}\in L_q(i+1)\).

If the two conjugated cyclic rows agreed up to a nonzero rotation, the
product of the two transpositions would be that rotation on the
\((2m-1)\)-cycle. A product of two transpositions moves at most four
coordinates, while every nontrivial cyclic rotation moves all
\(2m-1\ge5\) coordinates. Zero rotation would make the transpositions
equal, already excluded. \(\square\)

Thus the crude singleton behavior cannot be repaired merely by assigning
one constant conjugation to consecutive distinguished spikes in the same
row. A successful compression theorem must use larger permutations,
nonconsecutive/cross-row coalescence, or a different literal mechanism.

### Proposition 4.2 (endpoint-collar rigidity of constant conjugations)

Let \(i=a,\ldots,b\) be \(t=b-a+1\) consecutive starts in one source row,
and let \(\sigma\) be one coordinate permutation which fixes every root
\(S_i\) in the interval setwise. Assume \(2\le H\le m-1\).

- If \(t\le m-2\), then

  \[
  \sigma L_q(e_i)=L_q(e_i)
  \qquad
  (1\le q\le H,\ a\le i\le b-q+1).
  \tag{4.5}
  \]

  Thus the depth-\(q\) flag can change at no more than \(q-1\) terminal
  owners, and the full depth-\(\le H\) truncated chain at no more than
  \(H-1\) terminal owners.

- If \(t\ge m-1\), every lower flag at every owner of the interval is
  fixed.

#### Proof

Use the row coordinates

\[
 S_i=I_\pi(i,m-1),\qquad
 L_q(e_i)=I_\pi(i+q-1,m-q)
 =S_i\setminus\{x_i,\ldots,x_{i+q-2}\}.
\tag{4.6}
\]

First suppose \(t\le m-2\), and linearize the cyclic interval. The common
intersection of the roots is

\[
 C=\{x_b,\ldots,x_{a+m-2}\}.
\]

For every left-boundary coordinate \(x_j\), \(a\le j<b\), its membership
pattern across \(S_a,\ldots,S_b\) is the distinct initial segment
\(\{i:i\le j\}\). Therefore any permutation stabilizing every \(S_i\)
must fix each such \(x_j\) individually. If \(i\le b-q+1\), all deleted coordinates
\(x_i,\ldots,x_{i+q-2}\) lie in this left boundary and are fixed
pointwise. Since \(S_i\) is fixed setwise, (4.6) is fixed setwise. This
proves (4.5).

If \(t=m-1\), the common intersection has size one, every left- and
right-boundary coordinate has a unique nonzero membership pattern, and hence
every coordinate belonging to any selected root is fixed pointwise.
For \(t>m-1\), every token lies in some subinterval of \(m-1\) consecutive
starts, to which the preceding argument applies. Thus all its lower flags
are fixed. \(\square\)

The root-stabilizing hypothesis is essential; merely fixing the upper
flags does not force this conclusion. The threshold \(t=m-1\) is sharp:
when \(t\le m-2\), the common all-one membership class has size
\(m-t\ge2\), and the swap \((x_b\ x_{b+1})\) fixes every selected root but
changes \(L_2(e_b)=S_b\setminus\{x_b\}\).

Consequently, if a rematching is represented by \(C\) root-stabilizing
constant-conjugation row runs, at most

\[
 \boxed{(H-1)C}
\tag{4.7}
\]

depth-\(\le H\) truncated token chains can differ from the base flags. In
particular an \(o(W/H)\)-run construction of this type changes only
\(o(W)\) truncated token chains. If depth \(q\ge2\) has \(M_q\) distinct
missing base targets which the new profile covers, then at least \(M_q\)
depth-\(q\) occurrences must change, and

\[
 \boxed{C\ge\frac{M_q}{q-1}.}
\tag{4.8}
\]

This closes the naive compression route: the balanced flow of Theorem 5.1
can be compressed into \(o(W/H)\) constant-conjugation runs only if it is
already \(o(W)\)-close to the base chain system. A successful pervasive
rematching must allow stateful changes of conjugation inside a run, share
literal seams across different conjugate rows, or prove the required
closeness.

## 5. Same-edge product with the upper owner-fixed spike

For the source upper-spike construction in this subsection assume
\(H\le m-2\), the exact range needed for its helper coordinate outside
\(U_H(e_i)\cup A\). (The lower spike alone remains valid through
\(H=m-1\), and Theorem 5.2 below recovers arbitrary upper rematching
through \(H=m-1\) by a different permutation.) For an upper spike on the
same token, let \(\theta_i\) exchange the omitted
pair \(A\) with

\[
 B_i^+=\{b_i^+,z_i\}\subseteq[n]\setminus Y_i,
\tag{5.1}
\]

where \(b_i^+\) is the entering upper coordinate and
\(z_i\notin U_H(e_i)\). Its support is disjoint from \(Y_i\). In contrast,

\[
 \operatorname{supp}(\sigma_i)\subseteq S_i\subseteq Y_i.
\tag{5.2}
\]

Hence \(\sigma_i\theta_i=\theta_i\sigma_i\). The four occurrences in

\[
 F_A,\qquad \sigma_iF_A,\qquad
 \theta_iF_A,\qquad \theta_i\sigma_iF_A
\tag{5.3}
\]

all have the same central edge. Moreover

\[
 L_p(\theta_i^\alpha\sigma_i^\beta e_i)
 =\sigma_i^\beta L_p(e_i),\qquad
 U_p(\theta_i^\alpha\sigma_i^\beta e_i)
 =\theta_i^\alpha U_p(e_i)
\tag{5.4}
\]

for \(\alpha,\beta\in\{0,1\}\). Thus the lower bit changes only lower
flags, the upper bit changes only upper flags, and the two innovations are
orthogonal.

This commutation is occurrencewise. It does not assert that the
permutations attached to different owners commute, nor that one global
conjugating permutation works for all owners.

Arbitrary products over occurrences retain the same central matching.
After a final corner is selected, every changed token is placed in one of
the three conjugate row types, so the same proof gives

\[
 J_\varepsilon\le J_0+2t,
\tag{5.5}
\]

not \(J_0+4t\). This is an exact post-selection one-word upper/lower
product theorem with the run ledger (5.5). It is not a common-factor
assertion.

### Theorem 5.1 (arbitrary-chain rematching and token-core balance)

For every selected central token \(e=(S,Y)\), every prescribed nested
lower chain

\[
 S=\Lambda_1(e)\supset\Lambda_2(e)\supset\cdots
 \supset\Lambda_H(e),
 \qquad |\Lambda_q(e)|=m-q,
\tag{5.6}
\]

is realized by a permutation \(\sigma_e\in\operatorname{Sym}(S)\). This
permutation fixes the central edge and every upper flag.

Moreover, put

\[
 N_q=\binom{n}{m-q},\qquad 1\le q\le H.
\tag{5.7}
\]

There is a simultaneous choice of one chain (5.6) for every one of the
\(N_1\) rank-\((m-1)\) roots such that every rank-\((m-q)\) target \(T\)
has token-core load

\[
 \boxed{
 \lambda_q(T)\in
 \left\{
 \left\lfloor\frac{N_1}{N_q}\right\rfloor,
 \left\lceil\frac{N_1}{N_q}\right\rceil
 \right\}}
\tag{5.8}
\]

simultaneously for all \(1\le q\le H\).

#### Proof

The old lower chain is obtained by deleting an ordered list of distinct
coordinates of \(S\). The prescribed chain (5.6) gives another such
ordered list. A permutation of \(S\) maps the old list to the prescribed
one. Extended by the identity outside \(S\), it fixes \(S\), \(Y\), the
omitted pair, and every upper flag, since every upper flag contains all of
\(S\).

For simultaneous balance, use the downward Boolean inclusion network from
rank \(m-1\) to rank \(m-H\). Give every rank-\((m-1)\) source supply one.
At every rank-\((m-q)\) node impose the integer throughput bounds in
(5.8), using a split node and a capacitated internal arc.

Explicitly, attach a super-source to every rank-\((m-1)\) split node by an
arc fixed at one; give every downward inclusion arc capacity \(N_1\); and
attach the bottom split nodes to a sink of demand \(N_1\). At rank \(r\),
put

\[
 \alpha_r=\frac{N_1}{\binom nr}.
\]

The symmetric fractional deletion flow gives every \(r\)-set throughput
\(\alpha_r\) and sends \(\alpha_r/r\) along each of its \(r\) downward
arcs. A fixed \((r-1)\)-set has \(n-r+1\) immediate supersets, and

\[
 \frac{n-r+1}{r}\alpha_r=\alpha_{r-1},
\]

so conservation holds at every layer. The split-arc bounds contain these
fractional throughputs.

After the standard lower-bound reduction, this is a directed network with
integral capacities and demands. Its incidence matrix is totally
unimodular, so fractional feasibility implies an integral flow. Since
every source has supply one, unit path decomposition assigns exactly one
nested deletion path to each source, proving (5.8). \(\square\)

Writing

\[
 N_1=N_qc_q+s_q,\qquad 0\le s_q<N_q,
\tag{5.9}
\]

the token-core ordinary factorial floor at rank \(m-q\) is therefore the
exact minimum

\[
 \boxed{
 N_q\binom{c_q}{2}+s_qc_q.}
\tag{5.10}
\]

This is a same-central-matching algebraic solution of every lower
token-core floor mode through \(H\); no second principal \(W\)-word is
needed. It does not solve chronology. The permutations \(\sigma_e\) may
vary for all \(N_1=\Theta(W)\) tokens and the direct row splitting can
have \(\Theta(W)\) runs.

It balances mass \(N_1\), not the completed mass \(W\) exactly. The
completion nevertheless has an unconditional \(o(W)\) weighted-spill
bound in the Gaussian window. Put

\[
 d=W-N_1=\frac{2W}{m+2},
\]

and append any nested lower flag to each of the \(d\) unused owners. Let
\(a_q\) be the balanced core load from (5.8), let \(e_q\) be the added
load of total mass \(d\), and let \(O_q\) be overload above the nearest
balanced full-\(W\) quota. For fixed \(A\) and \(H\le A\sqrt m\), one has
\(d<N_q\) for all sufficiently large \(m\). A balanced full-\(W\) quota
\(b_q\) can then be chosen with \(b_q\ge a_q\) coordinatewise: if its
floor is one larger than the core floor this is automatic; if the floors
agree, enlarge the core high set by exactly \(d\) coordinates. Hence

\[
 O_q\le\sum_Te_q(T)=d
\]

and, for \(c_q=\lfloor W/N_q\rfloor\ge1\),

\[
 \boxed{
 \sum_{q=1}^H\frac{O_q}{c_q}
 \le d\sum_{q=1}^H\frac1{c_q}
 \le dH=O_A(W/\sqrt m)=o(W).}
\tag{5.11}
\]

Writing the \(d\) completion owners as isolated radius-\(H\) runs costs
exactly \(2Hd=o(W)\) extra letters beyond their \(d\) principal positions.
Thus full-owner abstract weighted spill and completion chronology are
already negligible. The unresolved literal gate is compression of the
\(N_1\) core permutations into \(o(W/H)\) typed row runs.

### Theorem 5.2 (arbitrary upper-chain rematching and exact full-owner balance)

Assume \(1\le H\le m-1\), and complete the principal middle layer so that every
owner \(Y\in\binom{[n]}m\) occurs exactly once. For every owner and every
prescribed nested upper chain

\[
 Y=\Upsilon_0(Y)\subset\Upsilon_1(Y)\subset\cdots
 \subset\Upsilon_H(Y),
 \qquad |\Upsilon_q(Y)|=m+q,
\tag{5.12}
\]

there is a coordinate permutation \(\tau_Y\), supported in
\([n]\setminus Y\), whose conjugate row realizes this chain while fixing
the owner, its central lower root when present, and every lower flag.

The chains can be chosen simultaneously so that every rank-\((m+q)\)
target has load

\[
 \boxed{
 \lambda_q^+(T)\in
 \left\{
 \left\lfloor\frac{W}{N_q^+}\right\rfloor,
 \left\lceil\frac{W}{N_q^+}\right\rceil
 \right\},
 \qquad
 N_q^+=\binom{n}{m+q}.}
\tag{5.13}
\]

Thus every upper factorial-floor mode through \(H\) is minimized exactly
on the same completed principal owner set.

#### Proof

For a token row with omitted pair \(A\), the old upper chain adds an
ordered list of coordinates from \([n]\setminus(Y\cup A)\). The desired
chain (5.12) adds another ordered list of \(H\) coordinates outside \(Y\).
Because

\[
 |[n]\setminus\Upsilon_H(Y)|=m+1-H\ge2,
\]

choose a two-set \(B_Y\) outside \(\Upsilon_H(Y)\). A permutation of
\([n]\setminus Y\) can map the old entering list to the desired list and
map \(A\) to \(B_Y\); extend it arbitrarily on the remaining coordinates.
The conjugate factor is exact on \([n]\setminus B_Y\). The permutation is
the identity on \(Y\), so it fixes the central edge and all lower flags.
For a completion owner, first choose any omitted pair outside it and a
labelled exact row containing it; the same construction applies.

For balance, use the upward Boolean inclusion network from rank \(m\) to
rank \(m+H\), with one unit supplied at every rank-\(m\) owner and split
node bounds (5.13). The symmetric fractional flow has throughput

\[
 \beta_r=\frac{W}{\binom nr}
\]

at every \(r\)-set and sends \(\beta_r/(n-r)\) along each upward edge.
Every \((r+1)\)-set receives

\[
 \frac{r+1}{n-r}\beta_r=\beta_{r+1}.
\]

The same integral lower-bounded network theorem and unit path
decomposition used in Theorem 5.1 produce one balanced upper chain per
owner. \(\square\)

Write

\[
 W=N_q^+c_q^++s_q^+,\qquad 0\le s_q^+<N_q^+.
\]

The exact ordinary upper collision floor is

\[
 \boxed{
 N_q^+\binom{c_q^+}{2}+s_q^+c_q^+.}
\tag{5.14}
\]

The upper permutations \(\tau_Y\) are supported outside \(Y\), whereas
the lower rematching permutations \(\sigma_S\) are supported inside
\(S\subset Y\). They commute at each occurrence. Hence Theorems 5.1--5.2
give a same-central-edge algebraic product in which:

- all upper ranks are exactly floor/ceiling balanced;
- the \(N_1\)-token lower core is exactly floor/ceiling balanced;
- the \(d\)-owner lower completion contributes weighted spill \(o(W)\);
- there is exactly one principal occurrence per completed middle owner.

There is only one principal occurrence per completed middle owner; no
second principal \(W\)-family is introduced. This closes the algebraic
signed-balance gate, but not simultaneous literal chronology: the pair
\((\sigma_S,\tau_Y)\) may vary at \(\Theta(W)\) owners, producing
\(\Theta(W)\) typed row runs.

### Theorem 5.3 (exact stateful lower-compression gate)

Let \(v\to w\) be a consecutive central-owner edge with

\[
 L_1(v)=v\cap w.
\]

Put \(L_0(v)=v\) and

\[
 \{\ell_h(v)\}=L_h(v)\setminus L_{h+1}(v),
 \qquad 0\le h<H.
\]

Appending only the next deepest mask \(L_H(w)\) updates the complete
useful lower prefix at \(v\) to that at \(w\) if and only if

\[
 \ell_h(v)=\ell_{h-1}(w)
 \qquad(1\le h<H)
\tag{5.15}
\]

and

\[
 L_H(v)\setminus L_H(w)=\{\ell_{H-1}(w)\}.
\tag{5.16}
\]

Equivalently,

\[
 L_{h+1}(v)=L_h(v)\cap L_h(w)
 \qquad(0\le h<H),
\tag{5.17}
\]

with \(L_H(v)\ne L_H(w)\).

#### Proof

The useful ordered partition at \(v\) is

\[
 \bigl(
 L_H(v),\{\ell_{H-1}(v)\},\ldots,\{\ell_0(v)\}
 \bigr).
\]

Move-to-front by \(L_H(w)\) prepends that set and retains, in order, the
nonempty differences of the old blocks. The target prefix requires
exactly \(H\) singleton blocks before the unresolved tail. Matching those
blocks gives (5.15)--(5.16), and taking prefix unions gives the equivalent
form (5.17). \(\square\)

Now assume explicitly that a vertex-disjoint central path cover contains
exactly the \(N_1=W-d\) token-core owners, and that every oriented edge
\(v\to w\) has \(L_1(v)=v\cap w\). Let the remaining \(d\) completion
owners carry full radius-\(H\) lower flags and be initialized separately.
Call a core edge failing the preceding test bad. If the core path cover
has \(C_0\) paths and \(K^-\) bad internal edges, cutting the bad edges
gives

\[
 C^-=C_0+K^-
\]

exact lower-prefix runs. A run of \(s\) owners costs exactly \(s+H\), so
including the \(d\) separately initialized completion flags gives

\[
 \boxed{
 L_{\rm lower}=W+H(C^-+d).}
\tag{5.18}
\]

If the completion owners are required only at the middle rank and carry
no lower flags, the corresponding exact length is instead \(W+HC^-\).
Thus the \(W\)-baseline in (5.18) depends on the explicit full-owner
hypotheses just stated; it is not a formula for an arbitrary unspecified
path cover.

Thus the precise direct lower theorem still missing after Theorem 5.1 is:
choose a floor/ceiling-balanced integral Boolean flow whose induced chains
have

\[
 \boxed{C^-+d=o(W/H).}
\tag{5.19}
\]

This is a stateful optimization inside the integral balanced-flow
polytope. Proposition 4.2 rules out only the simpler piecewise
constant-conjugation realization; it does not rule out (5.15)--(5.19).

The lower word above does not automatically expose the arbitrary balanced
upper chains from Theorem 5.2. Assuming the lower transition criterion is
already satisfied, the exact additional compatibility test is as follows.
Put

\[
 R_q(v)=[n]\setminus\Upsilon_q(v),\qquad
 \{u_h(v)\}=R_h(v)\setminus R_{h+1}(v).
\]

On the same oriented edge \(v\to w\), write
\(\{p\}=v\setminus w\) and \(\{x\}=w\setminus v\). The same one-mask
update exposes the upper chain at \(w\) if and only if

\[
 u_0(w)=p,\qquad
 u_h(w)=u_{h-1}(v)\quad(1\le h<H),
\tag{5.20}
\]
or, equivalently,

\[
 R_{h+1}(w)=R_h(v)\cap R_h(w)
 \quad(0\le h<H).
\tag{5.21}
\]

The exact deepest-endpoint restitution identity is

\[
 \boxed{
 R_H(w)
 =\bigl(R_H(v)\cup\{u_{H-1}(v)\}\bigr)\setminus\{x\}.}
\tag{5.22}
\]

Indeed, after the new lower prefix has been matched, the old departing
coordinate \(p\) is the next surviving block and hence must be
\(u_0(w)\). The old blocks
\(u_0(v),\ldots,u_{H-2}(v)\) then shift one place to become
\(u_1(w),\ldots,u_{H-1}(w)\). The last old upper block remains in the
tail unless it is \(x\), in which case the newly appended lower core
swallows it. This proves (5.20)--(5.22). In particular,
\(R_H(w)=R_H(v)\) is fully legal exactly when
\(x=u_{H-1}(v)\); imposing deepest-endpoint non-equality would wrongly
exclude this case. Notice that the upper recurrence is reverse-shifted
relative to the lower recurrence; reversing \(v,w\) here is an error.
No condition that the unresolved residual tail remain one unfragmented
state block is used or needed for literal exposure of the band flags.

For any assigned lower and upper chains, if \(K^\pm\) core edges fail at
least one of (5.15)--(5.16) and (5.20)--(5.21), and
\(C^\pm=C_0+K^\pm\), cutting those edges and initializing each resulting
two-sided useful state gives the exact constructed word length

\[
 \boxed{
 L_{\rm band}=W+2H(C^\pm+d).}
\tag{5.23}
\]

Consequently a sufficient and exact final direct constant-one gate is to
choose the downward and upward balanced flows jointly so that

\[
 \boxed{C^\pm+d=o(W/H).}
\tag{5.24}
\]

The separate flow theorems do not prove (5.24): they give balanced
marginals but no control of their common good-edge set. Thus all algebraic
marginal balance, spill, ownership, and one-principal-occurrence
requirements are discharged before this criterion, while simultaneous
two-sided literal chronology is precisely what remains conditional.

## 6. Exact lower-rank span test

Fix the central matching and its old flags. Put \(r=m-q\) and define

\[
 \mathcal B_q(L)=
 \left\{
 b\notin L:
 \exists e\text{ with }L_q(e)=L,\ 
 L_{q-1}(e)\setminus L=\{b\}
 \right\}.
\tag{6.1}
\]

Let \(\Gamma_q^-\) be the undirected graph on
\(\binom{[n]}r\) whose edges are

\[
 L\;--\;L-\{a\}+\{b\},
 \qquad b\in\mathcal B_q(L),\quad a\in L.
\tag{6.2}
\]

### Theorem 6.1 (predecessor-graph criterion)

The rank-\((m-q)\) projections of all \(q\)-distinguished lower spike
columns span exactly

\[
 \boxed{
 \left\{
 x\in\mathbb R^{\binom{[n]}r}:
 \sum_{T\in C}x_T=0
 \text{ for every connected component }C\text{ of }\Gamma_q^-
 \right\}.}
\tag{6.3}
\]

They span the full centered rank-\((m-q)\) space if and only if
\(\Gamma_q^-\) is connected.

#### Proof

The available distinguished-depth columns are exactly

\[
 \delta_{L-a+b}-\delta_L
\]

for the edges in (6.2). Edge-incidence vectors of a connected graph span
its zero-sum subspace, for example along a spanning tree. Different
components have disjoint support. This proves (6.3). \(\square\)

A useful sufficient condition is the following pivot property: there is a
coordinate \(z\) such that

\[
 z\in\mathcal B_q(L)
 \qquad\text{for every }L\not\ni z.
\tag{6.4}
\]

Then every vertex not containing \(z\) is adjacent to \(z\)-containing
vertices, and the \(z\)-containing vertices are connected by two-edge
paths corresponding to their Johnson adjacencies. Hence \(\Gamma_q^-\) is
connected.

Neither exact central saturation nor nonempty \(\mathcal B_q(L)\) proves
(6.4) or connectivity. This is the new directly testable
edge-distribution gate.

There is one triangular scope point. A \(q\)-spike is zero at all depths
\(p<q\). Thus connectivity of \(\Gamma_q^-\) for every \(2\le q\le H\)
is sufficient for triangular linear spanning of the lower band. If one
\(\Gamma_q^-\) is disconnected, that obstructs the \(q\)-and-deeper
subatlas, but shallower distinguished spikes can have tails at depth \(q\)
and might bridge its components. Disconnectedness of one graph alone is
therefore not a no-go for the full enlarged atlas.

There is an exact full-projection graph which includes all such tails.
For a token \(e\), put

\[
 \{b_s(e)\}=L_{s-1}(e)\setminus L_s(e),
 \qquad 2\le s\le q,
\]

and define

\[
 \widehat{\mathcal B}_q(L)=
 \left\{
 b_s(e):
 L_q(e)=L,\ 2\le s\le q
 \right\}.
\tag{6.5}
\]

Let \(\widehat\Gamma_q^-\) have the same vertex set as \(\Gamma_q^-\)
and all edges

\[
 L\;--\;L-\{a\}+\{b\},
 \qquad
 b\in\widehat{\mathcal B}_q(L),\quad a\in L.
\tag{6.6}
\]

### Theorem 6.2 (full lower-spike projection and floor walls)

The formal menu span of the rank-\((m-q)\) projections of all legal lower
owner-fixed spike columns, allowing distinguished depths
\(2\le s\le q\), is exactly the edge-incidence span of
\(\widehat\Gamma_q^-\). Hence this menu span is the full centered
rank-\((m-q)\) space if and only if
\(\widehat\Gamma_q^-\) is connected.

More generally, if \(C\) is a connected component of size \(n_C\), its
total load \(M_C\) is invariant. Write

\[
 M_C=n_Cc_C+s_C,\qquad 0\le s_C<n_C.
\tag{6.7}
\]

Among nonnegative integral profiles with that component mass, the exact
minimum ordinary collision floor is

\[
 \boxed{
 n_C\binom{c_C}{2}+s_Cc_C.}
\tag{6.8}
\]

#### Proof

An \(s\)-distinguished spike on \(e\) uses
\(\sigma=(a\ b_s(e))\). At depth \(q\), its innovation is zero when
\(a\notin L_q(e)\), and is

\[
 \delta_{L_q(e)-a+b_s(e)}-\delta_{L_q(e)}
\]

when \(a\in L_q(e)\). Every \(a\in L_q(e)\) is admissible because
\(L_q(e)\subseteq L_s(e)\). This proves that the projected columns are
exactly the edges (6.6), and the incidence-span argument from Theorem 6.1
applies.

For the floor statement, discrete convexity minimizes
\(\sum_{T\in C}\binom{\mu(T)}2\) by assigning load \(c_C+1\) to exactly
\(s_C\) vertices and load \(c_C\) to the other \(n_C-s_C\). Substitution
gives (6.8). \(\square\)

Thus disconnectedness of \(\widehat\Gamma_q^-\), unlike disconnectedness
of the smaller \(\Gamma_q^-\), is a definitive projected obstruction for
the complete lower owner-fixed-spike menu. Connectivity remains unproved.
This is a linear/menu theorem. Transpositions at several depths on the
same token compose nonlinearly, so no simultaneous product cube containing
all menu columns is asserted; chartwise Haar identities, and products on
disjoint token supports, remain exact.

### Theorem 6.3 (sharp central-saturation connectivity ranges)

Assume every rank-\((m-1)\) root occurs once in the central matching.

1. At \(q=2\), the distinguished graph \(\Gamma_2^-\) is connected.
   Hence the direct lower spikes span the full centered rank-\((m-2)\)
   target space.

2. For every

   \[
   3\le q\le m-2,
   \tag{6.9}
   \]

   central saturation, owner injectivity, and tokenwise literal
   integrality do not force \(\widehat\Gamma_q^-\) to be connected. There
   is an exact such token system for which one prescribed
   rank-\((m-q)\) target is isolated.

3. For \(m\ge3\), at \(q=m-1\), the full-projection graph
   \(\widehat\Gamma_{m-1}^-\) is again automatically connected, although
   for \(m\ge4\) the smaller distinguished graph
   \(\Gamma_{m-1}^-\) need not be.

#### Proof

For \(q=2\), let \(S\) be a rank-\((m-1)\) root and write its selected
depth-two flag as

\[
 f(S)=S\setminus\{b(S)\}.
\]

Choosing any \(a\in f(S)\) gives the spike edge

\[
 f(S)\;--\;S\setminus\{a\}.
\]

Thus the spike edges contain a spanning star on all rank-\((m-2)\)
children of every \(S\). Any two Johnson-adjacent rank-\((m-2)\) targets
\(L,L'\) have union \(S=L\cup L'\) of rank \(m-1\), and the star of that
root joins \(L\) to \(L'\) in at most two steps. The Johnson graph is
connected, proving part 1.

For part 2 put \(r=m-q\ge2\) and fix an \(r\)-set \(L_0\). For every
rank-\((m-1)\) root \(S\supset L_0\), the set \(S\setminus L_0\) has
size \(q-1\ge2\). Choose two coordinates of \(L_0\) and two coordinates
of \(S\setminus L_0\), and prescribe the depth-\(q\) flag

\[
 f(S)=(L_0-\{u,v\})\cup\{x,y\}.
\tag{6.10}
\]

Then \(d_J(f(S),L_0)=2\). For roots not containing \(L_0\), prescribe any
\(r\)-subset of the root. Order the \(q-1\) deletions from \(S\) so that
the prescribed \(f(S)\) is the final flag.

Every full-projection spike edge from the token rooted at \(S\) is a
Johnson edge incident with \(f(S)\). If such an edge ended at \(L_0\),
then \(S\) would contain \(L_0\) and \(d_J(f(S),L_0)=1\), contradicting
(6.10). Also \(L_0\) is never itself a selected depth-\(q\) flag. Hence it
is isolated in \(\widehat\Gamma_q^-\).

For full physicality, first choose an inclusion matching from all
rank-\((m-1)\) roots to distinct rank-\(m\) owners; Hall follows from the
biregular degrees \(m+2\) on the root side and \(m\) on the owner side.
For each matched edge choose an omitted pair outside its owner. A
coordinate relabeling of an exact local factor supplies a labelled cyclic
row whose central edge is the prescribed matched edge and whose next
\(q-1\) deletions realize the prescribed \(f(S)\). Taking these as
singleton literal row pieces gives an integral lower-saturating,
owner-simple token system. It has \(\Theta(W)\) runs, so it is an
obstruction to deductions from central legality alone, not an obstruction
to a stronger low-run correlated-factor theorem.

Finally take \(q=m-1\). A selected final flag is a singleton
\(f(S)\in S\). Across all distinguished depths \(2\le s\le m-1\), the
predecessors are exactly the other coordinates of \(S\). Hence the full
projection graph contains the complete star from \(f(S)\) to every other
singleton in \(S\). Any two coordinates lie together in some
rank-\((m-1)\) root, so these stars connect the singleton target layer.
The distinguished graph keeps only its last predecessor and need not have
this property. This proves part 3. \(\square\)

Thus the first genuinely missing connectivity estimate starts at depth
three and persists through \(q=m-2\). Any positive growing-band theorem
in that range must use cross-root structure of the correlated row system;
central saturation by itself is exactly enough at depth two, sharply
insufficient at intermediate depths, and enough again for the full
singleton projection at \(q=m-1\).

## 7. Integration with the long-interval dual and the span audit

The corrected boundary is:

1. The AD12 right-shifted first-contained chart remains a genuine
   \(W+o(W)\) long-interval lower chart with \(o(W/H)\) endpoints under
   \(H=o(m/\log^2m)\). It lives on the top owner layer and is a separate
   literal word from the bottom upper long chart.

2. The owner-fixed lower spike is a different construction on the bottom
   owner layer. It keeps each central edge and needs no second word, but
   its crude run cost is \(O(t)\) for \(t\) activated occurrences.

3. Therefore there is no general theorem that lower flags intrinsically
   require a second word. Arbitrary-chain rematching plus the integral
   flow theorem already balances the token core at every lower rank, and
   the \(d\)-owner completion has weighted spill \(o(W)\). The exact
   unresolved same-word gate is to compress those rematchings into
   \(o(W/H)\) stateful runs. Proposition 4.2 rules out naive
   constant-conjugation long packets unless only \(o(W)\) token chains
   need to change.

4. The fixed-pair orbit cokernel in AD12 remains correct for the
   pair-exchange upper-plus-right-shifted-lower menu. The new
   transpositions \((a_i\ b_i)\) need not fix the leftover coordinate
   \(\star\), so that cokernel does not apply to the enlarged direct-spike
   atlas. Indeed

   \[
   \left\langle
   \mathbf1_{\{\star\in\cdot\}}-\frac r{2m+1},
   \delta_{L-a+b}-\delta_L
   \right\rangle
   =
   \mathbf1_{\{b=\star\}}-\mathbf1_{\{a=\star\}}.
   \tag{7.1}
   \]

5. If the enlarged atlas consists of the fixed-partition upper charts and
   only the new lower spikes, the lower spikes fix every upper flag and do
   not alter the old upper-rank obstruction. If arbitrary owner-fixed
   upper spikes are also admitted, their occurrence-specific
   transpositions can move the old \(\star\)-mode. Theorem 5.2 goes
   further and exactly balances every upper rank by arbitrary
   outside-owner rematching, so the old fixed-partition cokernel is
   definitively not an obstruction for the full enlarged algebraic atlas.

The new result therefore corrects the earlier phrase “the remaining
positive theorem must fuse two central owner layers.” That statement is
true only for the particular right-shifted long-interval dual. It is false
as a general obstruction: owner-fixed spikes bypass the layer fusion
locally and literally.

## 8. Proved and unproved boundary

### Proved

1. Same-central-edge and exact token-matching legality.
2. Fixity of every upper flag and lower-only innovations.
3. Nonnegative lower cross-Gram and the exact factor in (2.5).
4. Squared/doubled-floor Haar constant \(1/4\), and ordinary factorial
   constant \(1/8\).
5. Exact run bound (4.1) and one-word length (4.3).
6. Exact commuting upper/lower four-state product.
7. Exact predecessor-graph span criterion.
8. Automatic full centered span at lower depth two.
9. A physical sharp obstruction showing that central legality alone does
   not force full-projection connectivity for \(3\le q\le m-2\).
10. Arbitrary-chain rematching and exact simultaneous token-core
    floor/ceiling balance through every lower depth.
11. \(o(W)\) weighted spill and literal collar cost for the \(d\)-owner
    completion in the Gaussian window.
12. Endpoint-collar rigidity and the lower bound (4.8) for
    constant-conjugation packet compression.
13. Arbitrary outside-owner upper rematching and exact simultaneous
    full-owner upper floor/ceiling balance, algebraically on the same
    principal owner set.
14. The exact stateful lower transition criterion and length ledger
    (5.15)--(5.19), under its explicit token-core path-cover hypothesis.
15. The exact upper-reverse compatibility criterion (5.20)--(5.22) and
    the conditional two-sided length ledger (5.23).

### Unproved

1. A joint choice of the balanced downward and upward flows with
   \(C^\pm+d=o(W/H)\); separate marginal balance does not imply this
   simultaneous two-sided chronology theorem.
2. A nonconstant-conjugation packet or shared-seam mechanism escaping
   Proposition 4.2.
3. Connectivity/frame estimates for the useful low-run spike menu, if the
   rounding route rather than direct balanced rematching is used.
4. A full signed-rank span/frame theorem for the enlarged upper-plus-lower
   owner-fixed atlas.
5. Constant one.
