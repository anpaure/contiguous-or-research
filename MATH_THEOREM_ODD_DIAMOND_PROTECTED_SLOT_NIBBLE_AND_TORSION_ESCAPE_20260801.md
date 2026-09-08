# Protected odd diamonds admit `o(W)` total synchronization defect, and torsion escape has an exact cofactor criterion

Date: 2026-08-01  
Lane: odd upper-diamond synchronization / higher-torsion escape  
Status: unconditional protected `o(W)` total-overload theorem, exact linear
escape criterion, and exact cyclic-orbit negative.  Exact zero defect and
physical acyclicity remain open.

## 0. Outcome

Let

\[
 \Omega=[2m-1],\qquad
 \mathcal L={\Omega\choose m-1},\qquad
 \mathcal M={\Omega\choose m},\qquad
 \mathcal U={\Omega\choose m+1},
\]

and put

\[
 W=|\mathcal L|=|\mathcal M|,\qquad
 U=|\mathcal U|=W-\operatorname {Cat}_m.
\]

An upper diamond \((L,R)\) has \(L\in\mathcal L\),
\(R\in\mathcal U\), \(L\subset R\), and two physical middle owners.

This note gives a direct odd-dimensional bounded-*total* rounding of the
simultaneous upper/lower/owner selector.  It is the owner-slot specialization
of the same near-perfect-matching philosophy used by the repository's
ordered-diamond Delcourt--Postle lane; its new role here is to state the
protected exact-upper completion and its overload scalar explicitly.

> For every fixed protected tight-pivot bank, one can choose one diamond for
> every upper colour so that the protected diamonds survive and
> \[
>  \sum_{L\in\mathcal L}(d(L)-1)_+
>  +\sum_{T\in\mathcal M}(d(T)-2)_+=o(W).              \tag{0.1}
> \]

The proof is a direct Pippenger--Spencer matching argument on a 4-uniform
slot hypergraph.  It improves the constant-*local* bounds in the preceding
rounding note to sublinear *total* defect.  It is still far from the
\(O(1)\) sidecar required for \(B(k)+O(1)\), and it gives no cycle bound.

The note also gives the exact cofactor direction associated with a
determinant-\(q\) fractional face.  The explicit \(m=4\) one-third vertex is
a favorable instance: releasing one tight owner row gives a monotone segment
to an integral Catalan forest.  No theorem yet proves this favorable sign
pattern for every Boolean face.

Finally, order-three torsion is not a cyclic-orbit phenomenon.  It already
occurs at \(m=4\), where the \(\mathbb Z_7\) action on upper colours is free
and every orbit has size seven.

## 1. The owner-slot hypergraph

Make two labelled slots \(T^0,T^1\) for every owner
\(T\in\mathcal M\).  Define a 4-uniform hypergraph \(\mathcal H_m\) with
vertex set

\[
       \mathcal U\mathbin{\dot\cup}\mathcal L
       \mathbin{\dot\cup}(\mathcal M\times\{0,1\}).   \tag{1.1}
\]

If the two middle corners of the diamond \((L,R)\) are \(T,H\), put in the
four hyperedges

\[
                         \{R,L,T^i,H^j\},
                         \qquad i,j\in\{0,1\}.         \tag{1.2}
\]

A matching in \(\mathcal H_m\) projects to a diamond family with distinct
upper colours, distinct lower colours, and physical owner degree at most
two.  Conversely every such diamond family can be lifted to a matching by
assigning the at most two occurrences of each owner to its two slots.

### Lemma 1.1 (exact degrees and codegrees)

The three vertex types have degrees

\[
\begin{aligned}
 d(R)&=4{m+1\choose2}=2m(m+1),&&R\in\mathcal U,\\
 d(L)&=4{m\choose2}=2m(m-1),&&L\in\mathcal L,\\
 d(T^i)&=2m(m-1),&&T\in\mathcal M.                    \tag{1.3}
\end{aligned}
\]

Moreover

\[
                         \Delta_2(\mathcal H_m)\le2m. \tag{1.4}
\]

#### Proof

