# The depth-one Johnson trade image and legal pentagon defect mobility

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, or external input is
used.

## 0. Outcome

Let \(\Omega\) have size \(n\), let the middle rank be \(m\), and assume

\[
                         m\ge3,\qquad n\ge m+3.                 \tag{0.1}
\]

For a Johnson edge \(e=XY\) of \(J(n,m)\), write

\[
 L(e)=X\cap Y,\qquad U(e)=X\cup Y.                             \tag{0.2}
\]

Let \(B_0,B_-,B_+\) record respectively the two middle endpoints, the
lower colour, and the upper colour of an edge.  The fixed-owner,
fixed-lower integral trade lattice is

\[
 \mathcal T=\ker_{\mathbb Z}B_0\cap\ker_{\mathbb Z}B_-.       \tag{0.3}
\]

Let \(P_{m+1}\) be point-versus-\((m+1)\)-set incidence.  The main theorem
of this note is the exact integral identity

\[
 \boxed{B_+(\mathcal T)=\ker_{\mathbb Z}P_{m+1}.}              \tag{0.4}
\]

Thus there is a short exact sequence

\[
 0\longrightarrow \mathcal T\cap\ker B_+
 \longrightarrow\mathcal T
 \mathop{\longrightarrow}^{B_+}
 \ker_{\mathbb Z}P_{m+1}\longrightarrow0.                    \tag{0.5}
\]

This strengthens the previously proved point-margin necessity in two ways.

1. Point incidence gives **all** integral linear invariants of the upper
   ledger.  There is no additional rational invariant, parity invariant,
   or finite-index lattice obstruction inside the fixed-owner,
   fixed-lower fibre.
2. The full coordinate orbit of the complemented six-coordinate pentagon
   already generates the whole image in (0.4).  More precisely, every
   elementary four-term upper trade is the difference of two pentagon
   images.

Consequently, on even ground \(n=2m\), a lower-rainbow saturating cycle on
\(N=\binom{2m}{m-1}\) owners has a formal integral trade to the exact
all-one upper ledger if and only if its owner set is point-balanced:

\[
 \boxed{|\{X\in V(C):v\in X\}|=N/2\quad(v\in[2m]).}            \tag{0.6}
\]

The word *formal* is essential: (0.4) does not assert that the lifted trade
is conformal at a given cycle, binary after application, or connected.

Upper defect is nevertheless genuinely mobile in the legal Hamilton state
space.  Two explicit Hamilton cycles of \(J(6,3)\), having exactly the same
complete lower histogram and related by one port-preserving complemented
pentagon, have respectively

\[
 (M^+,R^+)=(2,7),\qquad (M^+,R^+)=(1,6).             \tag{0.7}
\]

Thus neither the upper hole count nor upper repeat excess is a legal-switch
invariant.  What remains open for the exact lower-rainbow saturating core is
legal connectivity: one must realize enough conformal pentagons, or larger
ported trades, inside the chosen cycle.  Algebraic trade generation alone
does not supply their occurrences.

## 1. Oriented transition and point ledgers

Orient a simple Johnson cycle as

\[
                         C=(X_0,X_1,\ldots,X_{s-1}).            \tag{1.1}
\]

Write its \(i\)-th transition uniquely as

\[
 X_{i+1}=X_i-a_i+b_i,qquad a_i\in X_i,\quad b_i\notin X_i.    \tag{1.2}
\]

Then

\[
 L_i=X_i-\{a_i\},\qquad U_i=X_i\cup\{b_i\}.                  \tag{1.3}
\]

Let \(\ell\) and \(u\) be the lower and upper colour histograms, and let

\[
 r_v=|\{i:v\in X_i\}|.                                       \tag{1.4}
\]

Because the cycle returns to its initial owner, each coordinate is inserted
as often as it is deleted.  Put

\[
 t_v=|\{i:a_i=v\}|=|\{i:b_i=v\}|.                            \tag{1.5}
\]

