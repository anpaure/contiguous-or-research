# Fine strips: the natural endpoint reflection has zero frustration, but every same-frame conjugate pair has linear pair imbalance

Date: 2026-07-26

Method: pure mathematics.  No computation, search, solver, or probabilistic
claim is used.

## 0. Outcome

Fix a perfect matching

\[
 \mathcal P=\{\{a_1,b_1\},\ldots,\{a_m,b_m\}\}
\]

of the \(2m\) physical coordinates, and let \(\mathcal F\) be the canonical
dyadic fixed-pair \(C_{2h}\)-strip factor on the middle owners having at
least \(h\) split pairs.  Its omitted owner set is \(o(W)\), where

\[
                         W=\binom{2m}{m}.
\]

Let \(\rho=\prod_i(a_i\ b_i)\) be simultaneous endpoint reflection.  This
is the most immediate nontrivial coordinate symmetry of the construction.
The exact answer to the signed-packet question for the pair

\[
                         (\mathcal F,\rho\mathcal F)
\]

is as follows.

1.  The canonical factor is setwise fixed by \(\rho\).  After the two shores
    are identified by their physical strips, every overlay packet is a
    singleton strip on each shore.

2.  For any one common integral port system, the signed graph of all
    two-occurrence targets consists only of label-zero loops.  Hence

    \[
                             \boxed{\tau(G)=0}.             \tag{0.1}
    \]

    Its signs are the coboundary of the explicit constant potential
    \(x_P=0\).  Thus the signed-coboundary gate itself is completely benign
    for the natural reflection.

3.  Nevertheless the pair is unusable.  More generally, for **any two**
    strip factors whose transitions remain in the same fixed pairing
    \(\mathcal P\), and for arbitrary selected port subsets, the two-copy
    imbalance at lower depth \(q\) satisfies

    \[
      \boxed{
      \mathfrak B_{2,q}^-
       :=\sum_{T\in\binom{[2m]}{m-q}}|r_T-2|
       \ \ge\ 2D_{m,q},}                             \tag{0.2}
    \]

    where

    \[
      D_{m,q}=\sum_f(T_{f,q}-V_f)_+,
    \]

    \[
      T_{f,q}
       ={m!\,2^{m-2f-q}\over
          f!(f+q)!(m-2f-q)!},
      \qquad
      V_f
       ={m!\,2^{m-2f}\over f!^2(m-2f)!}.
                                                            \tag{0.3}
    \]

    Consequently, if \(q/\sqrt m\to c>0\), then

    \[
      \mathfrak B_{2,q}^-
       \ge
      \left(2\delta(c)+o(1)\right)W=\Omega_c(W),       \tag{0.4}
    \]

    with

    \[
      \delta(c)=e^{-c^2}\Phi(c/2)-\Phi(-3c/2)>0.       \tag{0.5}
    \]

Thus the most natural physical conjugate pair realizes alternative (i) of
the signed gate in the strongest possible form: the signs are an exact
coboundary.  It still fails the full two-shore criterion by a linear amount,
not because of frustrated cycles but because the pair-orbit occurrence
budget cannot attain two copies per target.  The conclusion applies to
endpoint shifts, pair permutations, and direction-order changes which keep
the same unordered coordinate pairing.  It does not apply to a conjugate
which changes the pairing, nor to a product-SCD-induced factor outside the
fixed-pair frame.

## 1. The canonical fixed-pair factor and endpoint reflection

In one active \(h\)-face identify middle owners with
\(V=\mathbb F_2^h\).  Put

\[
 p_0=0,
 \qquad
 p_i=e_1+\cdots+e_i\quad(1\le i\le h),
\]

and let

\[
 P=\{p_0,\ldots,p_{h-1},
          \mathbf1+p_0,\ldots,\mathbf1+p_{h-1}\}.     \tag{1.1}
\]

For dyadic \(h\), the Hamming-syndrome construction supplies a linear
subspace \(K\le V\) such that

\[
                    \{P+k:k\in K\}                   \tag{1.2}
\]

partitions \(V\) into isometric \(C_{2h}\)'s.  The direction word of every
cycle is

\[
             1,2,\ldots,h,1,2,\ldots,h.              \tag{1.3}
\]

The Stage-A factor uses (1.2) in every active \(h\)-face of every
fixed-pair occupancy cube with at least \(h\) split coordinates.  The union
of the remaining low-split occupancy cubes has size \(o(W)\).

### Lemma 1.1 (reflection invariance)

