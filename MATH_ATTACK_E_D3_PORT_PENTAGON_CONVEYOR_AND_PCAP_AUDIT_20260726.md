# Lane E rebased: the \(D_3\)-port pentagon, conveyor lattice, and PCap capacity

Date: 2026-07-26

Method: pure mathematics only.  All finite assertions are verified from
the displayed paths and set identities.

## 0. Outcome

There is a genuine port-preserving associator.  On \(J=[6]\), the five old
and five new paths below are two complete
\(\mathcal D_3\)-port-transversal path factors of the middle-levels
inclusion graph.  Both exhaust all twenty three-sets and all fifteen
four-set colours, and every root/complement endpoint pair is fixed
row-by-row.

Its intrinsic singleton-target displacement is

\[
 \boxed{\delta_{\rm pent}
 =2e_3+e_5-e_4-2e_2.}                                  \tag{0.1}
\]

Thus it crosses the leaf-rotation normal-form partition: it acts
nontrivially on a root with first-return semilength \(j=3\), while
preserving the complete \(X/Y\) ownership ledgers and all Dyck ports.

Arbitrary outer-context copies have constant-density raw capacity.  The
number of aligned size-three contexts is

\[
 H_{m,3}={1\over2}\binom{2(m-3)}{m-3}
        =\left({1\over256}+o(1)\right)
          \binom{2m+1}{m}.                              \tag{0.2}
\]

Each copy transports three positive units and three negative units in its
intrinsic target ledger, so the full bank has raw transport mass

\[
 3H_{m,3}=\left({3\over256}+o(1)\right)W.               \tag{0.3}
\]

This is larger than the \(o(W)\) PCap correction scales currently sought;
there is no scalar-capacity obstruction.

Two limitations remain exact.

1. Every port-preserving copy fixes its Dyck root endpoints pointwise.
   Hence these copies do not generate a conveyor understood as a
   permutation of Catalan roots.
2. In one fixed context, port-preserving automorphic copies of (0.1)
   generate only an index-four rank-two lattice, not the full zero-sum
   target lattice.  Overlapping outer contexts may mix these local
   sublattices, but no global spanning or PCap-oriented selection theorem
   is yet proved.

The new sharp target is therefore a contextual incidence-lattice and
sign-selection theorem, not another local associator.

## 1. The two path factors

The standard Dyck ports are

\[
                  \mathcal D_3=\{123,124,125,134,135\}. \tag{1.1}
\]

The old factor is

\[
\begin{array}{c|cccc}
P_1^-&123&136&146&456\\
P_2^-&124&126&156&356\\
P_3^-&125&145&345&346\\
P_4^-&135&235&245&246\\
P_5^-&134&234&236&256,
\end{array}                                             \tag{1.2}
\]

and the new factor is

\[
\begin{array}{c|cccc}
P_1^+&123&126&156&456\\
P_2^+&124&234&345&356\\
P_3^+&125&235&236&346\\
P_4^+&135&136&146&246\\
P_5^+&134&145&245&256.
\end{array}                                             \tag{1.3}
\]

## 2. Legality, endpoints, and the \(X\)-ledger

### Lemma 2.1

Every row of (1.2)--(1.3) is a length-three Johnson geodesic from a member
\(P\in\mathcal D_3\) to its complement \(J\setminus P\).  The two factors
have the same rowwise endpoint pairs.

#### Proof

Every consecutive pair has two common coordinates, hence is a Johnson
edge.  The five endpoint pairs on both sides are

\[
 123\leftrightarrow456,\quad
 124\leftrightarrow356,\quad
 125\leftrightarrow346,\quad
 135\leftrightarrow246,\quad
 134\leftrightarrow256.
\]

These are exactly the five Dyck/complement pairs. \(\square\)

### Lemma 2.2

Both tables enumerate every three-subset of \([6]\) exactly once.

#### Proof

The old and new entries have the common set

\[
\begin{aligned}
\mathcal X=\{&
123,124,125,126,134,135,136,145,146,156,\\
&234,235,236,245,246,256,345,346,356,456\},
\end{aligned}                                           \tag{2.1}
\]

which is \(\binom{[6]}3\). \(\square\)

In particular every Dyck set occurs exactly once and is a port.  This is
the global property missing from the four-row \(D_4\) packet.

## 3. The complete \(Y\)-ledger

For a path \(P=(X_0,X_1,X_2,X_3)\), put
\(Y_t=X_t\cup X_{t+1}\).