### Lemma 1.1 (oriented depth-one ledger)

For every coordinate \(v\),

\[
 \boxed{
 (P_{m-1}\ell)_v=r_v-t_v,\qquad
 (P_{m+1}u)_v=r_v+t_v.}                                      \tag{1.6}
\]

Equivalently,

\[
 \boxed{P_{m-1}\ell+P_{m+1}u=2r.}                           \tag{1.7}
\]

Moreover,

\[
 (P_{m+1}u-P_{m-1}\ell)_v=2t_v,                             \tag{1.8}
\]

so the coordinate-swap multigraph is Eulerian.

#### Proof

At transition \(i\), a coordinate \(v\) lies in \(L_i\) precisely when it
lies in \(X_i\) and is not the deleted coordinate \(a_i\).  Summing gives
the first identity in (1.6).  It lies in \(U_i\) precisely when it lies in
\(X_i\), or it is the newly inserted coordinate \(b_i\).  Summing gives the
second identity.  Equations (1.7)--(1.8) follow by addition and subtraction.
\(\square\)

The unoriented edgewise version of (1.7) is the diamond identity

\[
 \boxed{P_{m-1}B_-+P_{m+1}B_+=P_mB_0.}                       \tag{1.9}
\]

Indeed, for one edge \(XY\) and one coordinate \(v\),

\[
 \mathbf1_{v\in X\cap Y}+\mathbf1_{v\in X\cup Y}
 =\mathbf1_{v\in X}+\mathbf1_{v\in Y}.                      \tag{1.10}
\]

It follows immediately that

\[
                         B_+(\mathcal T)\subseteq\ker P_{m+1}.
                                                                    \tag{1.11}
\]

The rest of the proof establishes the reverse inclusion integrally.

## 2. The integer kernel of point incidence

We first prove a general elementary lemma.  Let \(2\le k\le n-2\), let
\(F_k\) be the free abelian group on the \(k\)-subsets of \(\Omega\), and
write \(e_A\) for its standard basis.

For a \((k-2)\)-set \(C\) and four distinct points
\(a,b,c,d\notin C\), define the quadrilateral

\[
 q(C;a,b,c,d)
 =e_{C\cup\{a,b\}}+e_{C\cup\{c,d\}}
  -e_{C\cup\{a,c\}}-e_{C\cup\{b,d\}}.                      \tag{2.1}
\]

Let \(Q_k\) be their integer span.

### Lemma 2.1 (integral quadrilateral generation)

For point-versus-\(k\)-set incidence \(P_k\),

\[
                         \boxed{Q_k=\ker_{\mathbb Z}P_k.}      \tag{2.2}
\]

#### Proof

Every vector (2.1) has zero point incidence, so
\(Q_k\subseteq\ker P_k\).

Work in the quotient \(F_k/Q_k\), and denote the class of \(e_A\) by
\([A]\).  Fix distinct points \(a,b\).  If
\(T\in\binom{\Omega\setminus\{a,b\}}{k-1}\), put

\[
 \delta_{a,b}(T)=[T\cup\{a\}]-[T\cup\{b\}].                 \tag{2.3}
\]

This class is independent of \(T\).  Indeed, adjacent vertices of
\(J(n-2,k-1)\) have the form

\[
 T=C\cup\{c\},\qquad T'=C\cup\{d\},                         \tag{2.4}
\]

and the quadrilateral relation on \(C,a,b,c,d\) says exactly

\[
 [T\cup\{a\}]-[T\cup\{b\}]
 =[T'\cup\{a\}]-[T'\cup\{b\}].                             \tag{2.5}
\]

The graph \(J(n-2,k-1)\) is connected because
\(1\le k-1\le n-3\).  Write the common class as \(\delta_{a,b}\).

If \(a,b,c\) are distinct, there is a \((k-1)\)-set avoiding all three,
because \(k-1\le n-3\).  Using that common context in (2.3) gives

