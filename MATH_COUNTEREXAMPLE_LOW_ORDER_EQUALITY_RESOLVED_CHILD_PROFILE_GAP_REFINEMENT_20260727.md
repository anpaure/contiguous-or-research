# Low-order equality-resolved CPS fails: internal interval gaps are mass-preserving

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or
external input is used.

## 0. Verdict

Let

\[
 n=2m,\qquad M=m+H,\qquad r=M+1,\qquad 3\le H=o(m),
\]

and let an ordinary promotion frame consist of one rank-\(M\) top and
the \(M\) rank-\(m\) owners obtained by complementing the cyclic
\(H\)-intervals of an order on that top. Write

\[
 D_O={m!^2\over(m-H)!}.
\]

Let \(D_{\rm ref}\) be the common initial reference degree used in the
stochastic profile hierarchy, and put

\[
 q_k(S)={d_0(S)\over D_{\rm ref}},
 \qquad
 \widehat q_k(S)={d_0(S)\over D_O}.
\tag{0.0}
\]

The two normalizations differ by one common factor. Every child/parent
ratio and every CPS contradiction below is therefore identical for
\(q\) and \(\widehat q\). Absolute rooted counts are displayed using
\(\widehat q\).

The proposed equality-resolved child estimate

\[
 \sum_{T\in\mathscr C(S)}q_{k+1}(T)
 \le {C\over m}q_k(S),
 \qquad 2\le k<H,
\tag{CPS\(_{<H}\)}
\]

is false, already at \(k=2\), for the written column--row child
relation. Its unweighted compensation analogue is also false if actual
external owner coins are included as children. If “compensation child”
means only a duplicated formal prefix/row occurrence, complete
physical-union resolution removes that formal positive term instead.

The obstruction is an internal gap refinement. If two checkpoint
owners leave a gap of length \(g\ge2\), inserting a checkpoint which
splits that gap into \(a\) and \(g-a\) has the exact componentwise ratio

\[
 \boxed{
 {q_{\rm child}\over q_{\rm parent}}
 =\left({a!(g-a)!\over g!}\right)^2
 =\binom ga^{-2}.}
\tag{0.1}
\]

There are \(\binom ga^2\) physical intermediate owners, and within
each resolved shore-signing component their child links partition the
parent component. Therefore

\[
 \boxed{
 \sum_{\text{complete split-}a\text{ orbit}}q_{\rm child}
 =q_{\rm parent}.}
\tag{0.2}
\]

For \(g=2,a=1\), four distinct children each carry one quarter of the
parent mass. One parent-disjoint event frame can contain three of the
four, giving

\[
 \sum_{T\in\mathscr C(S)}q_3(T)\ge {3\over4}q_2(S).
\tag{0.3}
\]

The failure persists for every \(2\le k<H\), and even in a hierarchy
seeded only by distance-one owner pairs. Equality resolution does not
remove it: all displayed resources are distinct, and the common
column--row resource is counted exactly once.

The consecutive spine is consequently not worst among all children.
It is the gap-free case and has no internal refinements. Among
**outward span extensions which remain below the geometric boundary**,
the one-step continuation has the largest pointwise ratio. For such an
extension by \(h\ge1\), with
\(\ell+h<H\), the exact ratio is

\[
                         \binom{m-\ell}{h}^{-2},
\tag{0.4}
\]

where \(\ell<H\) is the current total signed span. Summing outward
children over one frame does give \(O(q(S)/m)\).

Thus the minimum viable replacement must retain the interval-gap
geometry. Internal refinements are mass-preserving conditional
partitions; only span-increasing children contract. A cutoff indexed
only by the cardinality \(k=|S|\) cannot be correct.

## 1. Exact rooted checkpoint count

Fix an owner \(X\). A frame through \(X\), rooted at the boundary of
the missing \(H\)-interval, has the unique description

\[
 (x_1,\ldots,x_m;\ a_1,\ldots,a_H),
\tag{1.1}
\]