For fixed \(R\), choose its two deleted elements and then the two owner-slot
labels, giving the first row of (1.3).  For fixed \(L\), choose the two
added elements from its \(m\)-element complement and the two slots, giving
the second.

A fixed middle owner has \(m(m-1)\) Johnson neighbours: delete one of its
\(m\) elements and insert one of the \(m-1\) exterior elements.  Fixing its
slot still leaves two choices for the neighbour's slot, proving the third
row.

For codegrees, an incident upper/lower pair lies in four slot edges; an
incident upper/owner-slot pair lies in \(2m\); an incident
lower/owner-slot pair lies in \(2(m-1)\); two fixed owner slots lie in at
most one edge.  Same-type distinct pairs lie in no edge.  This proves
(1.4). \(\square\)

Thus, with

\[
                         D=2m(m+1),                           \tag{1.5}
\]

we have

\[
 {\delta(\mathcal H_m)\over D}={m-1\over m+1}\longrightarrow1,
 \qquad {\Delta_2(\mathcal H_m)\over D}=O(m^{-1})\longrightarrow0.
                                                               \tag{1.6}
\]

## 2. Protected almost-perfect synchronization

### Theorem 2.1 (`o(W)` total synchronization defect)

Let \(P_m\) be a protected diamond bank with

1. distinct upper colours;
2. distinct lower colours;
3. physical owner degree at most two; and
4. \(|P_m|=o(m)\).

Then there is a one-diamond-per-upper family \(B_m\supseteq P_m\) such that

\[
 \Phi(B_m):=
 \sum_{L\in\mathcal L}(d_{B_m}(L)-1)_+
 +\sum_{T\in\mathcal M}(d_{B_m}(T)-2)_+=o(W).          \tag{2.1}
\]

In particular, every fixed bank of tight-pivot collars, whose total diamond
length is \(O(\sqrt m)\), is retained.

#### Proof

