# Two-parent flag-stabilizer orbit and the common-parent covariance no-go

Date: 2026-07-29

Status: proved.  Diagonal symmetries of one common parent cannot change the
collision covariance.  After the minimal relaxation to independently
relabelled A and B parents, an explicit flag-stabilizer orbit makes every B
half-signature label one-wise uniform on its exact compatibility fibre.
For k=15, at least \(25/42\) of the full flag torsor attached to any
duplicate-safe pointed edge pair is residence-safe.  Thus the collision gate
is automatic once an eligible parent Hamilton cycle exists; the saved
artifacts still do not supply that parent.

## 1. Why the common-parent symmetry orbit cannot work

Let F be a lower-q1-exact parent factor on rank r of an n=2r-1 element
ground set X.  Let D(F) be its duplicate-safe oriented square catalogue, and
assume C_dup(F)>0.  Let

\[
\Xi(F)=N_{11}+N_{12}+N_{21}
-\frac{
 \langle a_1,b_1\rangle+\langle a_1,b_2\rangle+
 \langle a_2,b_1\rangle}{C_{\rm dup}}.
\tag{1.1}
\]

### Proposition 1.1 (diagonal relabelling invariance)

For every coordinate permutation sigma,

\[
C_{\rm dup}(\sigma F)=C_{\rm dup}(F),\qquad
N_{ij}(\sigma F)=N_{ij}(F),\qquad
N_\times(\sigma F)=N_\times(F),\qquad
\Xi(\sigma F)=\Xi(F).
\tag{1.2}
\]

Cycle rotation and reversal also leave every quantity in (1.2) unchanged.
Consequently no orbit obtained by applying the same Boolean-lattice
automorphism to both shores can average Xi to zero unless Xi was zero
already.

#### Proof

The map s to sigma s is a bijection from D(F) to D(sigma F).  Lower and
upper colours, their multiplicities, the square identities, and the
endpoint paths are carried equivariantly.  Hence

\[
A_i(\sigma s)=\sigma A_i(s),\qquad
B_j(\sigma s)=\sigma B_j(s).
\]

Every equality event and the crossed event are therefore preserved.
The four marginal vectors are merely permuted in their coordinate entries,
so their three inner products are unchanged.  This proves (1.2).  Rotation
and reversal only reindex the same undirected cycle and its cut paths.
\(\square\)

Complement is not an escape from Proposition 1.1: on n=2r-1 it sends rank r
to rank r-1 and is not an endomorphism of J(n,r).  The incidence-dual
construction has different shadow and residence hypotheses.

Thus only a genuinely nonconjugate factor switch, or an independent action
on the second rail, can alter the pairing.

## 2. The exact two-parent one-rung ledger

Let F and G be Hamilton cycles in J(X,r).  Assume:

1. each lower-colour map is a bijection onto rank r-1;
2. each upper-colour support is the entire rank r+1 layer;
3. every cyclic positive run of F has length at least D;
4. every cyclic zero run of G has length at least D.

Full cyclic biresidence of both parents is more than enough.  For a
permutation pi of X, use F as the A rail and the complemented cycle pi G as
the B rail.

For an edge e of F and an endpoint P, put L=lambda_F(e).  For an edge f of
pi G and an endpoint S, put K=lambda_piG(f) and R=the complement of S.
Delete the A copy of e and the complementary-B copy of f, and add the rung
from A_P to B_R.

### Lemma 2.1 (two-parent one-rung criterion)

The result is a spanning Johnson Hamilton path with both q1 palettes and
positive residence through D-1 exactly when

\[
R=L,\qquad P=\bar K,                                      \tag{2.1}
\]

both deleted parent upper colours have multiplicity at least two in their
respective parent, and the unique new seam satisfies

\[
\alpha_x+\beta_x\in\{0\}\cup[D,\infty)\qquad(x\in X).     \tag{2.2}
\]

Here alpha is measured on F and beta on the complemented pi G path.

#### Proof

The two cut Hamilton cycles become two paths and the rung joins them.
The edge-colour ledger is