where the \(x_i\)'s order \(X\), while
\((a_1,\ldots,a_H)\) is an ordered \(H\)-tuple of distinct labels from
\([2m]\setminus X\). Its top is

\[
                         U=X\cup\{a_1,\ldots,a_H\}.
\]

There are

\[
                         m!(m)_H={m!^2\over(m-H)!}=D_O
\tag{1.2}
\]

such rooted frames.

On the positive shore define

\[
 X_j^+
 =X\setminus\{x_1,\ldots,x_j\}
   \cup\{a_1,\ldots,a_j\},
 \qquad 1\le j<H.
\tag{1.3}
\]

There is an analogous negative-shore family using suffixes of the two
orders. Every owner at Johnson distance \(j<H\) from \(X\) in the
frame is represented on exactly one of these two shores.

Fix one sign-resolved checkpoint chain at distances

\[
 0=d_0<d_1<\cdots<d_s=\ell<H,
\qquad
 g_i=d_i-d_{i-1}.
\tag{1.4}
\]

The physical loss and entry sets at every checkpoint are fixed. Within
the \(i\)-th gap, the \(g_i\) loss labels and the \(g_i\) entry labels
may each be ordered arbitrarily. After the last checkpoint, the
remaining labels are free. Hence the exact number of rooted frames in
this one shore assignment is

\[
 \boxed{
 d_0^{\rm or}(S)
 ={(m-\ell)!^2\over(m-H)!}
   \prod_{i=1}^s(g_i!)^2.}
\tag{1.5}
\]

Equivalently,

\[
 \boxed{
 \widehat q^{\rm or}(S)
 =\left[
 {(m-\ell)!\prod_i g_i!\over m!}
 \right]^2.}
\tag{1.6}
\]

Write \(q^{\rm or}=(D_O/D_{\rm ref})\widehat q^{\rm or}\) for the
same oriented component in the hierarchy's reference normalization.

Indeed, on the \(X\)-side there are
\((m-\ell)!\prod_i g_i!\) orders. On the outside side there are

\[
 { (m-\ell)!\over(m-H)!}\prod_i g_i!
\]

ordered \(H\)-tuples. Multiplication proves (1.5).

For a physical monotone chain the positive- and negative-shore
assignments are disjoint and contribute equally, giving twice (1.5).
Splitting those signings into separate equality types does not change
any ratio below.

## 2. The exact internal-gap partition law

Suppose a gap \(g\) in (1.4) is split at \(a\), where
\(1\le a<g\). In (1.5), the factor \(g!\) on each of the two label
orders is replaced by \(a!(g-a)!\). The total span \(\ell\) does not
change. Therefore

\[
 {d_0^{\rm or}(S\cup\{Y\})\over d_0^{\rm or}(S)}
 =
 \left({a!(g-a)!\over g!}\right)^2
 =\binom ga^{-2}.
\tag{2.1}
\]

To choose the physical intermediate owner \(Y\), independently choose
which \(a\) of the \(g\) loss labels and which \(a\) of the \(g\)
entry labels have appeared. There are exactly
\(\binom ga^2\) choices.

Every rooted frame in the parent link has one unique phase-\(a\)
intermediate owner. Thus the child links are pairwise disjoint and
exhaust the parent link. Summing (2.1) proves (0.2).

This is a physical partition identity, not a formal multiplicity
estimate. In particular, ordered-history multiplicities cannot turn
it into a contraction.

## 3. A counterexample at every order below \(H\)

Choose distinct labels

\[
 x_1,\ldots,x_k\in X,
 \qquad
 a_1,\ldots,a_k\in[2m]\setminus X,
\]

and put

\[
 Z_j
 =X\setminus\{x_1,\ldots,x_j\}
   \cup\{a_1,\ldots,a_j\}.
\tag{3.1}
\]

For every \(2\le k<H\), define

\[
                         S_k=\{X,Z_2,Z_3,\ldots,Z_k\},
 \qquad Y=Z_1.
\tag{3.2}
\]

The parent checkpoint gaps are \(2,1,\ldots,1\), with total span \(k\).
There are exactly two shore signings. Formula (1.5) gives