The simultaneous endpoint swap \(\rho\) preserves the good owner set and

\[
                         \rho\mathcal F=\mathcal F.    \tag{1.4}
\]

#### Proof

On a split coordinate, \(\rho\) complements its orientation bit.  It fixes
the full/empty/split status of every pair, and therefore preserves every
occupancy-cube dimension and the rule choosing the first \(h\) active split
coordinates.

On those \(h\) active coordinates it acts by translation by
\(\mathbf1\).  But (1.1) gives the exact identity

\[
                         P+\mathbf1=P.                \tag{1.5}
\]

Consequently every active cycle \(P+k\) is fixed as an unoriented cycle.
On the inactive split coordinates, \(\rho\) merely sends one fixed
orientation face to the complementary fixed orientation face.  The same
factor (1.2) is installed in every such face.  Hence physical strips are
permuted by \(\rho\), and their full collection is unchanged.  Low-split
owners are also mapped among themselves, so the common owner leave is
preserved.  This proves (1.4). \(\square\)

The same argument includes two even more degenerate symmetries: reversing
the cyclic presentation of a strip does not change the physical strip at
all, and translating an active orientation by \(\mathbf1\) is the half-turn
of that same \(C_{2h}\).

## 2. The overlay and its exact signed potential

Use two labelled shores, each equal to the physical factor \(\mathcal F\),
and use the same selected port incidences on a physical strip on the two
shores.  This is exactly what results after identifying
\(\rho\mathcal F=\mathcal F\) by Lemma 1.1.

### Lemma 2.1 (singleton overlay packets)

Every overlay packet consists of one copy of a physical strip \(C\) on
shore \(0\) and the same physical strip \(C\) on shore \(1\).

#### Proof

The middle owner supports of distinct strips of \(\mathcal F\) are
disjoint.  The two copies of \(C\) have identical support, so all of their
owner edges join one another, while no owner edge can reach another strip.
\(\square\)

Let \(k_T\) be the number of strips of one shore whose selected port edge
contains \(T\).  Across the two shores the catalogue occurrence count is

\[
                              r_T=2k_T.              \tag{2.1}
\]

### Theorem 2.2 (exact coboundary)

For every target with \(r_T=2\), its signed edge is a label-zero loop.
Consequently \(G\) is balanced and \(\tau(G)=0\).

#### Proof

Equation (2.1) shows that \(r_T=2\) exactly when \(k_T=1\).  Let \(C\) be
that unique physical strip.  The two target occurrences are then

\[
                         (P_C,0),\qquad(P_C,1),        \tag{2.2}
\]

in the notation of the XOR packet theorem.  Their edge label is

\[
                         1\oplus0\oplus1=0.           \tag{2.3}
\]

Thus every regular edge is a label-zero loop.  The constant vertex
potential \(x_{P_C}=0\) satisfies every equation
\(x_{P_C}\oplus x_{P_C}=0\), so the frustration index is zero. \(\square\)

This is stronger than merely saying that all signed cycles are balanced:
there are no non-loop constraints at all.

## 3. A two-factor pair-orbit imbalance theorem

We now drop reflection invariance.  Let \(\mathcal F_0,\mathcal F_1\) be
any two owner-disjoint strip factors (possibly with a common \(o(W)\)
owner leave) such that every strip transition flips endpoints inside one
fixed pair of \(\mathcal P\).  Direction orders, active coordinate sets,
Hamming resolution classes, and translations may be chosen independently
on the two shores.

For a rank-\((m-q)\) target \(T\), let \(f(T)\) be the number of full
\(\mathcal P\)-pairs.  The type-\(f\) target orbit has size \(T_{f,q}\) in
(0.3).  A middle owner of type \(f\) has \(f\) full and \(f\) empty pairs;
there are \(V_f\) such owners.

### Lemma 3.1 (one-shore type budget)

For either shore \(i\in\{0,1\}\), and for arbitrary selected port subsets,

\[
 \sum_{T:\,f(T)=f} k_i(T)\le V_f,                    \tag{3.1}
\]

where \(k_i(T)\) is the selected depth-\(q\) occurrence count of \(T\) on
shore \(i\).

#### Proof

Every raw forward depth-\(q\) occurrence has one middle owner as its start.
Flipping \(q\) split pairs makes precisely those pairs empty and does not
change the set of source-full pairs.  Hence an occurrence ending at a
target of full-pair type \(f\) starts at a middle owner of the same
full-pair type \(f\).