Lift \(P_m\) to a matching of \(\mathcal H_m\): the owner-degree condition
allows the two physical occurrences at an owner to use different slots.
Delete every hypergraph vertex occupied by this matching and all incident
edges.  Call the residual hypergraph \(\mathcal H'_m\).

At most \(4|P_m|=o(m)\) vertices were deleted.  By (1.4), the degree of any
surviving vertex falls by at most

\[
                    4|P_m|\Delta_2(\mathcal H_m)=o(m^2)=o(D). \tag{2.2}
\]

Consequently \(\mathcal H'_m\) is still asymptotically regular with degree
\((1+o(1))D\), and its maximum codegree is still \(o(D)\).

The Pippenger--Spencer asymptotic chromatic-index theorem applies to this
fixed-uniformity hypergraph.  It gives a proper edge-colouring with

\[
                              (1+o(1))D                         \tag{2.3}
\]

colours.  Each colour class is a matching.  The number of residual edges is

\[
 |E(\mathcal H'_m)|
   =(U-|P_m|)(1-o(1))D.                                  \tag{2.4}
\]

Therefore one colour class has at least

\[
                              (1-o(1))U                         \tag{2.5}
\]

edges.  Project this matching to diamonds and adjoin \(P_m\).  The resulting
family has exact lower capacity one and owner capacity two, but may omit

\[
                              s_m=o(W)                          \tag{2.6}
\]

upper colours.

For each omitted upper colour choose an arbitrary diamond of that colour.
Each added diamond raises total lower overload by at most one and total
owner overload by at most two.  Hence the completed family \(B_m\) obeys

\[
                              \Phi(B_m)\le3s_m=o(W),            \tag{2.7}
\]

and still contains \(P_m\). \(\square\)

The external input is N. Pippenger and J. H. Spencer,
*Asymptotic behavior of the chromatic index for hypergraphs*, Journal of
Combinatorial Theory A 51 (1989), 24--42,
DOI `10.1016/0097-3165(89)90074-5`: for fixed uniformity, asymptotic
regularity and maximum codegree negligible relative to degree imply
chromatic index \((1+o(1))D\).

### Scope

The theorem controls the sum of all lower and owner overflows.  It does not
control physical cycles in the projected degree-two core.  It also does not
say that the \(o(W)\) completion diamonds preserve arbitrary-width upper
witnesses, residence, or a compiler cap.  The topology and full-word guards
remain separate.

## 3. Determinant torsion and the exact escape direction

Let \(x\) be a vertex of the synchronization polytope.  Restrict to its
positive support \(S\), and choose a square nonsingular matrix \(B\) of
active upper and capacity rows on those columns.  Put

\[
                              q=|\det B|.                       \tag{3.1}
\]

Cramer's rule shows that every coordinate denominator of \(x_S\) divides
the largest invariant factor of \(B\), and hence divides \(q\).  This is
the precise lattice torsion behind the fractional face.

Choose one active capacity row \(i\) in this basis and define its cofactor
direction

\[
                              c_i=\operatorname {adj}(B)e_i.    \tag{3.2}
\]

Then

\[
                              Bc_i=(\det B)e_i.                 \tag{3.3}
\]

Thus deleting row \(i\) exposes a one-dimensional fundamental circuit:
every other basis row remains fixed and row \(i\) changes by \(\det B\).
Orient \(c_i\) so that row \(i\) decreases.

### Theorem 3.1 (monotone torsion-escape criterion)

Suppose the oriented direction \(c_i\) satisfies

\[
                              a_hc_i\le0                        \tag{3.4}
\]

for every active capacity row \(h\) not kept equal by (3.3).  Define

\[
\begin{aligned}
 \tau_0&=\min_{j\in S:\,(c_i)_j<0}{x_j\over-(c_i)_j},\\
 \tau_+&=\min_{h:\,a_hx<b_h,\ a_hc_i>0}
                  {b_h-a_hx\over a_hc_i},             \tag{3.5}
\end{aligned}
\]

with an empty minimum interpreted as infinity.  If

\[
                              \tau_0\le\tau_+,                  \tag{3.6}
\]

then \(x+t c_i\), for \(0\le t\le\tau_0\), remains feasible and its final
point has strictly smaller positive support.

#### Proof

Equation (3.3) preserves every upper row and every retained active capacity
row.  Condition (3.4) prevents violation of any other tight capacity row.
The definition of \(\tau_+\) prevents an initially slack capacity row from
being exceeded before time \(\tau_0\), while the definition of \(\tau_0\)
preserves nonnegativity and makes at least one positive coordinate zero at
the endpoint. \(\square\)

This criterion is exact but not automatic.  A general cofactor direction
may increase another tight capacity row, or may hit a new tight row before a
support coordinate vanishes.  Proving that some row \(i\) always satisfies
(3.4)--(3.6), possibly after a bounded protected preparation, is the precise
**torsion-escape lemma** which would convert the LP into an exact selector.

### The calibrated cubic block

For the explicit \(m=4\) vertex in
`MATH_THEOREM_ODD_DIAMOND_SYNC_NONHALF_VERTEX_AND_CONSTANT_LOCAL_ROUNDING_20260801.md`,
we have \(q=3\).  Taking \(i\) to be the owner-`1235` row gives the segment

\[
                              0\le z\le1/3.                     \tag{3.7}
\]

At \(z=1/3\) lies the fractional vertex; at \(z=0\) lies the listed
integral upper/lower-rainbow owner-cap-two Catalan forest.  Every other
active row stays equal, owner `1235` decreases from two to one, and no slack
row becomes tight first.  Hence (3.4)--(3.6) hold with equality at a support
boundary.

This is a genuine higher-torsion escape, but only one calibrated face.

## 4. Boolean synchronization has unbounded determinant torsion

The determinant-three face contains a smaller literal cubic minor.  In the
row order

\[
 \begin{gathered}
 U_{12345},U_{12346},U_{12357},
 L_{123},L_{124},L_{135},L_{235},M_{1235},M_{1357},
 \end{gathered}
\]

and column order

\[
\begin{gathered}
(123,12346),(123,12356),(124,12345),(124,12346),\\
(135,12345),(135,13567),(157,12357),
(235,12345),(235,12357),
\end{gathered}
\]

the natural upper/lower/owner matrix is

\[
A_3=
\begin{pmatrix}
0&0&1&0&1&0&0&1&0\\
1&0&0&1&0&0&0&0&0\\
0&0&0&0&0&0&1&0&1\\
1&1&0&0&0&0&0&0&0\\
0&0&1&1&0&0&0&0&0\\
0&0&0&0&1&1&0&0&0\\
0&0&0&0&0&0&0&1&1\\
0&1&0&0&1&0&0&1&1\\
0&0&0&0&0&1&1&0&0
\end{pmatrix},
\qquad \det A_3=-3.                                  \tag{4.1}
\]

Integer row and column elimination gives the Smith normal form

\[
                         \operatorname {SNF}(A_3)
                           =\operatorname {diag}(1,1,1,1,1,1,1,1,3). \tag{4.2}
\]

Thus this is one primitive cubic torsion block: its cokernel torsion is one
copy of \(\mathbb Z/3\mathbb Z\), not a product hidden inside the displayed
minor.

This one block amplifies to arbitrarily large Boolean minors.

### Theorem 4.1 (block-diagonal cubic amplification)

For every positive integer \(t\), and every

\[
                              m\ge7t-3,                         \tag{4.3}
\]

the synchronization matrix for semilength \(m\) contains a square minor of
absolute determinant \(3^t\).

#### Proof

Choose a common core \(K\) of size \(m-4\), and choose \(t\) pairwise
disjoint seven-label banks outside \(K\).  Condition (4.2) is exactly

\[
                         |K|+7t\le2m-1.                        \tag{4.4}
\]

Inside each bank take the nine rows and nine columns of (4.1), adjoining
\(K\) to every displayed lower, upper and owner set.  Their ranks become
respectively \(m-1,m+1,m\), so they are literal rows and columns of the
semilength-\(m\) Boolean system.

Rows and columns from different banks use different noncore labels and
therefore have no selected incidence with one another.  The resulting
\(9t\)-square minor is block diagonal with \(t\) copies of \(A_3\).  Its
determinant is \((-3)^t\). \(\square\)

### Consequence

The natural synchronization matrix is not totally \(q\)-modular for any
absolute \(q\); its subdeterminants grow exponentially in the number of
disjoint active seven-label banks.  Therefore no rounding proof can rely on
a bounded list of determinant orders, even though each individual primitive
block above is cubic.

This matrix statement does not by itself construct feasible vertices with
denominator \(3^t\): the right-hand side and all unselected capacity rows
still matter.  It does prove that a general torsion-escape theorem must be
stable under simultaneous independent cubic blocks, which is exactly why a
protected absorber bank or a global slack allocation is needed.

## 5. Cyclic quotient does not isolate order-three torsion

At \(m=4\), the ground set has size seven.  Every nonempty proper subset of
\([7]\) has a free orbit under cyclic rotation \(\mathbb Z_7\): a nontrivial
stabilizer would be all of \(\mathbb Z_7\), forcing the subset to be empty or
all of \([7]\).  In particular every rank-five upper-colour orbit has size
seven.

Nevertheless Section 2 of the preceding note gives a determinant-three
vertex.  Its seven fractional upper colours are not even one cyclic orbit:
their complementary 2-sets have cyclic distances with multiplicities

\[
                              1^2,\quad2^3,\quad3^2.            \tag{4.1}
\]

### Corollary 5.1

The order-three torsion of the synchronization LP cannot be attributed
solely to order-three cyclic stabilizers, orbit sizes, or one complete
upper-colour rotation orbit.  A cyclic-quotient proof may still average or
rethread torsion globally, but it cannot classify all torsion by the sizes
of the \(\mathbb Z_{2m-1}\) upper orbits.

## 6. Revised frontier

Three scales are now separated exactly.

1. **Local multiplicity:** bounded unconditionally by the degree-bounded
   matroid rounding (`3/4`, or protected `4/6`).
2. **Total synchronization defect:** reduced unconditionally to \(o(W)\),
   retaining every fixed tight-pivot bank, by Theorem 2.1.
3. **Exact synchronization:** still requires a uniform torsion-escape or
   absorption theorem reducing \(o(W)\) to \(O(1)\), preferably zero.

After exact synchronization, physical cycle elimination and the rooted
Catalan connector are separate.  The present theorem does not claim an
upper-decorated Hamilton path or a universal OR word.
