# Lane K: PBBS \(q=1\) commutator rigidity and the seam-rich exact-factor gate

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
B=\operatorname{Cat}_m=\frac{W}{n}.
\]

There are two inequivalent meanings of “preserve the PBBS \(q=1\)
seed.” They have different answers.

1. **Owner-labelled preservation is impossible nontrivially.** For a
   spanning odd-graph \(2\)-factor \(F\), the \(q=1\) colour attached to
   each middle owner \(X\) determines the two \(F\)-neighbours of \(X\).
   Hence it determines \(F\) itself. A closed exact-factor commutator
   preserving this field owner by owner is the identity; equivariantly,
   one transported by a common permutation \(g\) is only \(gF\). It cannot
   change any unlabelled deeper-shadow objective.

2. **Unlabelled preservation has a precise surviving mechanism.** If only
   the \(q=1\) histogram is fixed, the changed owner colours form an
   Eulerian directed transport on the rank-\((m-1)\) colour set. Nontrivial
   deeper action is possible only by moving \(q=1\) colours around such
   cycles. Pointwise owner-fixed atoms cannot do this.

3. **There is an exact complement invariant.** For a cyclic-wreath trade,
   exact middle preservation fixes upper depth \(1\) automatically, and
   lower-\(q=1\) neutrality fixes upper depth \(2\). Thus a \(q=1\)-neutral
   exact-factor commutator cannot change the upper \(q=2\) shadow. Its first
   possible action is lower \(q=2\), paired by complementation with upper
   \(q=3\).