### Lemma 3.1

Both factors enumerate every four-subset of \([6]\) exactly once among
their adjacent unions.

#### Proof

The old colour rows are

\[
\begin{array}{c|ccc}
P_1^-&1236&1346&1456\\
P_2^-&1246&1256&1356\\
P_3^-&1245&1345&3456\\
P_4^-&1235&2345&2456\\
P_5^-&1234&2346&2356,
\end{array}                                             \tag{3.1}
\]

and the new colour rows are

\[
\begin{array}{c|ccc}
P_1^+&1236&1256&1456\\
P_2^+&1234&2345&3456\\
P_3^+&1235&2356&2346\\
P_4^+&1356&1346&1246\\
P_5^+&1345&1245&2456.
\end{array}                                             \tag{3.2}
\]

Each table lists the fifteen members of \(\binom{[6]}4\) exactly once.
\(\square\)

### Theorem 3.2 (the port-preserving pentagon trade)

Replacing (1.2) by (1.3) is a support-feasible exact local-factor trade.
After adjoining the omitted coordinate \(\infty\), both sides are exact
\(C_7\)-factors.  They are \(\mathcal D_3\)-port-transversal with identical
root/complement ports row-by-row.

The trade remains valid after arbitrary coordinate relabelling and after
adjoining a common exterior set in an aligned ambient context.

#### Proof

Lemma 2.2 is the complete \(X\)-vertex ledger.  Lemma 3.1 is the complete
\(Y\)-vertex ledger.  The middle-levels path-factor normal form therefore
lifts both tables to exact odd-graph factors.  Lemma 2.1 proves the
port statement.  Relabelling and adjoining a common exterior set preserve
containment, adjacency, and both multiset identities. \(\square\)

## 4. Exact intrinsic target movement

For a path \(P=(X_0,X_1,X_2,X_3)\), define its intrinsic target

\[
                         \theta(P)=X_1\cap X_2\cap X_3. \tag{4.1}
\]

### Proposition 4.1

The old and new target lists are

\[
 \begin{array}{c|ccccc}
 &P_1&P_2&P_3&P_4&P_5\\ \hline
 \theta^-&6&6&4&2&2\\
 \theta^+&6&3&3&6&5.
 \end{array}                                             \tag{4.2}
\]

Consequently the signed target change is (0.1).

#### Proof

Take the three-state intersections directly.  For example,

\[
 126\cap156\cap356=\{6\},\qquad
 234\cap345\cap356=\{3\},
\]

and the other eight intersections are equally immediate.  Subtracting the
two rows of (4.2) gives

\[
 (2e_6+2e_3+e_5)-(2e_6+e_4+2e_2)
 =2e_3+e_5-e_4-2e_2.
\]

\(\square\)

The root \(124\) is the primitive Dyck word \(110100\), with first-return
semilength \(j=3\).  Its target moves from \(6=2j\) to \(3\).
Thus this packet reaches beyond the leaf associator, whose root action is
confined to \(j=2\leftrightarrow1\).

## 5. Exact contextual supply

An aligned size-three context has a fixed exterior target \(O_C\) and an
affine labelling

\[
                         \iota_C:[6]\longrightarrow J_C.
\]

The contextual intrinsic direction is

\[
\boxed{
d_C=
 2e_{O_C\cup\{\iota_C(3)\}}
 +e_{O_C\cup\{\iota_C(5)\}}
 -e_{O_C\cup\{\iota_C(4)\}}
 -2e_{O_C\cup\{\iota_C(2)\}}.}                         \tag{5.1}
\]

### Proposition 5.1 (simultaneous fixed-scale bank)

All aligned size-three copies of the pentagon may be selected
simultaneously while preserving exact middle ownership.  Their number is
\(H_{m,3}\) in (0.2), and the sum of the positive masses of their intrinsic
directions is \(3H_{m,3}\).

#### Proof

Distinct recursive nodes of the same size cannot be nested.  If two occur
in one root, their coordinate blocks and phase slabs are disjoint.
Therefore the corresponding rowwise replacements commute.  Theorem 3.2
gives exactness in every slab, so their ownership ledgers add.

Equation (5.1) has positive mass three.  The audited aligned-context count
is

\[
 H_{m,3}={1\over2}\binom{2(m-3)}{m-3}.
\]

Using

\[
 W=\binom{2m+1}{m}
   ={2\,4^m\over\sqrt{\pi m}}(1+o(1))
\]

