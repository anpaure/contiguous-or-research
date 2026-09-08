# AD10: saturating-cycle flags, exact first failures, and the common-base theorem

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, solver, or finite
search is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_h=\binom{2m}{m-h},\qquad
 d_h=N_h-N_{h+1}.
\tag{0.1}
\]

The existing saturating-cycle theorem does **not** instantiate the AD9
durable-flag theorem.  In even dimension it supplies the upper half of the
first flag bijection, but not the lower half.  The odd-dimensional version
used in the AH report supplies only a lower first flag, has the wrong parity
for AD9, and its deeper extension has repeated fibres rather than active
bijections.  It is also an abstract inclusion flow rather than a physical
MTF trajectory.

This report proves four exact replacements.

1. If owner lifetimes may be selected rather than prescribed, two-sided
   integral active flag systems always exist through every depth.  The proof
   uses a common base of two dual transversal matroids at each layer.  Thus
   selectable flag **feasibility** is not the missing theorem; durable edge
   agreement is.

2. For the even saturating cycle, the exact first-layer durable cost is a
   deletion-plus-Hall statistic \(\kappa_1\).  Its elementary lower bound is

   \[
   \kappa_1\ge
   N_1-\left|\{C_i\cap C_{i+1}\}\right|.
   \tag{0.2}
   \]

   Hence the directly testable first estimate required on a Gaussian window
   is

   \[
   \boxed{\kappa_1=o_A(W/H),\qquad H=\lceil A\sqrt m\rceil.}
   \tag{0.3}
   \]

   The saturating-cycle theorem does not imply (0.3).

3. If the cycle is bi-saturating at depth one, the exact depth-two
   first-failure number is another explicit paired-colour/Hall statistic
   \(\kappa_2(I)\), given in Theorem 5.1.  Its paired-rainbow part is the
   matching deficiency of a labelled bipartite graph whose labels are the
   literal triple intersections and complementary double unions.

4. If both full depth-two colour sequences are saturating, their unavoidable
   collision excess is only

   \[
   2(N_1-N_2)=\frac{6N_1}{m+2}=O(W/m)=o_A(W/H).
   \tag{0.4}
   \]

   This proves the desired edge-distribution estimate at depth two.  What
   remains even there is the two boundary Hall matchings.  Iterating the
   same raw saturation bound gives \(2(N_1-N_H)\), which is sufficient only
   for \(H=o(m^{1/3})\), and only under recursively compatible boundary Hall.
   It is linear on a Gaussian window.  Thus q=1 saturation by itself does
   not reach constant one.

All sets, matchings, flags, and cuts below are integral.  Every retained edge
is an actual edge of one fixed owner forest.

## 1. Audit of the three q=1 objects

### 1.1 The even saturating cycle

The consecutive-level saturating-cycle theorem, applied between ranks
\(m\) and \(m+1\) of \(B_{2m}\), gives

\[
 C_0,U_0,C_1,U_1,\ldots,C_{N_1-1},U_{N_1-1},C_0,
\tag{1.1}
\]

where the \(U_i\)'s are all rank-\((m+1)\) sets, the \(C_i\)'s are
\(N_1\) distinct middle sets, and

\[
 C_i\subset U_i\supset C_{i+1}.
\tag{1.2}
\]

Consequently \(C_i,C_{i+1}\) are Johnson neighbours and

\[
 C_i\cup C_{i+1}=U_i.
\tag{1.3}
\]

Orient the contracted cycle as \(C_i\to C_{i+1}\).  The upper-complement
first flag forced at its head is

\[
 R_1(C_{i+1})
 =[2m]\setminus U_i.
\tag{1.4}
\]

Because the \(U_i\)'s enumerate the full upper rank, (1.4) is a bijection
onto \(\binom{[2m]}{m-1}\).  Thus the upper sign is exact.

The forced lower first flag is

\[
 S_i:=L_1(C_i)=C_i\cap C_{i+1}.
\tag{1.5}
\]

Nothing in the saturating-cycle theorem asserts that the \(S_i\)'s are
distinct or cover their rank.  This is exactly the transfer-head condition
in the two-sided Catalan formulation.  Treating (1.1) as a two-sided flag
cycle without proving (1.5) bijective is therefore invalid.

### 1.2 The odd AH core

The AH report instead has \(n=2m+1\), a set \(U\) of \(N_1\) rank-\(m\)
owners, and a lower bijection \(\phi:U\to\binom{[n]}{m-1}\).  Its integral
flow extension uses all \(N_1\) owners at every depth and has fibre sizes

\[
 \left\lfloor\frac{N_1}{N_q}\right\rfloor
 \quad\hbox{or}\quad
 \left\lceil\frac{N_1}{N_q}\right\rceil.
\tag{1.6}
\]

For \(q\ge2\) these are not the bijections
\(X_q\to\binom{[2m]}{m-q}\) required in AD9.  The report also proves only
nested inclusion paths, not the two durable intersection identities along
the Johnson cycle.  It explicitly notes that a general Johnson cycle is not
a tight-window MTF trajectory.  Finally its ambient parity is different.
Thus (1.6) cannot be imported as an AD9 flag system.

The updated Corollary 1.2 of the AH report is stronger at the marginal
level: after adjoining arbitrary nested flags for the omitted owners, it
gives one full-owner integral lower flag family with weighted overload
\(o(W)\) through every Gaussian window.  This settles marginal integrality,
nesting, coverage, and weighted spill.  It still does not couple the
deletion symbols of consecutive cycle owners.  Section 8 below gives the
exact mismatch statistic which Corollary 1.2 leaves uncontrolled.