\[
\begin{array}{c|cc}
&\text{lower}&\text{upper}\\ \hline
A_e&\lambda_F(e)&\upsilon_F(e)\\
B_f&\{z\}\cup\overline{\upsilon_{\pi G}(f)}
   &\{z\}\cup\overline{\lambda_{\pi G}(f)}\\
\text{rung}&R&\{z\}\cup P.
\end{array}                                               \tag{2.3}
\]

The tight no-z lower and z-upper colours are restored exactly by (2.1).
The two remaining deleted colours have no possible rung replacement, so
their survival is exactly the repeated-upper condition.  All nonseam
positive runs on A are positive runs of F; those on B are complements of
zero runs of pi G.  The only new internally bounded run is the seam sum in
(2.2).  This proves necessity and sufficiency.  \(\square\)

The proof uses no equality between F and G.  Thus independent relabelling of
the B parent is literal, owner-exact, and q1-exact.

## 3. The flag-stabilizer orbit

Call a parent edge upper-safe when its upper colour has multiplicity at
least two.  Choose:

* an upper-safe edge e of F and one endpoint P;
* an upper-safe edge g of G and one endpoint Q.

Write

\[
\begin{aligned}
L&=\lambda_F(e), & P&=L\cup\{a\},&
K&=X\setminus P,\\
K_0&=\lambda_G(g), &Q&=K_0\cup\{a_0\},&
L_0&=X\setminus Q.
\end{aligned}                                             \tag{3.1}
\]

These are ordered partitions

\[
X=K\mathbin{\dot\cup}\{a\}\mathbin{\dot\cup}L
 =K_0\mathbin{\dot\cup}\{a_0\}\mathbin{\dot\cup}L_0,
\tag{3.2}
\]

with both K-parts and L-parts of size r-1.

Let Omega(e,P;g,Q) be the set of all coordinate permutations pi satisfying

\[
\pi K_0=K,\qquad \pi a_0=a,\qquad \pi L_0=L.              \tag{3.3}
\]

It is a torsor for

\[
S_K\times S_L
\]

and has size ((r-1)!)^2.  Every pi in this torsor makes the fixed pointed
edge pair an exact duplicate-safe square:

\[
\pi Q=K\cup\{a\}=\bar L,\qquad
\overline{\lambda_{\pi G}(\pi g)}=\bar K=P.              \tag{3.4}
\]

### Endpoint half-signatures

For 1<=i<=D-2, let x_i be the coordinate of positive terminal age i at
the pointed A endpoint, if it exists.  It lies in L.  For
1<=j<=D-2, let y_j be the coordinate of zero terminal age j at the pointed
G endpoint, if it exists.  It lies in L_0.

The x_i are distinct, and the y_j are distinct.  If v_0 is the other
extension used by g, then v_0 lies in L_0 and is not any y_j: across g it
is at the boundary of a cyclic G zero-run of length at least D.

Under uniform pi in Omega, the restriction pi:L_0 to L is a uniformly
random bijection.  Hence, for every nonnull pair,

\[
\Pr[\pi y_j=x_i\mid \pi\in\Omega]=\frac1{r-1}.            \tag{3.5}
\]

This is exact one-wise uniform re-pairing on the physical compatibility
fibre.

### Theorem 3.1 (pointed flag-stabilizer splice)

Put

\[
t_D=\#\{(i,j):i,j\ge1,\ i+j<D\}=\binom{D-1}{2}.           \tag{3.6}
\]

The proportion of pi in Omega for which the designated one-rung seam is
safe is at least

\[
1-\frac{t_D}{r-1}.                                       \tag{3.7}
\]

Therefore, whenever

\[
r-1>\binom{D-1}{2},                                      \tag{3.8}
\]

some independently relabelled B parent gives a valid one-rung splice.

#### Proof

The square normal form says that a seam failure is exactly an equality

\[
x_i=\pi y_j
\]

for some i+j<D.  Automatic boundary coordinates cannot create another
failure; in particular the other extension v_0 has B age at least D.
There are at most t_D such comparisons.  Equation (3.5) and the union
bound give (3.7).  Strict positivity in (3.8) gives a permutation with no
failure.  Lemma 2.1 then gives the full path.  \(\square\)

At D=4, let eta be the number of active comparisons among

\[
(1,1),(1,2),(2,1),
\]