\[
 \boxed{
 d_0(S_k)={8(m-k)!^2\over(m-H)!},
 \qquad
 \widehat q_k(S_k)={8\over(m)_k^2}.}
\tag{3.3}
\]

After inserting \(Y\), all \(k\) gaps are one, so

\[
 \boxed{
 d_0(S_k\cup\{Y\})={2(m-k)!^2\over(m-H)!},
 \qquad
 \widehat q_{k+1}(S_k\cup\{Y\})={2\over(m)_k^2}.}
\tag{3.4}
\]

Consequently

\[
 \boxed{
 q_{k+1}(S_k\cup\{Y\})={1\over4}q_k(S_k).}
\tag{3.5}
\]

### Lemma 3.1 (a parent-disjoint event row exists)

There is an ordinary frame \(G\) containing \(Y\) but no member of
\(S_k\).

#### Proof

For owners \(A,B\) at Johnson distance \(d<H\), the exact pair ratio is

\[
                         {d_0(A,B)\over D_O}
 ={2\over\binom md^2}.
\tag{3.6}
\]

Every member of \(S_k\) is at a positive distance below \(H\) from
\(Y=Z_1\). Hence the fraction of \(Y\)-frames containing at least one
member of \(S_k\) is at most

\[
 \sum_{W\in S_k}{d_0(Y,W)\over D_O}
 \le {2k\over m^2}<1
\tag{3.7}
\]

for all sufficiently large \(m\). Some \(Y\)-frame avoids \(S_k\).
\(\square\)

There is also a clean equality version. Fix one witness frame \(R\)
through \(S_k\cup\{Y\}\). Among all \(Y\)-frames, the fraction sharing
another resource with \(R\) is at most

\[
 4\sum_{d=1}^{H-1}\binom md^{-2}
 +(m-H+1)^2\binom mH^{-2}
 +\binom mH^{-1}
 =O(m^{-2})<1.
\tag{3.8}
\]

The first term counts the two owners of \(R\) at each distance
\(d<H\), the second the distance-\(H\) plateau, and the last the top of
\(R\). Thus \(G\) may be chosen with

\[
                         V(G)\cap V(R)=\{Y\}.
\tag{3.9}
\]

For the written column--row child relation, \(G\cap S_k=\varnothing\)
and \(Y\) is a genuinely new equality-resolved physical resource.
Therefore

\[
 \sum_{T\in\mathscr C_G(S_k)}q_{k+1}(T)
 \ge q_{k+1}(S_k\cup\{Y\})
 ={1\over4}q_k(S_k),
\tag{3.10}
\]

contradicting (CPS\(_{<H}\)) for every fixed \(C\) and all sufficiently
large \(m\).

## 4. An explicit \(3/4\) column--row obstruction at order two

The preceding existence argument can be made completely explicit.
Choose distinct

\[
 x_1,x_2\in X,\qquad a_1,a_2\notin X,
\]

and put

\[
 Z=X\setminus\{x_1,x_2\}\cup\{a_1,a_2\},
 \qquad
 Y_{ij}=X\setminus\{x_i\}\cup\{a_j\}.
\tag{4.1}
\]

By (2.1),

\[
                         q_3(X,Z,Y_{ij})
 ={1\over4}q_2(X,Z)
\tag{4.2}
\]

for all four pairs \((i,j)\).

Choose an \((H-2)\)-set

\[
 R_0\subseteq[2m]\setminus
       (X\cup\{a_1,a_2\}),
\]

fix an arbitrary order of \(R_0\), put
\(V=X\cup\{a_1,a_2\}\cup R_0\), and take a cyclic order beginning

\[
                         a_2,\ x_1,\ R_0,\ a_1,\ x_2,
                         \ X\setminus\{x_1,x_2\}.
\tag{4.3}
\]

Its first three cyclic \(H\)-intervals are

\[
 R_0\cup\{a_2,x_1\},\qquad
 R_0\cup\{x_1,a_1\},\qquad
 R_0\cup\{a_1,x_2\}.
\tag{4.4}
\]