Each owner supplies one raw forward depth-\(q\) occurrence in its strip.
There are at most \(V_f\) available source owners of type \(f\); a common
leave can only reduce this number.  Selected ports are a subset of the raw
occurrences.  This proves (3.1). \(\square\)

### Theorem 3.2 (same-frame two-copy deficit)

If \(r_T=k_0(T)+k_1(T)\), then

\[
 \sum_{T\in\binom{[2m]}{m-q}}|r_T-2|
 \ge 2D_{m,q}.                                       \tag{3.2}
\]

#### Proof

Fix a deficient type \(f\), meaning \(T_{f,q}>V_f\).  The triangle
inequality and Lemma 3.1 give

\[
 \begin{aligned}
 \sum_{T:\,f(T)=f}|r_T-2|
 &\ge
 \left|\sum_{T:\,f(T)=f}(r_T-2)\right|\\
 &\ge
 2T_{f,q}-\sum_{T:\,f(T)=f}r_T\\
 &\ge
 2T_{f,q}-2V_f
 =2(T_{f,q}-V_f).
 \end{aligned}                                      \tag{3.3}
\]

Sum (3.3) over all deficient types. \(\square\)

The upper target layer obeys the same theorem by complementing every
source and target.  Therefore, if both signs are included in the
definition of \(\mathfrak B_2\), one may add the two lower bounds.

### Corollary 3.3 (Gaussian linear obstruction)

If \(q/\sqrt m\to c>0\), then every same-frame conjugate pair satisfies

\[
                         \mathfrak B_2\ge\Omega_c(W). \tag{3.4}
\]

#### Proof

The exact fixed-pair Hall computation gives

\[
 {D_{m,q}\over W}\longrightarrow
 e^{-c^2}\Phi(c/2)-\Phi(-3c/2)=\delta(c)>0.          \tag{3.5}
\]

Apply Theorem 3.2 at this one lower depth. \(\square\)

Since the intended annulus has \(H\gg\sqrt m\), such a depth is always
present for every fixed \(c>0\).

In particular, because \(\tau(G)\ge0\), the complete two-shore sufficient
quantity from the conjugate-packet theorem obeys the statewise bound

\[
                    \boxed{\mathfrak B_2+\tau(G)
                    \ge(2\delta(c)+o(1))W}            \tag{3.6}
\]

for every same-frame pair, whether or not its signed graph is balanced.

## 4. Interpretation and exact boundary

For the natural endpoint-reflection pair, the two terms in the packet
criterion split maximally cleanly:

\[
                         \tau(G)=0,
 \qquad
                         \mathfrak B_2=\Omega(W).     \tag{4.1}
\]

Thus no packing of frustrated cycles exists for this pair: its signed
graph is exactly balanced.  The failure precedes frustration and is the
old fixed-pair orbit-capacity obstruction in the correct two-copy
normalization.

Theorem 3.2 also disposes of every pair-preserving coordinate conjugate,
even if its signed graph happens to have a nontrivial favorable potential.
In particular, the following operations cannot supply a useful two-shore
packet pair while used globally in one frame:

* swapping arbitrary endpoints inside the fixed pairs;
* permuting the fixed pairs;
* changing direction orders or Hamming resolution classes;
* cyclically rotating or reversing the physical strip presentations; or
* taking the lower/upper complementary copy while retaining the same
  unordered pairing.

What remains genuinely open is a pair which changes the unordered pairing
on a positive fraction of owners, or a non-fixed-pair factor such as a
successful product-SCD-induced physical strip factor.  For such a pair the
type budget (3.1) no longer has a common \(f\)-coordinate, and one must
again determine either an \(o(W)\)-frustration potential or a packing of
\(\Omega(W)\) frustrated cycles.

## 5. Exact status

Proved:

1. endpoint-reflection invariance of the canonical dyadic Stage-A factor;
2. the singleton overlay description for the reflected pair;
3. the explicit constant signed potential and \(\tau(G)=0\);
4. the two-factor type-budget inequality (3.2), for arbitrary ports and
   arbitrary same-pair strip factors; and
5. its Gaussian \(\Omega(W)\) consequence.

Not proved:

* an \(o(W)\)-frustration theorem for any pair which changes the coordinate
  pairing;
* an \(\Omega(W)\) packing of frustrated cycles for such a mixed-frame
  pair; or
* the annulus matching theorem.

The natural reflection therefore gives a complete, rigorous negative
calibration of the signed-coboundary gate: exact balance of the signs alone
does not help unless the two-copy occurrence profile is also balanced.