and let zeta be one when all four age labels x_1,x_2,y_1,y_2 exist and
zero otherwise.  The exact safe proportion in the torsor is

\[
1-\frac{\eta}{r-1}+\frac{\zeta}{(r-1)(r-2)}.             \tag{3.9}
\]

Indeed the only overlap of collision events is the crossed assignment
pi y_2=x_1 and pi y_1=x_2.  Formula (3.9) recovers the exact collision
kernel inside the stabilizer orbit.

The worst D=4 profile has all three comparisons active and therefore also
has the crossed refund.  Its exact universal safe factor is

\[
\theta_r
=1-\frac3{r-1}+\frac1{(r-1)(r-2)}
=\frac{(r-3)^2}{(r-1)(r-2)}.                             \tag{3.9a}
\]

For k=15, r=8 and D=4, all three comparisons are active only when the
crossed refund is active as well.  Hence every pointed upper-safe pair has

\[
\Pr_{\pi\in\Omega}[\text{safe}]
\ge1-\frac37+\frac1{7\cdot6}=\frac{25}{42}.              \tag{3.10}
\]

This is an explicit existence theorem, not a heuristic.

### Corollary 3.2 (fixed-edge group orbit)

There is a genuine subgroup orbit on which the designated physical square,
not merely its flag type, stays fixed and every active half-signature
covariance is zero.

Let c_0 be the other extension of the pointed G edge, so its endpoints are
K_0+a_0 and K_0+c_0.  Choose

\[
v\in L\setminus\{x_1,\ldots,x_{D-2}\};
\]

at D=4 this excludes at most two coordinates.  Choose one pi_0 satisfying

\[
\pi_0K_0=K,\qquad \pi_0a_0=a,\qquad \pi_0c_0=v.
\tag{3.11}
\]

Let

\[
H=\operatorname{Sym}(L\setminus\{v\})
\]

be the coordinate subgroup fixing \(K\cup\{a,v\}\) pointwise.  It acts on
the B parent by \(h\pi_0G\).  Every orbit member contains the same pointed B edge

\[
\{K\cup\{a\},K\cup\{v\}\},
\]

so the square and both duplicate-slack tests persist.  Each short B label
lies in \(L\setminus\{v\}\) and is one-wise uniform there.  Consequently

\[
\mathbb E_{h\in H}
\left({\bf1}_{h\pi_0y_j=x_i}-\frac1{r-2}\right)=0.
\tag{3.12}
\]

More explicitly, regard the persistent square in each orbit member as one
row of an orbit table of size \(m_H=|H|\).  For active labels,

\[
a_i^{H}(x_i)=m_H,\qquad
b_j^{H}(x)=\frac{m_H}{r-2}\quad(x\in L\setminus\{v\}),
\]

and

\[
c_{ij}^{H}(x_i)=\frac{m_H}{r-2}
=\frac{\langle a_i^{H},b_j^{H}\rangle}{m_H}.             \tag{3.12a}
\]

Thus the aggregate covariance of the persistent-square orbit table is
exactly

\[
\Xi_H=0.                                                  \tag{3.12b}
\]

At D=4 the exact safe proportion is

\[
1-\frac{\eta}{r-2}+\frac{\zeta}{(r-2)(r-3)}.             \tag{3.13}
\]

For r=8 its worst value is attained when all three comparisons are active:

\[
1-\frac36+\frac1{6\cdot5}=\frac8{15}.                   \tag{3.14}
\]

Thus at least 384 of the 720 elements of this fixed-edge group orbit are
safe in the worst collision profile.

#### Proof

Condition (3.8) leaves a choice of v outside all nonnull A labels.
The three parts in (3.11) have the required sizes, so pi_0 exists.
Coordinate relabelling preserves every parent hypothesis.  Zero residence
at the pointed G cut gives \(y_j\ne c_0\) for all relevant j; therefore
pi_0 y_j lies in \(L\setminus\{v\}\), on which H acts uniformly.  This proves
(3.12).  Inclusion--exclusion for the three D=4 collision events gives
(3.13); substituting r=8 and the worst active profile gives (3.14).
\(\square\)

## 4. Global expectation