Their complementary owners are \(Y_{11},Y_{12},Y_{22}\).
The only \(H\)-intervals containing all of the consecutive
\((H-2)\)-block \(R_0\) are the three intervals in (4.4). Therefore
this event frame contains neither \(X\), whose complementary block is
\(R_0\cup\{a_1,a_2\}\), nor \(Z\), whose complementary block is
\(R_0\cup\{x_1,x_2\}\).

It follows that this one parent-disjoint frame contributes

\[
 \boxed{
 \sum_{T\in\mathscr C_G(X,Z)}q_3(T)
 \ge {3\over4}q_2(X,Z).}
\tag{4.5}
\]

There is no first-new-resource overcount in (4.5). Every frame through
the distance-two pair \(X,Z\) has a unique cyclic start strictly between
their two starts, hence exactly one of the four \(Y_{ij}\)'s as its
internal midpoint. The four child links therefore partition the parent
link. The three midpoint resources in \(G\) meet three disjoint
parent-row classes of total mass \(3q_2(X,Z)/4\), even after complete
equality subdivision.

The constant \(3/4\) is sharp for this internal square in one event
row. The four \(Y_{ij}\)'s induce a \(C_4\) in the Johnson graph. In
one cyclic owner deck with \(M>4\), distance-one owner pairs correspond
to adjacent cyclic starts, and the start cycle \(C_M\) contains no
\(C_4\). Hence at most three of the four can occur in one row; (4.3)
attains three.

## 5. Complete equality and boundary audit

The counterexample survives all relevant equality conventions.

1. **Existing-resource equality.**  
   The child \(Y\) is not in \(S_k\), and the event frame is disjoint
   from \(S_k\). Thus the physical profile order really increases from
   \(k\) to \(k+1\).

2. **Column--row equality.**  
   The occurrence of \(Y\) in the event column and parent row is the
   one new physical resource being exposed. Equality resolution counts
   it once; it does not cancel it.

3. **Same-parent and multiple-intersection patterns.**  
   Equation (3.9) gives a witness with exactly one column--row equality.
   If the full child orbit is subdivided according to further physical
   equalities, the nonnegative pieces still sum to
   \(q_{k+1}(S_k\cup\{Y\})\).

4. **Two shore orientations.**  
   The positive and negative rooted signings are disjoint. Each
   separately has ratio \(1/4\), so resolving them cannot help.

5. **Rotation, reversal, and simple quotients.**  
   These divide parent and child counts by the same stabilizer factor.

6. **Top equality.**  
   The all-\(k\) example uses total span \(k<H\), so at least
   \(H-k\) top coordinates remain free. No top is forced. If forced
   top children are admitted without first closing the parent profile,
   there is an additional simpler failure: owners at distance \(H\)
   force the top \(X\cup Z\), giving child ratio one.

7. **The \(k=H\) boundary.**  
   The obstruction never uses \(k=H\) or a post-\(H\) profile. It
   occurs for every \(2\le k<H\), exactly in the proposed contracting
   range.

8. **Ordered histories.**  
   Retaining factorial ordered multiplicities repeats nonnegative child
   mass and cannot change (3.5) into an \(m^{-1}\) bound.

Thus this is an equality-resolved pre-boundary obstruction, rather than
an artefact of the terminal \(H\)-level.

## 6. Distance-one seeds and iteration

Restricting order-two roots to distance-one pairs does not repair the
hierarchy. For \(3\le k<H\), define

\[
 S'_k=\{X,Z_1,Z_3,Z_4,\ldots,Z_k\}.
\tag{6.1}
\]

It has \(k\) resources and checkpoint gaps \(1,2,1,\ldots,1\).
Inserting \(Z_2\) again splits the unique gap of size two, so