4. **Positive-density deeper action forces a seam-rich move.** If \(F,F'\)
   differ in \(e\) old factor edges, then for every \(q\ge1\)

   \[
   \|B_{m-q}(F'-F)\|_1\le4qe,
   \qquad
   \|B_{m+q}(F'-F)\|_1\le4(q-1)e.
   \tag{0.1}
   \]

   Therefore \(\delta W\) action at some \(q\le H\) forces

   \[
   e\ge\frac{\delta W}{4H}.
   \tag{0.2}
   \]

   If the commutator is supported on \(C\le B\) affected old wreath rows,
   the average affected row must contain at least

   \[
   \frac{\delta n}{4H}
   \tag{0.3}
   \]

   cut-edge seams; this is \((\delta/(2A)+o(1))\sqrt m\) for
   \(H=A\sqrt m\), and \(\delta n/8=\Theta(m)\) if the action is already at
   lower depth \(2\).

5. **The physical-component budget is not itself the obstruction.** Every
   exact factor has only \(B=W/n=o(W/H)\) wreath rows and can pay
   \(O(HB)=o(W)\) collars whenever \(H=o(n)\). The required
   \(\Omega(W/H)\) residual seams must therefore be resewn entry-neutrally
   inside those \(B\) rows. Initializing each residual path separately
   would cost \(\Omega(W)\).

No all-dimensional PBBS-derived family satisfying this seam-rich Eulerian
gate is constructed here. The result is instead a universal invariant which
closes the pointwise-seed interpretation and sharply localizes the weaker
unlabelled problem. The known AC2 six-for-six triangle shows that this
boundary is real at the support-feasible level: it preserves \(q=1\) by an
Eulerian three-cycle and changes lower \(q=2\), but even one common exact
completion is unproved. The vertex-disjoint clean PBBS \(C_8\) reservoir has
only Catalan-scale seam action and cannot by itself attain (0.2).

Here “positive-density deeper-shadow support” means \(\Omega(W)\) nonzero
target coordinates, or \(\Omega(W)\) \(\ell^1\)-action, at a controlled
depth. A positive density of the \(B\) wreath rows is a strictly weaker
notion: bounded local cells can rebundle \(\Theta(B)\) rows while changing
only \(O(B)=o(W)\) shadow coordinates.

## 1. Exact-factor and PBBS conventions

Let

\[
O_m=KG(2m+1,m).
\]

A cyclic wreath row gives an \(n\)-cycle in \(O_m\). An exact wreath factor
is a spanning \(2\)-factor all of whose components are such \(n\)-cycles;
it has exactly \(B\) rows. The canonical PBBS object is also a spanning
\(2\)-factor, and each of its components is point-regular and has length a
multiple of \(n\), but it need not be an exact wreath factor.

For a cyclic row \(C\), write \(B_r e_C\) for the incidence vector of its
cyclic \(r\)-intervals. For a signed row vector \(z\), \(B_rz\) is its
rank-\(r\) shadow increment. The lower and upper depth-\(q\) increments are

\[
B_{m-q}z,\qquad B_{m+q}z.
\]

The owner-labelled field introduced below is stronger than the histogram
\(B_{m-1}F\). It is also stronger than the central token datum
\((S_i,Y_i)\) in the pair-omission spike chart. That chart explicitly allows
the other middle state adjacent through \(S_i\) and the source-row
provenance to change, and it uses occurrence-specific conjugate row copies;
it does not assert one common exact factor.

For a full exact factor, the upper-\(q=1\) histogram \(B_{m+1}F\) is the
complementary image of exact middle ownership and is therefore
factor-independent. The nontrivial factor-level \(q=1\) datum is the lower
angle histogram \(B_{m-1}F\). The near-rainbow upper ledger in the PBBS
transition-token construction belongs to the pre-completion word
architecture and should not be identified with this automatic exact-factor
upper histogram.

## 2. The owner-labelled first shadow reconstructs the factor

Let \(F\) be any spanning \(2\)-factor of \(O_m\). For
\(X\in\binom{[n]}m\), let \(Y_F(X),Z_F(X)\) be its two distinct factor
neighbours and define

\[
\chi_F(X)=Y_F(X)\cap Z_F(X)
   \in\binom{[n]}{m-1}.
\tag{2.1}
\]

Under the standard odd-cycle/wreath dictionary, the multiset of the
\(W\) values \(\chi_F(X)\) is the rank-\((m-1)\) cyclic-interval histogram
when \(F\) is an exact wreath factor.

Indeed, for a row \(C=(c_0,\ldots,c_{n-1})\), write
\(I_C(a,r)=\{c_a,\ldots,c_{a+r-1}\}\) with cyclic indices and take its
odd-cycle vertices to be

\[
X_i=I_C(im,m).
\]

Then \(X_i\) and \(X_{i+1}\) are disjoint, while

\[
X_{i-1}\cap X_{i+1}=I_C(im+m+1,m-1).
\tag{2.0}
\]

Since \(\gcd(m,n)=1\), the starts \(im+m+1\) run through all cyclic
positions. Thus one row contributes every one of its rank-\((m-1)\)
cyclic intervals exactly once as an owner colour.

### Theorem 2.1 (owner-labelled \(q=1\) rigidity)

For every middle owner \(X\), the pair of incident \(F\)-neighbours is
recovered from \((X,\chi_F(X))\). Explicitly, if

\[
X^c\setminus\chi_F(X)=\{a,b\},
\]

then

\[
\{Y_F(X),Z_F(X)\}
=\{\chi_F(X)\cup\{a\},\chi_F(X)\cup\{b\}\}.
\tag{2.2}
\]

Consequently, for spanning \(2\)-factors \(F,F'\),

\[
\chi_F(X)=\chi_{F'}(X)
\quad\Longleftrightarrow\quad
N_F(X)=N_{F'}(X),
\tag{2.3}
\]

and hence

\[
\boxed{\chi_F=\chi_{F'}\quad\Longleftrightarrow\quad F=F'.}
\tag{2.4}
\]

#### Proof

Both neighbours of \(X\) are \(m\)-subsets of the \((m+1)\)-set \(X^c\).
Thus they are \(X^c\setminus\{a\}\) and
\(X^c\setminus\{b\}\) for distinct \(a,b\in X^c\). Their intersection is
\(X^c\setminus\{a,b\}\), proving (2.2). The remaining assertions follow
owner by owner. \(\square\)

### Corollary 2.2 (equivariant rigidity)

If \(g\in S_n\) and

\[
\chi_{F'}(gX)=g\chi_F(X)
\qquad\text{for every }X,
\tag{2.5}
\]

then \(F'=gF\).

#### Proof

Apply Theorem 2.1 to \(F\) and \(g^{-1}F'\). \(\square\)

Thus a closed state-dependent coordinate commutator which returns the
owner-labelled PBBS \(q=1\) field returns the whole factor. If its cumulative
frame is \(g\), every rank histogram is only relabelled:

\[
B_rF'=gB_rF.
\tag{2.6}
\]

Every floor, missing-count, overload, and quadratic collision objective is
coordinate-relabel invariant, so no such commutator gives progress.

There is also an exact support identity. Put

\[
V_\Delta(F,F')=
\{X:N_F(X)\ne N_{F'}(X)\}.
\]

Then

\[
\boxed{
V_\Delta(F,F')
=\{X:\chi_F(X)\ne\chi_{F'}(X)\}.}
\tag{2.7}
\]

Hence positive-density odd-factor support necessarily creates
positive-density owner-labelled \(q=1\) motion.

## 3. Unlabelled \(q=1\) preservation is Eulerian transport

Define

\[
\mu_F(T)=\#\{X:\chi_F(X)=T\},
\qquad T\in\binom{[n]}{m-1}.
\tag{3.1}
\]

For spanning \(2\)-factors \(F,F'\), form a directed multigraph
\(\mathscr D(F,F')\) on the
rank-\((m-1)\) colours by inserting, for every owner \(X\), one arc

\[
\chi_F(X)\longrightarrow\chi_{F'}(X).
\tag{3.2}
\]

Loops may be discarded.

### Theorem 3.1 (Eulerian colour-transport criterion)

For every colour \(T\),

\[
\mu_F(T)-\mu_{F'}(T)
=d^+_{\mathscr D}(T)-d^-_{\mathscr D}(T).
\tag{3.3}
\]

Consequently,

\[
\boxed{
\mu_F=\mu_{F'}
\quad\Longleftrightarrow\quad
\mathscr D(F,F')\text{ is Eulerian}.}
\tag{3.4}
\]

The nonloop arcs of every unlabelled-\(q=1\)-neutral move therefore
decompose into directed colour cycles. When \(F,F'\) are exact wreath
factors, \(\mu_F=B_{m-1}F\) and \(\mu_{F'}=B_{m-1}F'\), so (3.4) is
equivalently \(B_{m-1}F=B_{m-1}F'\).

#### Proof

The arcs leaving \(T\) count its old occurrences, and the arcs entering
\(T\) count its new occurrences. This is (3.3). Equality of the histograms
is equivalent to equality of indegree and outdegree at every colour, and
every finite Eulerian directed multigraph decomposes into directed cycles.
\(\square\)

Thus an arbitrarily large owner set can change while the unlabelled
histogram stays fixed. What is forced is nonlocal circulation. In
particular, a family of atoms which fixes \(\chi_F(X)\) at every owner has
only loops in \(\mathscr D\), and Theorem 2.1 makes its endpoint trivial.

There is a useful geometric refinement. If \(F\) and \(F'\) retain one
common incident edge at a changed owner \(X\), then the two colours
\(\chi_F(X)\) and \(\chi_{F'}(X)\) differ by one Johnson exchange. Hence
the transport arc is an oriented edge of \(J(n,m-1)\). This is the case
for an ordinary alternating-cycle switch. If neither incident edge is
retained, the two colours differ by at most two Johnson exchanges.
Therefore every general colour-transport arc has Johnson distance at most
two.

### Lemma 3.2 (paired transition-token rigidity)

Let \(D\) be a simple transition \(2\)-factor on \(m\)-sets. For an edge
\(XX'\), put

\[
S= X\cap X',\qquad U=X\cup X'.
\]

Then the paired token \((S,U)\) determines the edge:

\[
U\setminus S=\{a,b\},
\qquad
\{X,X'\}=\{S\cup\{a\},S\cup\{b\}\}.
\tag{3.5}
\]

Consequently, if the lower labels are rainbow and the assigned map
\(S\mapsto U(S)\) is fixed, then the transition \(2\)-factor, its cyclic
components, and all of its multidepth flag multisets are fixed.

#### Proof

Equation (3.5) is immediate from
\(|S|=m-1\), \(|U|=m+1\). The paired-token multiset therefore determines
the edge set. A \(2\)-regular edge set determines its cycles, and the
deeper intersections and unions are read from those cycles. \(\square\)

This lemma identifies the hidden factor-consistency obligation in the
owner-fixed spike chart. Its occurrence-specific rows are legitimate
literal token sources, but promoting them to one exact factor must change
additional paired tokens or factor neighbours at seams. If the unlabelled
PBBS \(q=1\) ledger is retained, those changes must close into the
Eulerian transport of Theorem 3.1.

## 4. Complementation forbids upper-\(q=2\) action

Let \(\kappa_r\) be the coordinate-complement map from rank \(r\) to rank
\(n-r\). For every cyclic row \(C\), the complement of a cyclic
\(r\)-interval is a cyclic \((n-r)\)-interval, so

\[
B_{n-r}e_C=\kappa_r B_re_C.
\tag{4.1}
\]

### Theorem 4.1 (exact lower/upper complement hierarchy)

Let \(z\) be a signed difference of exact factors. Then

\[
B_mz=0\quad\Longrightarrow\quad B_{m+1}z=0.
\tag{4.2}
\]

More generally, for \(h\ge1\),

\[
B_{m-h}z=0\quad\Longrightarrow\quad B_{m+h+1}z=0.
\tag{4.3}
\]

Thus preservation of the lower shadows at depths \(1,\ldots,s\) forces
preservation of the upper shadows at depths \(1,\ldots,s+1\).

#### Proof

Equation (4.2) is (4.1) with \(r=m\), because \(n-m=m+1\). Equation
(4.3) follows because

\[
n-(m-h)=m+h+1.
\]

Apply (4.1) to \(z\). \(\square\)

In particular,

\[
\boxed{
B_mz=B_{m-1}z=0
\quad\Longrightarrow\quad
B_{m+1}z=B_{m+2}z=0.}
\tag{4.4}
\]

Therefore a lower-\(q=1\)-neutral exact-factor commutator cannot move
upper depth \(2\). A lower depth-\(2\) effect is accompanied, after
complementation, by an upper depth-\(3\) effect, not upper depth \(2\).

This theorem is specific to full cyclic-wreath incidence. It must not be
applied to the raw long-component PBBS \(2\)-factor or to independent
pair-omission token rows before a common exact-wreath completion is proved.

## 5. The universal boundary-deck ceiling

Suppose two exact factors \(F,F'\) are obtained by sewing the same nonempty
odd-graph residual paths

\[
P_1,\ldots,P_R,
\qquad L_i=|V(P_i)|,
\tag{5.1}
\]

possibly with different path orientations and endpoint pairings. A lower
depth-\(q\) occurrence along an oriented factor cycle is a stride-two block

\[
X_j\cap X_{j+2}\cap\cdots\cap X_{j+2q}.
\tag{5.2}
\]

Every block wholly inside one residual path is identical in the two
sewings. For either sewing, path \(P_i\) contributes at most
\(\min(L_i,2q)\) boundary-crossing starts. Put

\[
b_q=\sum_{i=1}^R\min(L_i,2q)\le2qR.
\tag{5.3}
\]

### Theorem 5.1 (common-residual boundary deck)

For \(q\ge1\),

\[
\boxed{
\|B_{m-q}(F'-F)\|_1\le2b_q\le4qR.}
\tag{5.4}
\]

By complementation,

\[
\boxed{
\|B_{m+q}(F'-F)\|_1\le4(q-1)R.}
\tag{5.5}
\]

#### Proof

Delete the identical internal blocks from both histograms. Each remaining
one-sign boundary deck has mass at most \(b_q\), so the triangle inequality
gives (5.4). Equation (5.5) follows from (4.1) and (5.4) at lower depth
\(q-1\). \(\square\)

The same statement yields a universal pairwise stability bound. Put

\[
e=|E(F)\setminus E(F')|
  =|E(F')\setminus E(F)|,
\tag{5.6}
\]

and let

\[
s=|V_\Delta(F,F')|.
\tag{5.7}
\]

Deleting the \(e\) old-only edges from the noncommon old cycles leaves
exactly \(e\) maximal common residual paths, with isolated vertices allowed;
common cycles cancel. The new-only edges sew the same paths into \(F'\).
Also, the old-only graph has maximum degree two on the \(s\) changed
owners, so \(e\le s\).

### Corollary 5.2 (deeper shadows are Lipschitz in labelled \(q=1\))

For every \(q\ge1\),

\[
\boxed{
\|B_{m-q}(F'-F)\|_1\le4qe\le4qs,}
\tag{5.8}
\]

and

\[
\boxed{
\|B_{m+q}(F'-F)\|_1\le4(q-1)e\le4(q-1)s.}
\tag{5.9}
\]

Since nonzero histogram coordinates are integral,
\(|\operatorname{supp}B_r(F'-F)|\le\|B_r(F'-F)\|_1\) as well.

### Corollary 5.3 (quantitative seam-richness)

If, for some \(q\le H\), either a lower or upper band increment has
support at least \(\delta W\), or has \(\ell^1\)-norm at least
\(\delta W\), then

\[
e,s\ge\frac{\delta W}{4H}.
\tag{5.10}
\]

Let \(C\) be the number of affected old \(n\)-wreath rows. Then \(C\le B\)
and all \(e\) old-only edges lie in those rows. Hence

\[
\frac eC\ge\frac{\delta n}{4H}.
\tag{5.11}
\]

At \(H=A\sqrt m\), the right side is

\[
\left(\frac{\delta}{2A}+o(1)\right)\sqrt m.
\tag{5.12}
\]

If the \(\delta W\) action is at lower depth \(2\), then

\[
\frac eC\ge\frac{\delta n}{8}=\Theta(m).
\tag{5.13}
\]

These are residual-seam counts, not physical output-component counts. A
final exact factor always has \(B\) wreath rows, so for \(H=o(n)\),

\[
B=o(W/H),\qquad HB=o(W).
\tag{5.14}
\]

Thus the desired physical budget is compatible with (5.10): the many
residual seams must be absorbed entry-neutrally into only \(B\) completed
wreaths. A construction which initializes every residual path separately
would pay \(HR=\Omega(W)\) in the worst band case and cannot work. This is
a design requirement, not a global nonexistence proof.

Here \(e\) counts deleted old edges, equivalently maximal common residual
paths. There are \(2e\) boundary ports. If one calls ports rather than cut
edges “seams,” every average in (5.11)--(5.13) doubles. A selected
ownership-overlay component contains at least one affected old row, so the
same lower bounds hold, a fortiori, when averaging over selected overlay
components.

### Corollary 5.4 (aggregate-band ceiling)

Summing (5.8)--(5.9) over \(2\le q\le H\) gives

\[
\sum_{q=2}^H
\left(
\|B_{m-q}(F'-F)\|_1+
\|B_{m+q}(F'-F)\|_1
\right)
\le4(H^2-1)e.
\tag{5.15}
\]

Hence \(\delta W\) aggregate band action forces only

\[
e\ge\frac{\delta W}{4(H^2-1)}.
\tag{5.16}
\]

At \(H=A\sqrt m\), this is merely Catalan scale. Thus the universal
boundary-deck invariant does not rule out a construction whose useful
action is distributed thinly over all Gaussian depths. The stronger
\(\Omega(n/H)\) seams-per-component conclusion (5.11) applies to
\(\Omega(W)\) action at one controlled depth. Existing bounded MSW/AC2
cells have a separate constant-per-depth profile and therefore only
\(O(HB)\) aggregate action; that is an architecture-specific fact.

## 6. Exact transposition gate and the failure of independent cubes

Let \(\tau\) be a coordinate transposition, and let \(L\) be a union of
whole ownership-overlay components of an exact factor \(F\) against
\(\tau F\). Replacing \(L\) by \(\tau L\) gives an exact factor \(F_L\),
and for every cyclic rank \(r\),

\[
B_r(F_L-F)=(\tau-I)B_r\mathbf1_L.
\tag{6.1}
\]

Hence the exact prepared shallow-neutral component gate is

\[
\boxed{
(\tau-I)B_{m-1}\mathbf1_L=0,
\qquad
(\tau-I)B_{m-q}\mathbf1_L\ne0
\text{ for some }q\ge2.}
\tag{6.2}
\]

For positive-density band action, (6.2) must additionally satisfy the
seam lower bound (5.10), and its \(q=1\) owner transport must be Eulerian.

There is a hereditary consequence. Suppose an independently signable exact
component cube has generators \(z_1,\ldots,z_d\), and **every** corner has
the same lower-\(q=1\) histogram. Comparing two corners which differ in one
bit gives

\[
B_{m-1}z_i=0
\qquad(1\le i\le d).
\tag{6.3}
\]

Thus a family whose individual generators all have nonzero first-shadow
increments cannot become hereditarily \(q=1\)-neutral merely by granting
independent signs. Its bits must be tied so that their transport arcs cancel
globally.

This closes the existing frozen libraries:

* every exact common-core \(C_8\) has nonzero first-shadow increment;
* the complete shifted MSW two-for-two atlas has a triangular unit minor,
  so its first-shadow map is injective even on integer combinations;
* interleaving global relabellings with transported toggles of one fixed
  owner-disjoint Catalan packet family has the normal form \(gF_\varepsilon\);
  it does not create a fresh shallow kernel;
* the vertex-disjoint clean PBBS \(C_8\) supply consists of ordinary
  spanning-\(2\)-factor switches, not exact-wreath trades, and each selected
  local cycle contributes only \(O(q)\) depth-\(q\) boundary action.

In particular, a Catalan-size disjoint family has \(e=O(B)\), and for
\(q\le H=o(n)\), (5.8) gives only

\[
O(HB)=o(W)
\tag{6.4}
\]

band action. The overlapping \(\Theta(W)\) PBBS candidate reservoir could
have enough raw seam mass, but no theorem fuses it into jointly legal,
point-regular, length-\(n\) exact components with Eulerian \(q=1\) transport.

## 7. Sharpness: the AC2 Eulerian triangle, and why it does not finish

There is already a genuine finite exact-factor witness at \(m=4\). The
certified four-for-four circuit \(w_4\) has a common ten-row completion to
two exact fourteen-row factors and satisfies

\[
B_4w_4=B_3w_4=0,\qquad B_2w_4\ne0.
\tag{7.1}
\]

Thus no dimension-free theorem can say that unlabelled lower-\(q=1\)
neutrality forces lower-\(q=2\) neutrality. What fails is an asymptotic
positive-density suspension of this phenomenon.

For every \(m\ge510\), the AC2 construction supplies a support-feasible
six-for-six partial trade

\[
Z=z_{xy}+z_{yz}-z_{xz},
\tag{7.2}
\]

made from three connected universal two-for-two components. It satisfies

\[
B_mZ=B_{m-1}Z=0,
\qquad
B_{m-2}Z\ne0.
\tag{7.3}
\]

Its three first-shadow component columns have the form

\[
f_y-f_x,\qquad f_z-f_y,\qquad f_x-f_z.
\tag{7.4}
\]

Thus its unlabelled cancellation is literally the Eulerian colour cycle

\[
x\longrightarrow y\longrightarrow z\longrightarrow x.
\tag{7.5}
\]

This proves that Theorem 2.1 cannot be strengthened from owner-labelled
rigidity to unlabelled-histogram rigidity.

The exact positive endpoint is nevertheless missing. If \(N\) is the
six-row negative sign, applicability is equivalent to a common residual
completion

\[
B_m\mathbf1_H
=\mathbf1-B_m\mathbf1_N,
\qquad H\in\mathbb Z_{\ge0}^{\Omega_m}.
\tag{7.6}
\]

Neither (7.6) nor even rational-cone membership of its residual is proved.
The aligned canonical MSW factor cannot supply the completion, because its
local first-shadow columns have the triangular unit minor.

For clarity, suppose conditionally that one exact factor contains
\(\ell\ge\gamma B\) pairwise middle-root-disjoint negative AC2 triangles.
Then their \(3\ell\) two-for-two components give a literal grouped cube.
All grouped corners preserve \(B_{m-1}\), replace \(6\ell\) old rows, and
rebundle \(6n\ell=\Theta(W)\) row-owner incidences. For suitable opposite
grouped corners,

\[
\left\|B_{m-2}(F^1-F^0)\right\|_2^2\ge2\ell.
\tag{7.7}
\]

However, the odd-factor edge change is only \(12\ell=O(B)\) old edges, and
the depth-\(2\) support of one triangle is bounded by a constant. Hence this
conditional family has positive density in **row rebundling**, but only
Catalan-scale deeper-shadow action. It still fails the requested
\(\Theta(W)\) shadow-support target. A truly successful family needs the
seam-richness of Section 5, not merely a positive density of bounded cells.

## 8. A PBBS-specific centered-charge obstruction

Every explicit clean PBBS \(C_8\) contains a compulsory residual
three-vertex path with core \(K\in\binom{[n]}{m-1}\) and centered charge

\[
\zeta_K=n\mathbf1_K-(m-1)\mathbf1.
\tag{8.1}
\]

### Theorem 8.1 (zero-background PBBS sewing obstruction)

Suppose one point-regular output \(n\)-cycle contains \(t\) disjoint
distinguished PBBS three-paths with cores \(K_1,\ldots,K_t\), and every
other residual piece in that output cycle has centered charge zero. Put

\[
g=\gcd(n,m-1)=\gcd(3,m-1)\in\{1,3\}.
\tag{8.2}
\]

Then

\[
\frac ng\mid t,
\qquad
3t\le n.
\tag{8.3}
\]

Consequently:

* if \(g=1\), then \(t=0\);
* if \(g=3\) and \(t>0\), then necessarily

  \[
  t=\frac n3,
  \qquad
  \sum_{i=1}^{n/3}\mathbf1_{K_i}
  =\frac{m-1}{3}\mathbf1,
  \tag{8.4}
  \]

  and the distinguished three-paths tile the whole output component.

#### Proof

Point balance and (8.1) give

\[
n\sum_{i=1}^t\mathbf1_{K_i}
=(m-1)t\mathbf1.
\tag{8.5}
\]

Coordinatewise divisibility gives \(n/g\mid t\). Disjointness of the
three-vertex paths gives \(3t\le n\). If \(g=1\), these inequalities force
\(t=0\). If \(g=3\), positive \(t\) forces \(t=n/3\); equality in the
vertex bound leaves no other vertices, and (8.5) becomes (8.4).
\(\square\)

Thus outside \(m\equiv1\pmod3\), every affected exact output wreath must
contain an explicit nonzero oppositely centered residual piece. In the
ternary case the only zero-background escape is the rigid total-tiling
one-design in (8.4). This is independent of the Eulerian first-shadow
condition, so a successful PBBS construction must solve both constraints
simultaneously.

## 9. Exact proved/conditional boundary

The following statements are proved.

1. Owner-labelled PBBS \(q=1\) preservation is a complete invariant of the
   odd-graph factor. No nontrivial exact-factor commutator can preserve it.
2. Unlabelled \(q=1\) preservation is exactly Eulerian owner-colour
   transport.
3. For full cyclic-wreath trades, lower-\(q=1\) neutrality forces upper
   depths \(1\) and \(2\) to be fixed.
4. Positive-density action anywhere in \(q\le H\) forces at least
   \(\delta W/(4H)\) changed factor edges and owner-labelled \(q=1\)
   changes, and forces average cut-edge complexity \(\delta n/(4H)\)
   inside a Catalan-size affected-row family. This rankwise statement does not exclude
   a Catalan-seam construction with action distributed over all \(H\)
   depths; its aggregate envelope is (5.15).
5. \(B=o(W/H)\) output rows and \(O(HB)=o(W)\) collars are compatible with
   that requirement; the residual seams must be fused entry-neutrally.
6. Bounded independent Catalan cells, including a hypothetical packed AC2
   triangle family, have only \(O(HB)=o(W)\) band action and cannot supply
   positive-density deeper-shadow support.

One sharp sufficient surviving theorem, in the single-overlay lane, is
therefore:

> **Seam-rich Eulerian PBBS commutator gate.** For each fixed \(A>0\),
> \(H=\lceil A\sqrt m\rceil\), construct one exact factor \(F\) with
> the designated PBBS lower-\(q=1\) histogram (or, for the constant-one
> application, a PBBS-quality \(o(W)\)-defect histogram) and a prepared
> union \(L\) of complete
> ownership-overlay components such that
>
> \[
> (\tau-I)B_{m-1}\mathbf1_L=0,
> \]
>
> its owner-colour transport is Eulerian,
>
> \[
> \max_{2\le q\le H}
> \left\|(\tau-I)B_{m-q}\mathbf1_L\right\|_1
> =\Omega(W)
> \]
>
> (or an equivalent \(\Omega(W)\) useful multidepth action), and the
> \(\Omega(W/H)\) residual seams are resewn into \(O(B)=o(W/H)\) physical
> wreath rows with \(O(HB)=o(W)\) collar charge.

No present PBBS, frozen MSW, owner-fixed spike, or bounded AC2 library
proves this gate. Conversely, the invariants above do not rule out such a
seam-rich, aggregate-\(q=1\)-neutral construction. This is the precise
proved/conditional boundary. A multistep commutator with dynamically
recomputed components need not reduce to one pair \((\tau,L)\), but its
endpoint must still obey the Eulerian and seam-rich invariants of Sections
3 and 5. No constant-one claim follows from this lane.