Let s_F and s_G be the numbers of upper-safe edges in F and G.  There are
2s_F and 2s_G upper-safe oriented edge incidences.  The symmetric group is
transitive on lower-extension flags (K_0,a_0); there are

\[
r\binom{n}{r-1}=rW
\]

such flags.  Thus, for uniform pi in S_X,

\[
\mathbb E C_{\rm dup}(\pi)=\frac{4s_Fs_G}{rW}.            \tag{4.1}
\]

There is also an exact pooled collision identity.  Put

\[
I_A=2s_F,\qquad I_B=2s_G.
\]

Let \(A_i^\star\) and \(B_j^\star\) count upper-safe oriented incidences
whose raw age-i or age-j label is nonnull, and let
\(A_{12}^\star,B_{12}^\star\) count incidences on which both low-age labels
are nonnull.  Summing over fixed ordered incidence pairs gives

\[
\mathbb E N_{ij}
=\frac{A_i^\star B_j^\star}{rW(r-1)}
\quad((i,j)=(1,1),(1,2),(2,1)),                          \tag{4.1a}
\]

\[
\mathbb E N_\times
=\frac{A_{12}^\star B_{12}^\star}{rW(r-1)(r-2)},         \tag{4.1b}
\]

and hence

\[
\mathbb E N_{\rm safe}
=\frac1{rW}\left[
 I_AI_B
 -\frac{A_1^\star B_1^\star+A_1^\star B_2^\star+
              A_2^\star B_1^\star}{r-1}
 +\frac{A_{12}^\star B_{12}^\star}{(r-1)(r-2)}
\right].                                                 \tag{4.1c}
\]

No independence between different square candidates is used in these
equalities.  Combining the same flag count with Theorem 3.1 gives

\[
\boxed{
\mathbb E N_{\rm safe}(\pi)\ge
\frac{4s_Fs_G}{rW}
\left(1-\frac{\binom{D-1}{2}}{r-1}\right).}              \tag{4.2}
\]

This proves expectation and existence simultaneously.

For an upper-complete Hamilton cycle, write

\[
M=\binom{n}{r+1},\qquad E=W-M.
\]

Every upper load is at most r: the r+1 facets of one upper set induce a
proper linear forest in the Hamilton cycle.  Therefore, if q upper colours
have load at least two,

\[
q\ge\left\lceil\frac{E}{r-1}\right\rceil,\qquad
s_F,s_G\ge E+\left\lceil\frac{E}{r-1}\right\rceil.        \tag{4.3}
\]

At k=15 this lower bound is 1635.  Using the sharp D=4 factor 25/42 from
(3.10), equations (4.1)-(4.2) sharpen to

\[
\mathbb E C_{\rm dup}\ge
\frac{10692900}{51480}>207,\qquad
\mathbb E N_{\rm safe}\ge
\frac{267322500}{2162160}>123.                           \tag{4.4}
\]

Hence some B-parent relabelling has at least 124 safe oriented one-rung
corners.  The pointed theorem is stronger for pure existence: it starts
from any one upper-safe edge on each parent and makes that specific pair
safe.

### Corollary 4.1

If one q1-exact, upper-complete, cyclically biresident Hamilton cycle F in
J(15,8) exists, then using F on the A rail and pi F on the B rail for a
suitable coordinate permutation pi produces a q1-complete, positively
resident one-rung Hamilton path in the k=16 middle layer.

Thus, after permitting independently relabelled rails, the collision
noncover condition is no longer an additional existence hypothesis.

### Corollary 4.2 (optional two-sided child seam)

If both parents are fully cyclically biresident and the child path is
required to have both positive and zero internal residence, the same
averaging still succeeds.  Conditional on an aligned pointed flag, the
positive seam comparisons use the uniform bijection \(L_0\to L\), while
the zero seam comparisons use the independent uniform bijection
\(K_0\to K\).  Hence at D=4

\[
\Pr[\text{both seam signs safe}\mid\text{alignment}]
\ge\theta_r^2.                                           \tag{4.5}
\]

At k15, the upper-completeness bound (4.3) therefore gives

\[
\mathbb E N_{\rm both-safe}>73.59,
\]