### 1.3 The scalar Hamilton refinement

The Hamilton-cycle refinement of the odd saturating cycle makes lower
q=1 loads one or two, with the exact floor counts.  It neither supplies the
opposite signed flag nor decomposes into physical depth-growing rotor paths.
Scalar q=1 balance, common-owner active bijections, and durable MTF edges are
three distinct statements.

## 2. Selectable two-sided active flags always exist

This section is independent of saturating cycles.

### Theorem 2.1 (common-base active-flag theorem)

Let \(0\le h<m\).  Suppose \(X_h\) is a set of size \(N_h\), and

\[
 L_h,R_h:X_h\longrightarrow\binom{[2m]}{m-h}
\tag{2.1}
\]

are bijections.  Then there is a common subset

\[
 X_{h+1}\subset X_h,\qquad |X_{h+1}|=N_{h+1},
\tag{2.2}
\]

and bijections

\[
 L_{h+1},R_{h+1}:X_{h+1}longrightarrow
 \binom{[2m]}{m-h-1}
\tag{2.3}
\]

such that, for every \(v\in X_{h+1}\),

\[
 L_{h+1}(v)\subset L_h(v),\qquad
 R_{h+1}(v)\subset R_h(v).
\tag{2.4}
\]

Consequently, starting from

\[
 X_0=\binom{[2m]}m,\qquad
 L_0(v)=v,\qquad R_0(v)=[2m]\setminus v,
\tag{2.5}
\]

one can construct integral two-sided active flags through every prescribed
depth \(H<m\), provided the lifetime sets are selectable.

#### Proof

Write \(r=m-h\), \(M=N_h\), \(M'=N_{h+1}\), and \(d=M-M'\).
Consider the inclusion graph between

\[
 \mathcal V_r=\binom{[2m]}r
 \quad\hbox{and}\quad
 \mathcal V_{r-1}=\binom{[2m]}{r-1}.
\]