\[
                         q_{k+1}(S'_k\cup\{Z_2\})
 ={1\over4}q_k(S'_k).
\tag{6.2}
\]

The profile appears in the ordered-profile tower from the distance-one
seed \(\{X,Z_1\}\) by first adjoining \(Z_3\), followed by the outward
checkpoints. If literal parent-disjoint event rows are required at every
step, the pair-codegree union bound in Lemma 3.1 supplies them
successively. Thus the unrestricted third-resource diffusion estimate
cannot be iterated from distance-one roots without retaining the gap
state.

More generally, begin with endpoints at distance \(d=H-1\). At any
unfilled phase \(j\), (0.2) gives a mass-preserving complete global
refinement orbit. After fixing one intermediate, each remaining subgap
has the same partition identity. Hence a noncontracting global
interpolation tree persists through profile orders \(2,\ldots,H-1\).
This does not assert that one fixed event row captures the whole orbit
at every level; the fixed-row constant capture needed to refute CPS is
already supplied by the gap-two construction.

## 7. Compensation children

For the unweighted compensation child relation written in
(CPS\(_{<H}\)), the same owner \(Y\) gives

\[
                         q_{k+1}(S_k\cup\{Y\})
 ={1\over4}q_k(S_k),
\]

and the complete split orbit has total mass \(q_k(S_k)\). Complete
physical equality resolution records this common resource once rather
than erasing it.

There are two possible intended dynamic meanings, and they must be
distinguished.

* If a “compensation child” is only a duplicated formal occurrence of a
  resource already present in the prefix/last-row union, complete
  physical-union resolution makes that formal overcount zero.

* If it is the actual external compensation clock of an active child
  owner \(Y\), before the degree/quarantine stop retain its rate

  \[
  0\le\chi_t(Y)={\Delta_t-d_t(Y)\over r\Delta_t}\le {1\over r}.
  \tag{7.1}
  \]

  Then the mass-preserving identity (0.2) gives the valid rate-aware
  estimate

  \[
  \boxed{
  \sum_{Y\text{ in a complete internal split orbit}}
       \chi_t(Y)q_{k+1}(S\cup\{Y\})
  \le {1\over r}q_k(S)
  =O\!\left({q_k(S)\over m}\right).}
  \tag{7.2}
  \]

  Here \(0\le d_t(Y)\le\Delta_t\). Moreover, vertex-induced deletion
  preserves the partition identity dynamically:

  \[
  \sum_{Y\text{ in the complete split orbit}}d_t(S\cup\{Y\})
  =d_t(S).
  \tag{7.3}
  \]

  Thus the corresponding first-moment coin hazard is at most
  \(d_t(S)/r\). This identity alone does not control a quadratic-
  variation or higher-power term.

Thus compensation does not require the false unweighted CPS. It either
vanishes after physical-union resolution or is controlled by its actual
clock. The parent-disjoint selected-edge column--row obstruction in
Sections 3--4 remains.

## 8. The strongest surviving contraction theorem

There is an exact positive statement after internal refinements are
separated.

### Theorem 8.1 (outward span extensions contract)

Fix one sign-resolved checkpoint orbit with total signed span
\(\ell<H\), arbitrary internal gap vector, and positive time-zero mass.
If a new owner extends one shore outward by \(h\ge1\), without splitting
an existing gap, and \(\ell+h<H\), then

\[
 \boxed{
 {q^{\rm or}_{\rm child}\over q^{\rm or}_{\rm parent}}
 =\binom{m-\ell}{h}^{-2}.}
\tag{8.1}
\]

If instead a compatible top is fixed, its conditional ratio is

\[
 \boxed{
 {q^{\rm or}_{\rm top\ child}\over q^{\rm or}_{\rm parent}}
 ={1\over\binom{m-\ell}{H-\ell}}.}
\tag{8.2}
\]

Consequently, for every event frame \(G\),

\[
 \boxed{
 \sum_{\substack{\text{outward owner children in }G\\
                  \ell+h<H}}
 q^{\rm or}_{\rm child}
 +\mathbf 1_{\{\text{the top of }G\text{ is compatible and nonforced}\}}
  q^{\rm or}_{\rm top\ child}
 \le {C\over m}q^{\rm or}_{\rm parent}.}
\tag{8.3}
\]

#### Proof

In (1.5), an outward extension by \(h\) replaces \(\ell\) by
\(\ell+h\) and adds one terminal gap factor \(h!\). Hence

\[
 {q^{\rm or}_{\rm child}\over q^{\rm or}_{\rm parent}}
 =\left({(m-\ell-h)!h!\over(m-\ell)!}\right)^2
 =\binom{m-\ell}{h}^{-2}.
\]

For a fixed top, the remaining \(H-\ell\) exterior labels are chosen
from \(m-\ell\) possibilities. Conditioning on their set costs
\(\binom{m-\ell}{H-\ell}^{-1}\), proving (8.2).

The owner ratio in (8.1) is maximized at \(h=1\), and is
at most \(C/m^2\) because \(\ell<H=o(m)\). One event frame has at most
\(M=O(m)\) owner resources. The top ratio is at most \(C/m\), with
equality in order only when \(H-\ell=1\). There is one top resource.
Summation proves (8.3). \(\square\)

Thus \(h=1\) has the largest pointwise outward ratio, and the complete
outward row sum is \(O(1/m)\). Internal interpolation is a different
orbit and is noncontracting.

## 9. Consequences for the finite-\(H\) reduction

The following claims cannot be used as currently stated.

1. The unrestricted fixed-third-resource and one-frame fibre estimates
   in MATH_THEOREM_PAIR_PROFILE_STOP_UNDER_TRIPLE_FIBRE_AND_NEXT_BOUNDARY_20260727.md
   fail for a distance-two parent: the exact ratios are \(1/4\) and at
   least \(3/4\), rather than \(m^{-2+o(1)}\) and \(m^{-1+o(1)}\).
   Their distance-one/external-extension instances are not affected.
   Accordingly, downstream conclusions which use those lemmas for
   unrestricted profiles must be withdrawn. The separate theta
   inequality for its certified distance-one/equality-resolved input is
   not refuted here, nor are whole-arm statements explicitly conditional
   on the profile stops.

2. The hypothesis (CPS\(_{<H}\)) in
   MATH_REDUCTION_FINITE_H_PROFILE_CUTOFF_AND_NO_POST_H_BOUNDARY_20260727.md
   is false in every asserted order \(2\le k<H\).
   In particular, the reduction's statement that the unrestricted
   order-two instance is already proved is false. The all-fibre EGF
   theorem remains a valid abstract implication from CPS, but it has no
   ordinary-frame application under the stated child relation.

3. Terminating at profile cardinality \(k=H\) does not remove the
   obstruction. Internal gap refinements occur strictly below \(H\),
   and a profile with few resources can already have geometric span
   \(H\). In one sign-resolved component, the natural boundary is its
   span rather than cardinality. For mixed positive/negative shores or
   several interval components, a span vector is required; the present
   note does not prove that one scalar total span is sufficient.

Any surviving formulation needs at least the following state data:

\[
                         (\boldsymbol\ell,\ \mathcal G),
\tag{9.1}
\]

where \(\boldsymbol\ell\) records the componentwise shore spans and
\(\mathcal G\) records the gap system, resolved shore signing, and any
top-forced class. A physical profile may have several admissible
signings, which must be kept as separate conditional components.

* Splitting a gap leaves \(\boldsymbol\ell\) fixed and acts by the exact
  mass-preserving conditional kernel (0.2). It must be grouped into
  the parent state, centered, or otherwise handled without claiming an
  \(m^{-1}\) gain.
* Increasing one sign-resolved span below \(H\) is controlled by
  Theorem 8.1.
* Reaching span \(H\) in one component is a natural boundary which may
  be quarantined. The exact mixed-shore boundary remains to be derived.
* Actual compensation clocks should retain the factor \(1/r\) from
  (7.2).

These coordinates are necessary, not proved sufficient for the dynamic
generator. Proving a stopped generator/quarantine theorem after this
refinement would be a genuine replacement for CPS. No CPS-form uniform
\(O(1/m)\) scalar contraction indexed only by physical profile
cardinality can hold.

Constant one remains open.