and the central-binomial asymptotic gives (0.2)--(0.3). \(\square\)

Thus the pentagon bank has more than enough *raw scalar* mass to absorb an
\(o(W)\) PCap defect.  This does not yet give a correctly directed
absorber.

## 6. What “Catalan conveyor” can mean

There are two inequivalent notions.

### Proposition 6.1 (no root-permutation conveyor)

Every contextual pentagon copy fixes each Dyck port and its complementary
endpoint row-by-row.  Hence every composition of such copies induces the
identity permutation on the Catalan root set.

#### Proof

This is Lemma 2.1 after adjoining the fixed exterior context.  Composition
preserves the pointwise endpoint identities. \(\square\)

Therefore the pentagon does not generate the Tamari symmetric group on
roots.  Its useful action is instead a **shadow conveyor**: it changes the
target attached to a fixed root, as in (4.2).

This shadow action genuinely crosses the leaf-rotation normal-form
partition.  In particular it changes the target of the \(j=3\) root
\(124\), something no below-root leaf rotation can do.

## 7. The local automorphism lattice

The automorphism group of the port family (1.1) is

\[
 \operatorname{Aut}(\mathcal D_3)
 =\langle(2\ 3),(4\ 5)\rangle
 \cong C_2\times C_2,                                  \tag{7.1}
\]

with coordinates \(1\) and \(6\) fixed.

#### Proof

Coordinate \(1\) belongs to all five ports and \(6\) to none, so both are
fixed.  Coordinates \(2,3\) have port degree three and coordinates \(4,5\)
degree two.  The two displayed swaps preserve the five sets, and these
degree classes allow no other permutations. \(\square\)

Put

\[
 x=e_3-e_2,\qquad y=e_5-e_4.
\]

Then \(\delta_{\rm pent}=2x+y\).  Its orbit under (7.1) is

\[
                         \{\pm(2x+y),\ \pm(2x-y)\}.       \tag{7.2}
\]

### Proposition 7.1 (index-four local lattice)

The integer lattice generated by all port-preserving automorphic copies of
the pentagon direction is

\[
 \boxed{
 \Lambda_{\rm pent}
 =\{\,2a\,x+b\,y:\ a,b\in\mathbb Z,\ a\equiv b\pmod2\,\}.}
 \tag{7.3}
\]

It has rank two and index four in
\(\mathbb Zx\oplus\mathbb Zy\).  In particular it is not the full
zero-sum lattice on the six local singleton targets.

#### Proof

The generators \(2x+y\) and \(2x-y\) give coefficient pairs
\((2,1)\) and \((2,-1)\), whose determinant has absolute value four.
Their integer combinations are exactly (7.3). \(\square\)

Thus one fixed context has a real and integral routing restriction.  The
restriction may disappear globally because different outer contexts embed
the four active roles into different physical targets, but that requires a
theorem about the full context-incidence matrix.

## 8. PCap: what is proved and what remains

For one serviced depth, boundary locality gives a constant-degree conflict
graph on same-scale contextual copies: a length-\(q\) intersection window
can interact with a size-three replacement only when one of its two
boundaries meets that replacement slab.  Hence a constant fraction of the
bank can be made additive at any **one** depth.  Together with (0.3), this
leaves no one-depth capacity obstruction.

This does not prove the required multidepth PCap theorem:

1. the intrinsic vector (5.1) directly controls the size-three target
   row, while the effects at growing depths are boundary arms which have
   not yet been given a favorable sign;
2. a subfamily simultaneously additive at every \(q\le H\) obtained by
   naive conflict colouring can lose a factor of order \(H\);
3. the available direction in a fixed context lies in the restricted
   lattice (7.3); and
4. cap-tail improvement is nonlinear and requires correlation of the
   chosen orientations with the current overloads.

The exact remaining lemma can be stated without reference to Tamari
connectivity.

> **Contextual pentagon PCap lemma \((\mathrm{CPP}_H)\).**  
> For the aligned-context directions \(d_C\), together with their complete
> boundary-arm vectors at every \(q\le H\), choose legal old/new pentagon
> states so that the resulting exact factor has total protected cap tail
> \(o(W)\), while the aggregate nonadditive boundary remainder is \(o(W)\).

The pentagon proves that \((\mathrm{CPP}_H)\) has the right local
integrality, chronology, port, and scalar-capacity inputs.  Its unresolved
content is global incidence-lattice expansion and correlated multidepth
signing.