Let \(\mathcal T\) be the transversal matroid on ground set
\(\mathcal V_r\): a family is independent when it can be matched
injectively to rank \(r-1\) along facet incidences.  Its rank is \(M'\).

The vector which is constantly

\[
 q=\frac{M'}M=\frac r{2m-r+1}
\tag{2.6}
\]

belongs to the base polytope of \(\mathcal T\).  Indeed, put weight
\(1/(2m-r+1)\) on every incidence edge.  Every rank-\((r-1)\) vertex has
weighted degree one, while every rank-\(r\) vertex has weighted degree
\(q\).  Bipartite matching integrality decomposes this fractional matching
into maximum integral matchings, proving the assertion.

It follows by matroid duality that the constant vector

\[
 p=1-q=\frac dM
\tag{2.7}
\]

belongs to the base polytope of \(\mathcal T^*\), whose rank is \(d\).
Pull \(\mathcal T^*\) back to \(X_h\) once through \(L_h\) and once
through \(R_h\); call the resulting matroids \(\mathcal M_L,\mathcal M_R\).
The same constant vector \(p\mathbf1\) belongs to both base polytopes.

For completeness, apply the matroid-intersection min--max theorem.  For
every \(A\subseteq X_h\),

\[
 d=p|X_h|
 =p|A|+p|X_h\setminus A|
 \le r_{\mathcal M_L}(A)+r_{\mathcal M_R}(X_h\setminus A).
\tag{2.8}
\]

Therefore \(\mathcal M_L\) and \(\mathcal M_R\) have a common independent
set \(I_h\) of size \(d\).  Since both matroids have rank \(d\), this is a
common base.  Put

\[
 X_{h+1}=X_h\setminus I_h.
\]

The complement of a base of \(\mathcal T^*\) is a base of
\(\mathcal T\).  Hence both endpoint families indexed by \(X_{h+1}\)
have perfect facet matchings onto the complete next rank.  Take those two
integral matchings as \(L_{h+1}\) and \(R_{h+1}\).  This proves
(2.2)--(2.4), and induction proves the final assertion. \(\square\)

The theorem does not say that the two perfect matchings agree with any
prescribed rotor edge.  That is precisely the durable gate.

### Corollary 2.2 (unconditional lifetime-seam bound)

Let \(F\) be any directed path forest on \(X_0\), and construct the nested
sets in Theorem 2.1.  Give owner \(v\) lifetime

\[
 \tau(v)=\max\{h:v\in X_h\}.
\]

If \(J\) is the set of edges of \(F\) whose endpoints have unequal
lifetimes, then

\[
 \boxed{
 |J|\le2\sum_{h=0}^{H-1}|X_h\setminus X_{h+1}|
 =2(W-N_H)
 \le\frac{2WH^2}{m}.}
\tag{2.9}
\]

In particular,

\[
 H=o(m^{1/3})\quad\Longrightarrow\quad |J|=o(W/H).
\tag{2.10}
\]

#### Proof

An edge with unequal endpoint lifetimes crosses exactly the stopped/active
cut at the smaller endpoint lifetime.  A stopped owner has degree at most
two in a path forest, giving the first inequality.  The stopped sets are
disjoint and telescope to \(W-N_H\).  Finally

\[
 d_h=N_h\frac{2h+1}{m+h+1}
 \le W\frac{2h+1}{m},
\]

and \(\sum_{h=0}^{H-1}(2h+1)=H^2\). \(\square\)

Thus arbitrary selectable flags already have a sufficiently small lifetime
boundary on every \(H=o(m^{1/3})\) window.  No corresponding durable-edge
bound follows.

## 3. Fusion with arbitrary selectable lifetimes

The globally contiguous lifetime order in AD9 can be replaced by an exact
edge boundary count.

### Lemma 3.1 (arbitrary-lifetime durable fusion)

Let \(F\) be a directed path forest with \(p\) components, let
\((\mathbf L,\mathbf R)\) be feasible active flags through depth \(H\),
let \(J\) be the unequal-lifetime edges, and let \(D\) be the equal
positive-lifetime edges which are not durable through their common
lifetime.  Put \(K=|D|\).  Then there is one literal band word of exact form

\[
 L=W+2\sum_S r(S),
\tag{3.1}
\]

where the sum is over the components obtained after cutting \(D\cup J\),
and \(r(S)\) is their common lifetime.  Consequently

\[
 \boxed{L\le W+2H(p+K+|J|).}
\tag{3.2}
\]

#### Proof

After the cuts, every component has constant lifetime.  A positive-radius
surviving edge is durable and hence is a genuine rotor edge at every level
up to that radius; a radius-zero edge is an ordinary Johnson edge.  The
exact rotor-path word for a component with \(t\) owners and radius \(r\)
has length \(t+2r\).  Concatenate these words.  The owner terms sum to
\(W\), and cutting a forest edge raises the component count by one.  This
gives (3.1)--(3.2). \(\square\)

Therefore, for any growing window, the exact composition target is

\[
 p+K+|J|=o(W/H).
\tag{3.3}
\]

Theorem 2.1 settles flag feasibility, and Corollary 2.2 settles \(J\) on
subcubic windows.  It does not settle \(K\).

## 4. The exact q=1 cost of the even saturating cycle

Return to (1.1).  Let

\[
 \mathcal Y_1=\binom{[2m]}{m-1},\qquad
 S_i=C_i\cap C_{i+1}.
\tag{4.1}
\]

For a nonempty set \(Q\subseteq\mathbb Z_{N_1}\), delete the cycle edges
\(C_i\to C_{i+1}\) with \(i\in Q\).  The remaining graph is a spanning
directed path forest on the \(N_1\) cycle owners with exactly \(|Q|\)
components.  Define

\[
 \mathcal M^-(Q)
 =\mathcal Y_1\setminus\{S_i:i\notin Q\},
\tag{4.2}
\]

and let its lower boundary graph have left class

\[
 T^-(Q)=\{C_i:i\in Q\}
\tag{4.3}
\]

and adjacency \(C_i\sim S\) exactly when \(S\subset C_i\).

### Theorem 4.1 (exact saturating-cycle q=1 statistic)

The retained path forest admits two-sided active first flags which make
every retained edge durable if and only if

1. the colours \(S_i\), \(i\notin Q\), are pairwise distinct; and
2. the balanced graph between \(T^-(Q)\) and \(\mathcal M^-(Q)\) has a
   perfect matching.

Equivalently, condition 2 is

\[
 \left|\{C_i:i\in Q,\ S\subset C_i
          \text{ for some }S\in\mathcal A\}\right|
 \ge|\mathcal A|
 \quad(\mathcal A\subseteq\mathcal M^-(Q)).
\tag{4.4}
\]

Consequently the exact q=1 component statistic is

\[
 \boxed{
 \kappa_1(C)
 =\min_{\varnothing\ne Q\subseteq\mathbb Z_{N_1}}
 \{|Q|:\text{conditions 1--2 hold}\}.}
\tag{4.5}
\]

Adding the \(W-N_1=W/(m+1)\) omitted middle owners as lifetime-zero
isolated vertices gives a literal word through ranks \(m-1,m,m+1\) of
exact length

\[
 \boxed{W+2\kappa_1(C).}
\tag{4.6}
\]

#### Proof

For a retained edge \(C_i\to C_{i+1}\), lower durability forces
\(L_1(C_i)=S_i\).  Since \(L_1\) is injective, condition 1 is necessary.
The unforced lower owners are exactly the path terminals \(C_i\),
\(i\in Q\), and the unused lower targets are exactly (4.2).  Their numbers
are both \(|Q|\), so Hall gives precisely condition 2.

On the upper-complement side, a retained edge forces

\[
 R_1(C_{i+1})=[2m]\setminus U_i.
\]

These targets are distinct.  The unforced sources are \(C_{i+1}\),
\(i\in Q\), and the missing targets are \([2m]\setminus U_i\),
\(i\in Q\).  The assignment with the same index is valid because
\(C_{i+1}\subset U_i\).  Thus the upper boundary matching is automatic.
The constructed flags make every retained edge durable, proving
(4.5).

Each positive-radius component has radius one and costs two initialization
letters; every omitted owner has radius zero and costs one owner letter only.
This gives (4.6). \(\square\)

### Corollary 4.2 (first edge-distribution obstruction)

Let

\[
 \delta_1(C)=N_1-|\{S_i:i\in\mathbb Z_{N_1}\}|.
\tag{4.7}
\]

Then

\[
 \boxed{\kappa_1(C)\ge\max\{1,\delta_1(C)\}.}
\tag{4.8}
\]

If \(\delta_1(C)=0\), then \(\kappa_1(C)=1\).

#### Proof

To leave distinct colours, at least one edge must be deleted for every
occurrence in excess of the number of supported colours, giving
\(|Q|\ge\delta_1(C)\).  At least one edge is needed to turn a cycle into a
path forest.  If \(\delta_1=0\), delete any edge \(i\).  Its lower colour
\(S_i\) is the unique missing target and satisfies \(S_i\subset C_i\), so
the one-by-one lower Hall test passes. \(\square\)

Thus a **bi-saturating** cycle would give exact q=1 flags with one active
component and zero durable defect.  The published saturating-cycle theorem
proves only the upper saturation in (1.3), not \(\delta_1=0\).

## 5. Exact depth-two first failures after bi-saturation

Assume now that \(\delta_1(C)=0\).  Cut the cycle so that the depth-two
active owners form a terminal cyclic block

\[
 I=\{C_a,C_{a+1},\ldots,C_b\},\qquad |I|=N_2.
\tag{5.1}
\]

The preceding \(N_1-N_2\) cycle owners have lifetime one.  Retain the q=1
flags coming from the full cycle and write

\[
 T_i:=R_1(C_i)=[2m]\setminus U_{i-1}.
\tag{5.2}
\]

For every internal active edge \(e_i:C_i\to C_{i+1}\),
\(a\le i<b\), define the forced depth-two pair

\[
 A_i=S_i\cap S_{i+1}
     =C_i\cap C_{i+1}\cap C_{i+2},
\tag{5.3}
\]

\[
 B_i=T_i\cap T_{i+1}
     =[2m]\setminus(U_{i-1}\cup U_i).
\tag{5.4}
\]

Both have rank \(m-2\).  Indeed, \(S_i,S_{i+1}\) are distinct facets of
\(C_{i+1}\), while \(T_i,T_{i+1}\) are distinct facets of
\([2m]\setminus C_i\).

For \(Q\subseteq\{a,a+1,\ldots,b-1\}\), retain the internal edges outside
\(Q\).  Let \(Y^-(Q)\) and \(Y^+(Q)\) be the rank-\((m-2)\) targets missing
from the retained \(A\)- and \(B\)-colour sets.  Let

\[
 T^-(Q)=\{C_b\}\cup\{C_i:i\in Q\},
\tag{5.5}
\]

\[
 T^+(Q)=\{C_a\}\cup\{C_{i+1}:i\in Q\}.
\tag{5.6}
\]

The lower boundary adjacency is \(C_i\sim A\) iff \(A\subset S_i\), and
the upper boundary adjacency is \(C_i\sim B\) iff \(B\subset T_i\).

### Theorem 5.1 (exact depth-two cut statistic)

For the fixed block \(I\), the minimum number of internal active edges
whose first durable failure occurs at level one is

\[
 \boxed{
 \kappa_2(I)=\min_Q|Q|,}
\tag{5.7}
\]

where the minimum is over precisely those \(Q\) for which

1. the retained \(A_i\)'s are pairwise distinct;
2. the retained \(B_i\)'s are pairwise distinct;
3. the balanced graph \(T^-(Q)\leftrightarrow Y^-(Q)\) has a perfect
   matching; and
4. the balanced graph \(T^+(Q)\leftrightarrow Y^+(Q)\) has a perfect
   matching.

In particular, \(\kappa_2(I)=0\) if and only if the internal \(A_i\)'s
are distinct, their unique missing target is a facet of \(S_b\), the
internal \(B_i\)'s are distinct, and their unique missing target is a facet
of \(T_a\).

#### Proof

For a retained edge, the two durable identities force

\[
 L_2(C_i)=A_i,\qquad R_2(C_{i+1})=B_i.
\]

Thus conditions 1--2 are necessary.  In the lower forest, the unforced
owners are exactly its terminals (5.5); in the upper-complement forest they
are exactly its sources (5.6).  In each sign their number is \(|Q|+1\),
equal to the number of missing targets.  The two Hall tests are therefore
necessary.

Conversely, the two perfect boundary matchings, together with the forced
assignments on retained edges, define bijections \(L_2,R_2\).  Every chosen
target is a facet of its current q=1 endpoint.  Hence the flags are nested
and every retained edge satisfies both durable identities at level one.
The deleted edges fail first at that level, proving (5.7).  The last
assertion is the case \(Q=\varnothing\). \(\square\)

Form the bipartite multigraph \(\mathscr B_I\) on two copies of
\(\binom{[2m]}{m-2}\), with one labelled edge \(A_iB_i\) for every
internal active edge.  Theorem 5.1 immediately gives the directly testable
lower bound

\[
 \boxed{
 \kappa_2(I)
 \ge (N_2-1)-\nu(\mathscr B_I),}
\tag{5.8}
\]

where \(\nu\) is matching number.  This is the exact paired edge-distribution
obstruction; the gap between (5.8) and equality is precisely the two
Boolean boundary Hall problems.

## 6. What full depth-two saturation would buy

Extend (5.3)--(5.4) cyclically over all \(N_1\) q=1 owners.  Assume the two
support equalities

\[
 \{A_i:i\in\mathbb Z_{N_1}\}
 =\binom{[2m]}{m-2},
\tag{6.1}
\]

\[
 \{B_i:i\in\mathbb Z_{N_1}\}
 =\binom{[2m]}{m-2}.
\tag{6.2}
\]

These are two new saturation assertions.  Neither follows from q=1
bi-saturation.  They say that the two induced Hamilton cycles on the q=1
flag rank have complete edge-colour support.

### Lemma 6.1 (exact paired-collision budget)

Under (6.1)--(6.2), for every active block \(I\) there is a set of at most

\[
 \boxed{
 2(N_1-N_2)=\frac{6N_1}{m+2}}
\tag{6.3}
\]

internal edges whose deletion makes both retained colour maps
\(i\mapsto A_i\) and \(i\mapsto B_i\) injective.  Equivalently,

\[
 (N_2-1)-\nu(\mathscr B_I)
 \le2(N_1-N_2).
\tag{6.4}
\]

#### Proof

For either sign, let \(\mu(S)\) be its full cyclic colour multiplicity.
Surjectivity and the fact that there are \(N_1\) occurrences give

\[
 \sum_S(\mu(S)-1)=N_1-N_2.
\tag{6.5}
\]

For any subset of occurrence positions, its collision excess
\(\sum_S(\mu_I(S)-1)_+\) is at most the right side of (6.5).  Delete all
but one occurrence of every repeated lower colour in the active block, and
then do the same for the upper colours.  The union of the two deletion sets
has size at most \(2(N_1-N_2)\), and the surviving labelled edges form a
matching in \(\mathscr B_I\).  Finally

\[
 \frac{N_2}{N_1}=\frac{m-1}{m+2},
\]

which gives (6.3). \(\square\)

For \(H=O_A(\sqrt m)\), (6.3) is \(o_A(W/H)\).  Hence, at depth two,
the raw paired-rainbow distribution would already be quantitatively strong
enough.  The exact remaining condition is that one can choose such a
deletion set so that the two boundary graphs in Theorem 5.1 satisfy Hall.
No marginal saturation theorem supplies those matchings.

The local obstruction is sharp in scope.  A run of \(r\) internal edges
with one repeated \(A\)-colour forces at least \(r-1\) first failures,
regardless of the upper side.  Existing depth-one rainbowness does not
exclude such collapsed depth-two runs or nonlocal repetitions.

## 7. Recursive quantitative boundary

At a general recursive layer, once \(L_h,R_h,X_{h+1}\) and the surviving
forest are fixed, define \(\kappa_{h+1}\) exactly as in Theorem 5.1: it is
the minimum number of new edge deletions needed to make the two forced
colour maps injective and to pass the terminal/source Hall tests.  The
first-failure ledger is then

\[
 \boxed{K_H=\sum_{h=0}^{H-1}\kappa_{h+1},}
\tag{7.1}
\]

with \(\kappa_1\) interpreted by Theorem 4.1 after the structural cycle
cuts.  Choices at level \(h\) determine the instance at level \(h+1\), so
the minima may not be optimized independently.

If, conditionally, every recursive cyclic occurrence system were
two-sided saturating and the duplicate deletions could always be chosen to
pass both boundary Hall tests, the analogue of Lemma 6.1 would give

\[
 K_H\le2\sum_{h=1}^{H-1}d_h
 =2(N_1-N_H)
 \le\frac{2W(H^2-1)}m.
\tag{7.2}
\]

Thus this raw saturation scheme would imply

\[
 K_H=o(W/H)
 \quad\text{when}\quad H=o(m^{1/3}).
\tag{7.3}
\]

This is only a conditional composition: recursive saturation and the
boundary Hall choices are unproved.  At \(H=\Theta(\sqrt m)\), the right
side of (7.2) is \(\Theta_A(W)\), so even proving saturation at every rank
would not establish the Gaussian-window durable estimate by this naive
collision deletion.

## 8. Exact deletion-symbol count for the odd AH core

This section addresses the updated Corollary 1.2 directly.  Its notation is
local to odd dimension:

\[
 n=2m+1,\qquad M=N_1=\binom{n}{m-1}.
\tag{8.1}
\]

Use the source indexing of the saturating Boolean cycle:

\[
 S_0,X_0,S_1,X_1,\ldots,S_{M-1},X_{M-1},S_0,
\tag{8.2}
\]

so that

\[
 S_i\subset X_i\supset S_{i+1},
 \qquad \phi(X_i)=S_i.
\tag{8.3}
\]

The flag \(\phi(X_i)=S_i\) belongs to the edge from \(X_i\) to
\(X_{i-1}\), not to the oppositely oriented edge.  We therefore orient the
contracted owner cycle as

\[
 e_i:X_i\longrightarrow X_{i-1}.
\tag{8.3a}
\]

There are unique transition symbols \(p_i\in X_i\) and
\(q_i\notin X_i\) such that

\[
 X_{i-1}=X_i-\{p_i\}+\{q_i\}.
\tag{8.4}
\]

Then

\[
 \phi(X_i)=S_i=X_i-\{p_i\}=X_i\cap X_{i-1}.
\tag{8.4a}
\]

This orientation point is essential.  The abstract child
\(S_i\cap S_{i+1}\) studied in the omitted-owner audit uses the two facets
incident with the same owner \(X_i\).  It is not the forward durable child
of the AH flag \(L_1(X_i)=S_i\); that child is governed by
\(S_i\cap S_{i-1}\).

Fix any one of the integral core flag resolutions from AH Theorem 1.1 and
define its deletion symbols by

\[
 a_{i,s}
 :=L_{s-1}(X_i)\setminus L_s(X_i),
 \qquad1\le s\le H.
\tag{8.5}
\]

Thus

\[
 a_{i,1}=p_i.
\tag{8.6}
\]

### Lemma 8.1 (one-edge deletion-symbol criterion)

Suppose the directed edge \(X_i\to X_{i-1}\) satisfies the lower durable
intersection identities through levels \(0,1,\ldots,s-1\), where
\(1\le s<H\).  Then it also satisfies the identity at level \(s\) if and
only if

\[
 \boxed{a_{i,s+1}=a_{i-1,s}.}
\tag{8.7}
\]

#### Proof

Put

\[
 A=L_s(X_i),\qquad B=L_s(X_{i-1}),
 \qquad b=a_{i-1,s}.
\]

The identity at level \(s-1\) gives

\[
 A=L_{s-1}(X_i)\cap L_{s-1}(X_{i-1})
 \subseteq L_{s-1}(X_{i-1})=B\cup\{b\}.
\tag{8.8}
\]

The sets \(A,B\) have the same rank.  If the identity at level \(s\)
holds, then \(A\cap B=L_{s+1}(X_i)\) has rank \(|A|-1\).  Hence
\(A\setminus B=\{b\}\), and the element deleted from \(A\) is \(b\),
which is (8.7).

Conversely, (8.7) says \(b\in A\).  Equation (8.8) and equal cardinality
then give \(A\setminus B=\{b\}\).  Therefore

\[
 L_{s+1}(X_i)=A-\{b\}=A\cap B,
\]

which is the identity at level \(s\). \(\square\)

No injectivity of \(L_s\) was used.  The criterion therefore applies to
the repeated core fibres of AH Theorem 1.1.

### Theorem 8.2 (exact core lower rotor-run count)

For a fixed nested core resolution define

\[
 \mathcal B_H^-(L)
 =\left\{i\in\mathbb Z_M:
 \exists\,1\le s<H\text{ with }
 a_{i,s+1}\ne a_{i-1,s}\right\}.
\tag{8.9}
\]

For \(1\le s<H\), its first-failure layers are

\[
 \begin{aligned}
 \mathcal B_s^-(L)=\{i:{}&
 a_{i,t+1}=a_{i-1,t}\quad(1\le t<s),\\
 &a_{i,s+1}\ne a_{i-1,s}\}.
 \end{aligned}
\tag{8.10}
\]

Then the sets in (8.10) are disjoint and

\[
 \boxed{
 |\mathcal B_H^-(L)|
 =\sum_{s=1}^{H-1}|\mathcal B_s^-(L)|.}
\tag{8.11}
\]

Cutting exactly the edges in \(\mathcal B_H^-(L)\) partitions the core
cycle into the minimum number

\[
 \boxed{
 P_H^-(L)=\max\{1,|\mathcal B_H^-(L)|\}}
\tag{8.12}
\]

of directed pieces on which every lower core flag is transported through
depth \(H\).  If one first linearizes the cycle by optimally deleting one
edge, the remaining lower nondurable-edge count is

\[
 \boxed{
 K_{H,\mathrm{path}}^-(L)
 =\bigl(|\mathcal B_H^-(L)|-1\bigr)_+.}
\tag{8.13}
\]

Consequently the sharp lower-symbol estimate required to fuse the core with
\(o(W)\) reset cost is

\[
 \boxed{
 \min_L|\mathcal B_H^-(L)|=o(W/H),}
\tag{8.14}
\]

where the minimum is over the balanced integral nested core resolutions of
AH Theorem 1.1.  Equivalently, one must minimize the **union** of mismatch
positions, not the sum of all mismatches over depths.

#### Proof

Lemma 8.1 shows that an edge transports the full lower flag through depth
\(H\) exactly when it is outside (8.9).  Every bad edge has a unique first
failure, proving (8.11).  Deleting \(b>0\) edges from one directed cycle
gives exactly \(b\) path components; if \(b=0\), one structural cut is
still needed.  This proves (8.12).  The structural cut may be chosen at one
bad edge when one exists, giving (8.13).  In any physical completion of
these lower-compatible pieces, the useful lower prefix costs \(O(H)\) per
piece, so (8.14) is the exact lower-side asymptotic target. \(\square\)

Corollary 1.2 of the AH report proves that the feasible set in (8.14) is
nonempty and that every one of its resolutions has acceptable marginal
weighted spill after adjoining the omitted owners.  It gives no estimate
on (8.9): its integral flow paths are chosen by target capacities, with no
constraint linking owner \(X_i\)'s \((s+1)\)-st deletion to owner
\(X_{i+1}\)'s \(s\)-th deletion.

If all equalities in (8.7) hold, induction gives the exact diagonal law

\[
 \boxed{a_{i,s}=p_{i-s+1}}
 \qquad(1\le s\le H),
\tag{8.15}
\]

and hence

\[
 L_s(X_i)
 =X_i\setminus\{p_i,p_{i-1},\ldots,p_{i-s+1}\}
 =\bigcap_{t=0}^{s}X_{i-t}.
\tag{8.16}
\]

Thus (8.14) is exactly a tight-window condition, not a marginal load
condition.

### 8.3 The sharp depth-two instance

The core-total ratio and high-slot count are exactly

\[
 \frac{M}{N_2}=\frac{m+3}{m-1},\qquad
 M-N_2=\frac{4M}{m+3}.
\tag{8.16a}
\]

Thus for \(m\ge6\) the AH core capacities at depth two are one or two,
with exactly \(M-N_2\) high targets.  These are core-total capacities, not
the original \(W\)-owner high set used for the omitted-owner spill.

At depth two, (8.7) becomes

\[
 \boxed{a_{i,2}=p_{i-1}.}
\tag{8.17}
\]

The desired deletion is even locally available exactly when

\[
 p_{i-1}\in L_1(X_i)=X_i-\{p_i\}.
\]

Using (8.4), this is equivalent to

\[
 \boxed{p_{i-1}\ne q_i.}
\tag{8.18}
\]

Thus every positive coordinate run of length one is an unavoidable
depth-two mismatch.

For the saturating Boolean cycle, this local obstruction is actually absent.
The two sets \(S_i\) and \(S_{i-1}\) are distinct rank-\((m-1)\) facets of
\(X_{i-1}\).  If \(p_{i-1}=q_i\), then deleting \(q_i\) from
\(X_{i-1}=S_i\cup\{q_i\}\) would give \(S_{i-1}=S_i\), contrary to the
fact that all \(S_j\)'s are distinct.  Hence

\[
 \rho_1^+=0
 \quad\text{and}\quad
 S_i-\{p_{i-1}\}=S_i\cap S_{i-1}
 \quad\text{for every }i.
\tag{8.18a}
\]

The cyclic histogram of these forward durable children is the same, after
an index shift/reversal, as the natural histogram in Section 8 of the
omitted-owner audit:

\[
 h(T)=|\{i:S_i\cap S_{i-1}=T\}|.
\tag{8.18b}
\]

The exact optimum is a finite integral min-cost flow.  Its left vertices
are the cycle owners \(X_i\); its right vertices are
\(V_2=\binom{[n]}{m-2}\), with the balanced lower and upper integer bounds
on each target prescribed in AH Theorem 1.1.  Join \(i\) to \(T\) when

\[
 T\subset L_1(X_i),\qquad |T|=m-2,
\]

and give this arc cost zero exactly when

\[
 T=L_1(X_i)-\{p_{i-1}\};
\tag{8.19}
\]

all other arcs have cost one.  Allow each right vertex its balanced
capacity \(1\) or \(2\), with exactly \(M-N_2\) high vertices.  Network
integrality and AH Theorem 1.1 imply feasibility, and its minimum cost is

\[
 \boxed{
 \beta_2^-=\min_{L_2}
 \left|\{i:a_{i,2}\ne p_{i-1}\}\right|.}
\tag{8.20}
\]

Therefore

\[
 P_2^- =\max\{1,\beta_2^-\},\qquad
 K_{2,\mathrm{path}}^-=(\beta_2^--1)_+.
\tag{8.21}
\]

Let

\[
 \rho_1^+=|\{i:p_{i-1}=q_i\}|,
\tag{8.22}
\]

and, on the eligible indices, let

\[
 \mu_2(T)=
 |\{i:p_{i-1}\ne q_i,\
 L_1(X_i)-\{p_{i-1}\}=T\}|.
\tag{8.23}
\]

For every balanced core quota vector \(b_2\),

\[
 \boxed{
 \beta_2^-
 \ge \rho_1^+
 +\sum_T(\mu_2(T)-b_2(T))_+.}
\tag{8.24}
\]

Minimizing the right side over balanced \(b_2\) gives the sharp elementary
run-plus-overflow lower bound.  Equality is not asserted: after fixing all
zero-cost assignments below capacity, the remaining incidence graph can
still fail Hall.  The min-cost flow (8.20), not the scalar overload alone,
is the exact test.

#### Proof of (8.18) and (8.24)

The set \(X_{i-1}\) consists of \(X_i-\{p_i\}\) together with the one new
symbol \(q_i\).  Since \(p_{i-1}\in X_{i-1}\), it lies in
\(X_i-\{p_i\}\) exactly when it is not \(q_i\), proving (8.18).  Every
ineligible index must pay cost one.  Among eligible indices, at most
\(b_2(T)\) natural assignments to target \(T\) can be retained, so at least
\((\mu_2(T)-b_2(T))_+\) of them must change.  These owner sets are disjoint,
giving (8.24). \(\square\)

The core-total min-cost flow (8.20) is useful when one insists on the
balanced core resolution of AH Theorem 1.1.  For physical fusion, the
omitted owners may instead absorb the natural core imbalance.  The exact
full-owner test is sharper.

### Proposition 8.3 (zero-mismatch full-owner depth-two cut)

Let \(H_1\subseteq V_1\), \(|H_1|=d=W-M\), be the image of an omitted-owner
SDR, so that the depth-one full load is one everywhere and two on \(H_1\).
For \(m\ge8\), let \(H_2\subseteq V_2\) have the forced size

\[
 |H_2|=W-N_2.
\tag{8.24a}
\]

All core cycle edges can retain their natural lower durable child through
depth two, while the omitted owners complete an exactly balanced full load,
if and only if

\[
 \boxed{h(T)\le1+\mathbf1_{H_2}(T)\quad(T\in V_2)}
\tag{8.24b}
\]

and

\[
 \boxed{
 |H_1\cap N(\mathcal A)|
 \ge |\mathcal A|+|H_2\cap\mathcal A|-h(\mathcal A)
 \quad(\mathcal A\subseteq V_2).}
\tag{8.24c}
\]

Here \(N(\mathcal A)\subseteq V_1\) is the family of immediate parents of
\(\mathcal A\), and \(h(\mathcal A)=\sum_{T\in\mathcal A}h(T)\).
When (8.24b)--(8.24c) hold, the exact lower core mismatch count at depth two
is zero.

#### Proof

Pin the core child of \(X_i\) to \(S_i\cap S_{i-1}\).  The desired full
depth-two load is

\[
 b_2(T)=1+\mathbf1_{H_2}(T).
\]

The residual demand to be carried by the \(d\) omitted-owner tokens is

\[
 r_2(T)=b_2(T)-h(T).
\tag{8.24d}
\]

Nonnegativity of every residual demand is exactly (8.24b).  Moreover

\[
 \sum_T r_2(T)=W-M=d.
\]

The omitted tokens have current parent set \(H_1\).  Clone child \(T\)
exactly \(r_2(T)\) times.  Hall's condition for matching the \(H_1\)
tokens to all clones is precisely (8.24c).  Such a matching gives the
required nested omitted-owner children.  Conversely, every completion
supplies this matching, so both conditions are necessary.  The pinned core
children obey (8.17) at every edge, hence create no lower first failure.
\(\square\)

Equivalently, without requiring zero mismatch, form the full token
min-cost flow from the depth-one owner tokens to \(V_2\): give a core token
cost zero only on its natural child \(S_i\cap S_{i-1}\), give it cost one
on every other facet, and give every omitted token cost zero.  Impose the
full balanced target capacities \(1\) or \(2\).  Its integral optimum
\(\widehat\beta_2^-\) is the exact minimum number of lower core cycle edges
which first fail at depth two.  Proposition 8.3 says

\[
 \widehat\beta_2^-=0
 \quad\Longleftrightarrow\quad
 \text{there are }H_1,H_2\text{ satisfying (8.24b)--(8.24c).}
\tag{8.24e}
\]

The corrected omitted-owner theorem proves feasibility of the uncosted
flow, by allowing arbitrary rerouting of core tokens.  It does not bound
\(\widehat\beta_2^-\), and it does not verify (8.24b)--(8.24c) for the
natural durable children.

### 8.4 Iterated directly testable estimate and two-sided scope

For each \(1\le s<H\), define the raw mismatch set

\[
 D_s^-(L)=\{i:a_{i,s+1}\ne a_{i-1,s}\}.
\tag{8.25}
\]

Then the exact growing-depth target is

\[
 \boxed{
 \min_L\left|\bigcup_{s=1}^{H-1}D_s^-(L)\right|
 =o(W/H).}
\tag{8.26}
\]

The stronger but nonsharp estimate

\[
 \sum_{s=1}^{H-1}|D_s^-(L)|=o(W/H)
\tag{8.27}
\]

would suffice.  The union in (8.26) is correct because an edge is paid only
at its first failure.  Corollary 1.2 bounds neither expression.

Finally, (8.26) is only a **lower-side** rotor-run statistic.  A genuine
two-sided durable system would also require upper-complement flags
\(R_s\).  If

\[
 u_{i,s}=R_{s-1}(X_i)\setminus R_s(X_i),
\]

then the correctly oriented upper shift along \(X_i\to X_{i-1}\) is

\[
 \boxed{u_{i-1,s+1}=u_{i,s}.}
\tag{8.28}
\]

The true two-sided bad-edge set is the union of the failures in (8.7) and
(8.28).  The AH construction supplies no such upper family.  Moreover its
core maps have repeated fibres, whereas AD9 uses active bijections.  Hence
even a proof of (8.26) would give a fused physical lower core with small
reset cost, not an AD9 instantiation or a full symmetric-band literal word.

The \(d=O(W/m)\) omitted-owner flags in Corollary 1.2 may be initialized
separately at cost \(O(Hd)=O_A(W/\sqrt m)=o(W)\).  The unresolved cost is
the \(M=(1-o(1))W\) cycle core, measured exactly by (8.26), together with
the absent upper counterpart.

## 9. Exact proved/conditional boundary

### Proved

1. The current q=1 saturating-cycle inputs are one-sided and do not
   instantiate AD9.
2. AH Corollary 1.2 proves full-owner lower marginal integrality, nesting,
   coverage, and weighted overload \(o(W)\), but not cycle chronology.
3. With selectable lifetimes, integral two-sided active flags always exist
   through every depth (Theorem 2.1).
4. Their lifetime-change edges in any fixed path forest satisfy the exact
   bound (2.9).
5. Arbitrary-lifetime durable flags literalize with the exact component
   ledger (3.1)--(3.2).
6. The even saturating cycle has the exact q=1 deletion/Hall statistic
   (4.5), and its uncontrolled lower support gives the necessary estimate
   (4.8).
7. After hypothetical q=1 bi-saturation, the first physical depth-two
   failure number is exactly (5.7), with paired matching obstruction (5.8).
8. Hypothetical two-sided depth-two support saturation gives the sharp raw
   paired-collision budget (6.3).
9. For the odd AH core, the exact lower rotor-run count is the union of
   deletion-symbol mismatch positions (8.9)--(8.14); depth two is the
   min-cost flow (8.20), with exact run-plus-overflow lower bound (8.24).
10. Allowing the omitted owners to absorb the natural core imbalance gives
    the exact zero-mismatch depth-two cuts (8.24b)--(8.24c), and the general
    exact cost is the full token flow \(\widehat\beta_2^-\).

### Unproved

1. A saturating cycle with

   \[
   \kappa_1=o_A(W/H)
   \]

   on the even q=1 active owner set.
2. The two depth-two support equalities (6.1)--(6.2) for the same cycle.
3. Boundary Hall for a deletion set of size \(o(W/H)\), on both signs and
   recursively.
4. A recursively compatible sequence with total first-failure count

   \[
   K_H=o_A(W/H)
   \]

   on a Gaussian window.
5. For the odd AH core, the deletion-symbol estimate (8.26), and any
   upper-complement flag family satisfying the reverse shift (8.28).

The precise new target is therefore not another abstract nested-flow
extension.  It is a labelled edge-distribution theorem: select common active
owners and endpoint matchings so that the paired forced-colour graph loses
only \(o(W/H)\) actual cycle/forest edges, while its terminal and source
holes pass the two integral Hall systems.