\[
 \delta_{a,b}+\delta_{b,c}=\delta_{a,c}.                       \tag{2.6}
\]

Fix a point \(p\), set \(\gamma_p=0\), and set
\(\gamma_a=\delta_{a,p}\) for \(a\ne p\).  Then

\[
                         \delta_{a,b}=\gamma_a-\gamma_b.       \tag{2.7}
\]

If two \(k\)-sets are Johnson-adjacent, say
\(A=T\cup\{a\}\) and \(A'=T\cup\{b\}\), equations
(2.3) and (2.7) give

\[
 [A]-\sum_{x\in A}\gamma_x
 =[A']-\sum_{x\in A'}\gamma_x.                               \tag{2.8}
\]

Since \(J(n,k)\) is connected, there is one class \(\alpha\) such that

\[
                         [A]=\alpha+\sum_{x\in A}\gamma_x    \tag{2.9}
\]

for every \(k\)-set \(A\).

Now take \(y=\sum_Ay_Ae_A\in\ker_{\mathbb Z}P_k\).  Summing its point
equations gives

\[
                         k\sum_Ay_A=0,
\]

and hence \(\sum_Ay_A=0\).  Formula (2.9) yields

\[
 \sum_Ay_A[A]
 =\alpha\sum_Ay_A
  +\sum_{x\in\Omega}\gamma_x\sum_{A\ni x}y_A=0.              \tag{2.10}
\]

Thus \(y\in Q_k\), proving the reverse inclusion in (2.2).  Every step
took place over \(\mathbb Z\), so there is no hidden finite index.
\(\square\)

## 3. The pentagon orbit lifts every quadrilateral

Let \(D\) be a six-set, let \(K\) be an \((m-3)\)-set disjoint from
\(D\), and let \(M,N\) be disjoint perfect matchings of \(D\).  Define

\[
 w(K;M,N)=
 \sum_{ij\in M}e_{K\cup(D\setminus\{i,j\})}
 -\sum_{ij\in N}e_{K\cup(D\setminus\{i,j\})}.                \tag{3.1}
\]

The complemented rooted-pentagon tables give one fixed-owner,
fixed-lower trade whose upper image is the difference of two disjoint
perfect matchings.  Relabelling its six active coordinates proves the
following.

### Lemma 3.1 (six-cycle lift)

For every \(K,D,M,N\) as above, there is
\(z(K;M,N)\in\mathcal T\) with

\[
                         B_+z(K;M,N)=w(K;M,N).                 \tag{3.2}
\]

#### Proof

One explicit complemented pentagon has upper difference

\[
 e_{K\cup\widehat{25}}+e_{K\cup\widehat{36}}
 +e_{K\cup\widehat{14}}
 -e_{K\cup\widehat{15}}-e_{K\cup\widehat{34}}
 -e_{K\cup\widehat{26}},                                    \tag{3.3}
\]

where hats denote complements inside \([6]\).  The positive and negative
omitted pairs in (3.3) are disjoint perfect matchings.  The two path-factor
tables have the same row ports, the same middle-owner degree ledger, and
the same complete lower ledger.  Their signed difference therefore lies
in \(\mathcal T\).

The union of two disjoint perfect matchings on six labelled points is an
alternating six-cycle.  The symmetric group on \(D\) is transitive on
ordered alternating colourings of such a cycle.  A coordinate relabelling
of (3.3) therefore gives (3.2) for every ordered pair \((M,N)\).  Adjoining
the fixed core \(K\) preserves all three ledgers. \(\square\)

### Lemma 3.2 (a quadrilateral is two pentagons)

Every quadrilateral in \(\ker P_{m+1}\) belongs to \(B_+(\mathcal T)\).

#### Proof

Write such a quadrilateral as

\[
 q=e_{C\cup\{a,b\}}+e_{C\cup\{c,d\}}
   -e_{C\cup\{a,c\}}-e_{C\cup\{b,d\}},                     \tag{3.4}
\]

where \(|C|=m-1\).  Choose two distinct points \(p,q_0\in C\), and put

\[
 K=C\setminus\{p,q_0\},qquad
 D=\{p,q_0,a,b,c,d\}.                                       \tag{3.5}
\]

On \(D\), consider the perfect matchings

\[
\begin{aligned}
 M_1&=\{ab,cd,pq_0\},\\
 M_2&=\{ac,bd,pq_0\},\\
 M_0&=\{ap,q_0d,bc\}.
\end{aligned}                                                 \tag{3.6}
\]

The matching \(M_0\) is edge-disjoint from each of \(M_1,M_2\).  Hence
Lemma 3.1 gives two pentagon trades, and

\[
\begin{aligned}
 B_+\bigl(z(K;M_1,M_0)-z(K;M_2,M_0)\bigr)
 &=w(K;M_1,M_2)\\
 &=q.                                                         \tag{3.7}
\end{aligned}
\]

For the last equality, the common omitted edge \(pq_0\) cancels;
omitting \(ab,cd,ac,bd\) from \(D\), and then adjoining \(K\), gives
respectively

\[
 C\cup\{c,d\},\quad C\cup\{a,b\},\quad
 C\cup\{b,d\},\quad C\cup\{a,c\}.                        \tag{3.8}
\]

This is exactly (3.4). \(\square\)

### Theorem 3.3 (complete integral upper action)

Equation (0.4) holds.

#### Proof

Inclusion from left to right is (1.11).  Apply Lemma 2.1 with
\(k=m+1\).  Assumption (0.1) gives

\[
                         2\le m+1\le n-2.
\]

Every element of \(\ker_{\mathbb Z}P_{m+1}\) is therefore an integer sum
of quadrilaterals, and Lemma 3.2 lifts each quadrilateral to
\(\mathcal T\). \(\square\)

### Corollary 3.4 (complete linear invariant theorem)

Over \(\mathbb Q\) or \(\mathbb R\), an upper-target functional is
constant on every fixed-owner, fixed-lower trade fibre if and only if it
has the form

\[
                         f(U)=\sum_{v\in U}c_v                \tag{3.9}
\]

for some point weights \((c_v)\).  Constants are included by taking all
\(c_v\) equal.

#### Proof

By Theorem 3.3 the invariant functionals are the annihilator of
\(\ker P_{m+1}\), namely the row space of \(P_{m+1}\).  Its elements are
exactly (3.9). \(\square\)

### Corollary 3.5 (formal fibre criterion)

Fix any integral Johnson edge vector \(x\).  An integral upper vector
\(u'\) is obtainable while preserving \(B_0x\) and \(B_-x\) if and only if

\[
                         P_{m+1}u'=P_{m+1}B_+x.               \tag{3.10}
\]

#### Proof

Necessity is the diamond identity.  Under (3.10), the difference
\(u'-B_+x\) lies in \(\ker_{\mathbb Z}P_{m+1}\), so Theorem 3.3 lifts it
to a member of \(\mathcal T\). \(\square\)

## 4. Exact consequence for a lower-rainbow saturating cycle

Now take \(n=2m\), and put

\[
 N=\binom{2m}{m-1}.                                           \tag{4.1}
\]

Let \(C\) be a simple \(N\)-cycle whose lower colours are all members of
\(\binom{[2m]}{m-1}\), once each.  Let \(V(C)\) be its owner set and let

\[
                         r_v=|\{X\in V(C):v\in X\}|.          \tag{4.2}
\]

The upper and lower target layers both have size \(N\).  Hence exact
two-sided rainbowness asks for the all-one upper vector.

### Theorem 4.1 (formal two-sided upgrade criterion)

There is \(z\in\mathcal T\) satisfying

\[
                         B_+(x_C+z)=\mathbf1                 \tag{4.3}
\]

if and only if (0.6) holds.

#### Proof

The diamond identity gives

\[
 P_{m+1}B_+x_C
 =2r-P_{m-1}\mathbf1.                                  \tag{4.4}
\]

By Theorem 3.3, (4.3) has an integral solution in \(\mathcal T\) if and
only if

\[
 P_{m+1}\mathbf1
 =2r-P_{m-1}\mathbf1.                                  \tag{4.5}
\]

For every coordinate,

\[
 \binom{2m-1}{m-2}+\binom{2m-1}{m}=\binom{2m}{m-1}=N,         \tag{4.6}
\]

where \(\binom{2m-1}{m}=\binom{2m-1}{m-1}\).  Thus (4.5) is
exactly \(2r_v=N\) for every \(v\). \(\square\)

This theorem closes the ledger lattice and nothing more.  The vector
\(x_C+z\) supplied by it may have negative or nonbinary coordinates, and
even a binary two-factor need not be connected.  Thus point balance is
algebraically sufficient but is not yet a Hamilton switch theorem.

For odd ground, or for a shorter upper-injective target, the corresponding
statement is equally exact.  If \(b\in\{0,1\}^{\binom{[n]}{m+1}}\) has the
same total mass as \(u_C\), then there is a formal trade with upper ledger
\(b\) if and only if

\[
                         P_{m+1}b=P_{m+1}u_C.                  \tag{4.7}
\]

The additional problem is existence of the binary target vector \(b\) and
then a conformal connected lift.

There is a complementary formal conclusion for a full-owner Hamilton
cycle.  It explains why the remaining obstruction there is also legal
rather than a ledger obstruction.

### Theorem 4.2 (formal hole removal for every full-owner lower-complete cycle)

Let \(C\) be a Hamilton cycle of \(J(2m,m)\), and suppose its lower
histogram is

\[
                         \ell=\mathbf1+h,\qquad h\ge0.          \tag{4.8}
\]

Then there is a nonnegative integral upper vector \(u'\), with no holes and
with total mass \(W=\binom{2m}m\), such that

\[
                         P_{m+1}u'=P_{m+1}u_C.                 \tag{4.9}
\]

Consequently Theorem 3.3 supplies a formal
\(z\in\mathcal T\) with \(B_+(x_C+z)=u'\).

#### Proof

Put

\[
 N=\binom{2m}{m-1},\qquad E=W-N.
\]

Since the Hamilton cycle has \(W\) edges and every lower target is used,

\[
                         \sum_Sh(S)=E.                         \tag{4.10}
\]

For a coordinate \(v\), put \(h_v=\sum_{S\ni v}h(S)\) and

\[
                         q_v=E-h_v.                            \tag{4.11}
\]

Then \(0\le q_v\le E\), and

\[
 \sum_vq_v=2mE-(m-1)E=(m+1)E.                                \tag{4.12}
\]

There is an \(E\)-column zero-one matrix whose row sums are the \(q_v\)'s
and every column sum is \(m+1\).  Here is the complete cut check.  After
sorting the row sums, for every \(t\),

\[
 \sum_{i=1}^tq_i
 \le
 \begin{cases}
 tE,&t\le m+1,\\
 (m+1)E,&t\ge m+1.
 \end{cases}                                                  \tag{4.13}
\]

These are precisely the max-flow cut inequalities for sending \(q_v\)
units from coordinate \(v\), through unit-capacity coordinate--column
arcs, to \(E\) columns of demand \(m+1\).  Integral max flow therefore
gives the matrix.  Regard each column as an \((m+1)\)-set; their multiset
has an integral histogram \(g\ge0\), of mass \(E\), satisfying

\[
                         P_{m+1}g=q.                           \tag{4.14}
\]

Set \(u'=\mathbf1+g\).  It has no holes and mass \(N+E=W\).
The diamond identity for the full owner layer, together with the binomial
identity

\[
 2\binom{2m-1}{m-1}
 -\binom{2m-1}{m-2}
 -\binom{2m-1}{m}=E,                                         \tag{4.15}
\]

gives

\[
 P_{m+1}(u_C-\mathbf1)
 =E\mathbf1-(h_v)_{v\in[2m]}=q.                              \tag{4.16}
\]

Equations (4.14)--(4.16) prove (4.9).  The last assertion follows from
Theorem 3.3. \(\square\)

## 5. Reversal and complementation

Reversal changes the oriented sequence of transitions but not the
undirected edge set.  Therefore it changes neither \(\ell\), nor \(u\),
nor any defect.

On even ground, complementation preserves the middle layer.  If \(C^c\)
is the coordinatewise complement of \(C\), then edgewise

\[
 L(e^c)=\Omega\setminus U(e),\qquad
 U(e^c)=\Omega\setminus L(e).                                \tag{5.1}
\]

Thus complementation exchanges the two colour histograms, up to target
complementation.  In particular, it sends a lower-rainbow cycle to an
upper-rainbow one.  It is not, in general, a member of the fixed-owner,
fixed-lower trade fibre: it changes the owner set unless that set is
complement-closed, and it preserves the lower ledger only when the old
upper ledger already has the required complemented form.  Hence the two
endpoint states supplied by complementation do not by themselves give an
interpolating legal switch path.

## 6. Legal pentagon moves and exact repeat descent

Embed the complemented pentagon on a common \((m-3)\)-set \(K\) and a
six-set \(D\).  Its old and new tables consist of five internally
vertex-disjoint paths, with the same two ports in every row.  Suppose the
five old paths occur as five disjoint segments of a simple Hamilton cycle
\(C\).  Replace them simultaneously by the five new paths.

### Lemma 6.1 (ported legality)

The replacement gives another simple Hamilton cycle \(C'\), on the same
owners and with the same lower histogram.

#### Proof

Both path factors enumerate the same twenty local middle owners once, and
have the same endpoint pair in each of the five rows.  Contract the five
old segments of \(C\) to five labelled port-to-port edges.  Replacing each
segment by the corresponding new row leaves this contracted cycle
unchanged.  Expanding again therefore gives one cycle, not merely a
two-factor.  The internal owners remain distinct and the outside of the
cycle is untouched.  The two factors have the same lower ledger, so the
complete lower histogram is preserved. \(\square\)

Write the upper change as

\[
 \Delta=e_{A_1}+e_{A_2}+e_{A_3}
       -e_{D_1}-e_{D_2}-e_{D_3},                              \tag{6.1}
\]

where all six targets are distinct.  For an upper load \(u\), put

\[
                         R^+(u)=\sum_U(u(U)-1)_+.              \tag{6.2}
\]

### Lemma 6.2 (exact legal defect change)

For every legal pentagon move,

\[
 \boxed{
 R^+(u+\Delta)-R^+(u)
 =|\{j:u(A_j)\ge1\}|-|\{j:u(D_j)\ge2\}|.}                    \tag{6.3}
\]

#### Proof

Adding one unit increases \((x-1)_+\) exactly when \(x\ge1\).  Removing
one unit decreases it exactly when \(x\ge2\).  Sum these six independent
changes. \(\square\)

Thus a pentagon can alter upper defect in an actual Hamilton cycle; the
only local question is the occupancy score in (6.3).  The next section
gives a literal nonzero example.

## 7. A legal Hamilton defect-changing switch in \(J(6,3)\)

Consider the following cyclic list of all twenty three-subsets of \([6]\):

\[
\begin{aligned}
C_{\rm old}=(&346,236,126,125,
256,156,145,134,\\
&124,234,345,356,
456,245,235,123,\\
&135,136,146,246).
\end{aligned}                                                   \tag{7.1}
\]

The closing edge is \(246\,346\).  Replace the five complemented-pentagon
rows, preserving the same five connectors, to obtain

\[
\begin{aligned}
C_{\rm new}=(&346,146,145,125,
256,236,136,134,\\
&124,126,156,356,
456,345,234,123,\\
&135,235,245,246).
\end{aligned}                                                   \tag{7.2}
\]

### Theorem 7.1 (literal legal mobility)

The lists (7.1)--(7.2) are Hamilton cycles of \(J(6,3)\), related by one
legal complemented-pentagon switch.  Their lower histograms agree and
cover every two-subset.  Their upper statistics are

\[
\begin{array}{c|cc}
 &M^+&R^+\\ \hline
C_{\rm old}&2&7\\
C_{\rm new}&1&6.
\end{array}                                                     \tag{7.3}
\]

#### Proof

Each displayed list contains all twenty three-subsets exactly once.  The
five four-vertex blocks in (7.1) are, in order of rooted-pentagon row
labels,

\[
 3,5,2^{\rm rev},1,4^{\rm rev},                               \tag{7.4}
\]

and (7.2) uses the corresponding five new rows with the same orientations.
The connector edges are

\[
 125\!-\!256,\quad134\!-\!124,\quad356\!-\!456,\quad
 123\!-\!135,\quad246\!-\!346.                               \tag{7.5}
\]

Their intersections are respectively

\[
                         25,14,56,13,46,                       \tag{7.6}
\]

so they are Johnson edges.  All internal adjacencies are Johnson edges by
the two pentagon tables.  This proves Hamiltonicity and legal switch
equivalence.

In each path factor, the fifteen internal lower colours are all fifteen
two-subsets once.  The fixed connectors add one further copy of the five
colours in (7.6).  Hence the lower histograms agree and are complete.

For the old internal factor, the upper holes are

\[
                         1245,2356,                            \tag{7.7}
\]

and its repeated upper targets are \(1256,2345\), each of load two.  For
the new internal factor, the upper holes are

\[
                         1345,2346,                            \tag{7.8}
\]

and its repeated targets are \(1346,2345\), each of load two.  These lists
follow directly by taking the union of each adjacent pair in the five
displayed rows.

The connector upper targets are

\[
                         1256,1234,3456,1235,2346.             \tag{7.9}
\]

Thus (7.9) fills the new hole \(2346\) but neither old hole, while all its
other targets were already occupied in both states.  Therefore the old
cycle has two upper holes and the new one has one.  Since every Hamilton
cycle here has twenty edges and there are fifteen upper targets,

\[
                         M^+=15-20+R^+=R^+-5.                  \tag{7.10}
\]

This gives \(R^+=7\) and \(R^+=6\), proving (7.3). \(\square\)

The example is deliberately used only for the legal-mobility assertion.
It is a full-owner, lower-complete Hamilton cycle, so its five connector
edges repeat lower colours.  It is not a length-fifteen lower-rainbow
saturating cycle.

## 8. Exact proved boundary

The union-relevant algebraic trade space is now completely characterized:

\[
                         \mathcal T/(\mathcal T\cap\ker B_+)
                         \cong\ker_{\mathbb Z}P_{m+1}.         \tag{8.1}
\]

The orbit of one six-coordinate ported packet generates this quotient, and
Theorem 7.1 proves that its upper action can be nonzero inside the actual
Hamilton state space.  Hence a further search for a scalar, parity, or
linear union-defect invariant cannot close the depth-one problem.

Three genuinely nonlinear gates remain for a lower-rainbow saturating
cycle.

1. **Conformality.**  A formal decomposition of a desired ledger change
   may subtract edges absent from the current cycle.
2. **Port occurrence.**  A legal pentagon requires five prescribed
   port-to-port segments simultaneously.  The one-sided saturating-cycle
   theorem does not force such a forest.
3. **Connected binary lifting.**  Even if an upper ledger lies in the
   correct point-incidence fibre, a binary lift can be disconnected, and a
   signed lift need not have any binary representative.

Thus the precise next positive statement is a prescribed-ported-forest or
conformal augmentation theorem inside a point-balanced lower-rainbow
cycle.  The ledger lattice itself is no longer an obstruction.