so some relative B relabelling has at least 74 two-sided-safe oriented
corners.

## 5. What happened to the old Xi

The orbit above has exact zero covariance after conditioning on the forced
square flag:

\[
\mathbb E_{\pi\in\Omega}
\left({\bf1}_{\pi y_j=x_i}-\frac1{r-1}\right)=0.          \tag{5.1}
\]

This is the correct fibre-centred covariance.  It is not the old global Xi
from (1.1).  The old statistic subtracts a product of whole-catalogue
marginals, while physical square compatibility first forces both labels
into the same (r-1)-set L.  Even ideal mixing therefore has collision
probability 1/(r-1), not 1/n.  The positive values of Xi in the saved
translation-equivariant audits partly record this geometric conditioning.
For an always-active slot with globally uniform marginals, the forced
structural offset is exactly

\[
\frac1{r-1}-\frac1{2r-1}
=\frac{r}{(r-1)(2r-1)}>0.                                \tag{5.2}
\]

Moreover, the torsor changes the rest of the candidate catalogue, so
C_dup and the four global profiles need not remain fixed.  Consequently a
claim that the old per-factor Xi averages to zero would be false or at
least unsupported.  Proposition 1.1 shows it is exactly false for every
diagonal common-parent symmetry orbit.

The theorem needed for existence is (3.7), not old-Xi cancellation.

## 6. Alternating circuits and the strict common-parent boundary

Let I be the bipartite inclusion graph between ranks r-1 and r.  A
lower-q1-exact Johnson 2-factor is equivalent to a spanning degree-two
subgraph H of I: the two selected middle neighbours of a lower owner L are
the endpoints of the Johnson edge with colour L.  Contracting the lower
vertices recovers the Johnson factor, and a Hamilton factor corresponds to
one cycle in H.

The symmetric difference of two such degree-two subgraphs is a union of
even alternating circuits.  Since I has no 4-cycle, the smallest
nontrivial move is an alternating C6.  It has the form

\[
L_a=K\cup\{a\},\quad L_b=K\cup\{b\},\quad L_c=K\cup\{c\},
\]

with middle vertices K+ab, K+bc, K+ca, and it toggles one incidence at
each of these six vertices.

Such a move preserves exact lower ownership and degree two, but it does not
automatically preserve:

* one physical component;
* every upper colour whose last provider may be deleted;
* either cyclic residence system;
* C_dup or the four endpoint-age marginals.

Conjugating one admissible circuit by an automorphism only produces
isomorphic factors and leaves Xi constant by Proposition 1.1.  A strict
common-parent Xi-mixing orbit therefore requires genuinely nonconjugate
alternating circuits with all four additional gates checked at every state.
No such orbit is presently proved.

For the positive two-parent construction, the endpoint factors G and pi G
are nevertheless connected algebraically by alternating circuits:
the symmetric difference of their two inclusion 2-factors decomposes into
an alternating-circuit packet.  The flag-stabilizer theorem applies that
packet simultaneously through the coordinate group action.  It makes no
claim that a sequence toggling the constituent circuits one at a time keeps
Hamiltonity, upper support, or residence.  Thus it is an
eligibility-preserving compound Markov endpoint action, not a proved legal
single-circuit trajectory.

## 7. Saved-artifact boundary

Coordinate relabelling preserves component lengths, upper-load
completeness, and both cyclic run-length multisets.  It therefore cannot
repair any saved near-parent:

* from3 remains two components and retains its 2010 short zero-runs;
* q1ham_d93 remains one component but retains 1050 short one-runs and 2070
  short zero-runs;
* seed0.dualresident.seed7 remains 26 components with 855 short one-runs;
* connected409 retains its missing upper-q1 colours and short zero-runs.

Thus Theorem 3.1 closes the endpoint-collision orbit condition
conditionally, but it does not manufacture the missing eligible parent.
The exact surviving gate is now:

> construct one lower-q1-exact, upper-complete, cyclically biresident
> Hamilton cycle in J(15,8), or construct two Hamilton parents with the
> corresponding one-sided residence conditions of Section 2.

The theorem concerns middle ownership, both q1 palettes, and positive
residence.  Deeper shadows and COMP_3 remain separate.
