# A literal mixed-frame connector across the BTK sink, and the exact internal-surgery cuts

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

The natural terminal sink of one fixed BTK product frame is not a
frame-independent chronology obstruction. There is an explicit one-edge
frame change followed by a complete product atom which is accepted by the
actual two queues, is owner-disjoint from the preceding atom, and retains
every internal lower and upper target of both atoms.

Write

\[
                 m=2r+h,
\]

and suppose

\[
  H\ge 7,\qquad 3\le h\le H-1,\qquad H\le r.       \tag{0.1}
\]

After any legal history ending with a length-\(h\) product atom at its
high endpoint, one may make an internal-\(A\) seam and then traverse a
length-\(h\) atom in a coordinate-relabelled BTK frame in the opposite
direction.  The complete concatenation is literally \(H\)-safe.  The
low-end statement is the \(A\leftrightarrow B\) dual.  Alternating the two
constructions gives arbitrarily long chronology-safe occurrence routes.
Thus there is no local sink depending only on the current owner and its
two live queues once moving frames are admitted.

The connector also closes into an exact antipodal \(C_{2m}\) packet.
Starting with any length-\(h\) atom, one can partition all still-unused
coordinates into moving-frame atom blocks and internal seams so that the
first \(m\) edges form a geodesic from an owner to its complement.  Reuse
the same \(m\) support pairs, in the same order and opposite orientation,
to close a simple cycle.  Its support word is a permutation of \(m\)
disjoint pairs repeated at distance \(m\), so it is cyclically
\(H'\)-safe for every integer \(1\le H'\le m\).  It contains
\(\Theta(m/h)\) complete product atoms
and has exactly \(2m\) owners, the desired packet size for an
\(O(W/m)\)-component construction.

This is not yet an exact factor theorem.  The marker used below separates
each new atom from the immediately preceding atom, but independently
chosen new atoms can meet older atoms.  Simultaneous capacity-one owner
selection and simultaneous shadow dispersion remain unproved.

Internal surgery has a different exact boundary.

1. Surgery confined to the owner set of one monotone atom is trivial.
2. The smallest nontrivial owner-, degree-, and endpoint-preserving
   recoupling is the parallel-edge switch on a Johnson \(Q_2\).  Under an
   explicit fringe-disjointness condition it is chronology-legal.
3. A local-frame-independent half-rank potential, for a fixed outer
   bipartition, detects all same-half seams and, at every depth, all
   changes of direction inside one half.  Hence a
   surgery preserving both signed target multisets cannot freely use such
   moves.  Cross-half, orientation-coherent square circulations are the
   first potential-null internal-surgery escape.

Finally, an endpoint-current identity gives a genuine frame- and
surgery-independent global cut.  It becomes large only when all legal
paths share one weighted current obstruction.  Fixed BTK record tails do
not supply such a common weight; the connector constructed here is the
reason.

## 1. Exact chronology convention

For a finite route \(X_0,\ldots,X_L\), write

\[
 X_t\longrightarrow X_{t+1}=X_t-a_t+b_t,
 \qquad |X_t|=m.                                    \tag{1.1}
\]

Immediately before edge \(t\), retain the supports of edges

\[
                    \max\{0,t-H+1\},\ldots,t-1.     \tag{1.2}
\]

Equivalently, retain the recently inserted set \(I_t\subseteq X_t\)
and recently removed set \(R_t\subseteq X_t^c\).  The edge in (1.1) is
accepted exactly when

\[
                       a_t\notin I_t,
             \qquad   b_t\notin R_t.                \tag{1.3}
\]

Membership supplies the other two exclusions automatically.  A route is
two-sided \(H\)-safe if and only if no physical coordinate occurs in two
different edge supports in any \(H\)-edge window.  This is also exactly
the condition that, for every valid start \(t\) and
\(0\le q\le\min\{H,L-t\}\),

\[
 \left|\bigcap_{j=0}^{q}X_{t+j}\right|=m-q,
 \qquad
 \left|\bigcup_{j=0}^{q}X_{t+j}\right|=m+q.         \tag{1.4}
\]

The two live sets have a common size at most \(H-1\), although below it
is convenient to retain their separate intersections with the two
halves.

Fix a split

\[
                         [2m]=A\mathbin{\dot\cup}B,
             \qquad |A|=|B|=m.                      \tag{1.5}
\]

A length-\(h\) product diagonal has high endpoint type

\[
 |X\cap A|=r+h,\qquad |X\cap B|=r,\qquad m=2r+h.    \tag{1.6}
\]

It is traversed low-to-high by inserting \(h\) distinct \(A\)-labels
and removing \(h\) distinct \(B\)-labels.  The reverse traversal removes
the former and inserts the latter.

## 2. The queue-avoiding moving-frame connector

### Theorem 2.1 (literal high-end connector, with exact count)

Assume (0.1).  Let a two-sided \(H\)-safe route end by traversing a
complete length-\(h\) product-BTK atom \(P\) low-to-high, reaching its
high endpoint \(X\).  Let

\[
                   I\subseteq X,qquad R\subseteq X^c              \tag{2.1}
\]

be the actual live insertion and removal sets at \(X\).  Put

\[
 i_A=|I\cap A|,qquad
 d_A=|R\cap A|,qquad
 d_B=|R\cap B|.                                      \tag{2.2}
\]

There are exactly

\[
 \boxed{
 (r+h-i_A)(r-d_A)
 (r+h-i_A-1)_h(r+h-d_B)_h}                          \tag{2.3}
\]

distinct choices of the following form:

* an internal-\(A\) Johnson seam \(X\to Y=X-a+b\);
* an ordered length-\(h\) monotone product path \(Q\), beginning at
  \(Y\) and traversed high-to-low;

such that the seam and every edge of \(Q\) are accepted by the actual
queues.  Here \((u)_v=u(u-1)\cdots(u-v+1)\).

Every such \(Q\) is a complete product diagonal in a coordinate-conjugate
BTK frame on the same split \(A\dot\cup B\).  Moreover

\[
                         V(P)\cap V(Q)=\varnothing.   \tag{2.4}
\]

Consequently \(P;(X,Y);Q\) is a simple, literal, two-sided
\(H\)-safe route.

#### Proof

Choose

\[
        a\in(X\cap A)\setminus I,qquad
        b\in(A\setminus X)\setminus R,               \tag{2.5}
\]

and put \(Y=X-a+b\).  There are respectively

\[
                         r+h-i_A,qquad r-d_A          \tag{2.6}
\]

choices.  The seam is accepted by (1.3).  It preserves the half-rank in
(1.6), so \(Y\) is again a high endpoint of the correct radius.

Choose ordered lists of distinct labels

\[
 \begin{split}
 S=(s_1,\ldots,s_h)&\subseteq
       (Y\cap A)\setminus(I\cup\{b\}),\\
 T=(t_1,\ldots,t_h)&\subseteq
       (B\setminus Y)\setminus R.                    \tag{2.7}
 \end{split}
\]

The two available ground sets have exact sizes

\[
                    r+h-i_A-1,qquad r+h-d_B,         \tag{2.8}
\]

which proves the count (2.3).  Positivity is quantitative: since every
live set has size at most \(H-1\),

\[
 \begin{array}{rcl}
 r+h-i_A&\ge&h+1,\\
 r-d_A&\ge&1,\\
 r+h-i_A-1&\ge&h,\\
 r+h-d_B&\ge&h+1.
 \end{array}                                         \tag{2.9}
\]

Define

\[
             Q_j=Y-\{s_1,\ldots,s_j\}
                    +\{t_1,\ldots,t_j\},
             \qquad 0\le j\le h.                    \tag{2.10}
\]

This is not merely a formal Johnson path.  To install it as a BTK product
diagonal, write

\[
 U=(Y\cap A)\setminus S,\quad V=A\setminus Y,
 \qquad |U|=|V|=r,                                   \tag{2.11}
\]

and order the \(A\)-coordinates as

\[
        v_1,u_1,\ldots,v_r,u_r,s_h,s_{h-1},\ldots,s_1.       \tag{2.12}
\]

At \(Y\) the corresponding word is \((01)^r1^h\), and descending its
BTK chain removes \(s_1,s_2,\ldots,s_h\) in that order.  Similarly put

\[
 Z=Y\cap B,\quad W=(B\setminus Y)\setminus T,
 \qquad |Z|=|W|=r,                                   \tag{2.13}
\]

and order the \(B\)-coordinates as

\[
             w_1,z_1,\ldots,w_r,z_r,t_1,t_2,\ldots,t_h.     \tag{2.14}
\]

At \(Y\) this word is \((01)^r0^h\), and ascending its BTK chain inserts
\(t_1,t_2,\ldots,t_h\).  The rank-\(m\) product diagonal is exactly
(2.10).

It remains to check the actual FIFO chronology.  Each \(s_j\) avoids all
old live insertions and the seam insertion \(b\).  It cannot equal an
earlier new insertion, because \(S\subset A\) and \(T\subset B\).  Each
\(t_j\) avoids every old live removal; it cannot equal the seam removal
\(a\) or an earlier new removal, again because the halves differ.  The
lists themselves have no repetitions.  Hence (1.3) accepts every edge of
\(Q\), with no appeal to a queue reset or to expiration.

Finally, \(b\) is absent from the high endpoint \(X\) of \(P\).  Since
\(P\) reaches \(X\) by inserting \(A\)-labels, \(b\) is absent from
every owner of \(P\).  The seam inserts \(b\), and (2.7) forbids its
removal in \(Q\), so \(b\) belongs to every owner of \(Q\).  This proves
(2.4).  Each atom is itself simple, and the seam joins their two disjoint
owner sets, completing the proof. \(\square\)

### Corollary 2.2 (this really changes the fixed frame)

Under the hypotheses of Theorem 2.1, the atom \(Q\) cannot be the
successor atom from the same fixed BTK product frame as \(P\).

#### Proof

The audited fixed-frame sink theorem says that for \(h\ge3\) and
\(H\ge7\), no direct endpoint seam followed by a complete atom of that
same frame is accepted after the natural traversal of \(P\).  The route
in Theorem 2.1 is accepted.  Therefore its successor frame is genuinely
different. \(\square\)

### Corollary 2.3 (low end and indefinite occurrence-level continuation)

At a low endpoint, interchange \(A\) and \(B\) in Theorem 2.1.  Thus an
internal-\(B\) seam followed by a low-to-high atom in a new frame is
accepted.  With

\[
 i_B=|I\cap B|,qquad d_A=|R\cap A|,qquad d_B=|R\cap B|,
\]

the exact low-end count is

\[
 \boxed{
 (r+h-i_B)(r-d_B)
 (r+h-i_B-1)_h(r+h-d_A)_h.}                          \tag{2.14a}
\]

Alternating high- and low-end constructions produce, for
every finite \(N\), a chronology-safe route through \(N\) complete
length-\(h\) product-atom occurrences.

This induction is only in the occurrence graph.  The marker at the
\(j\)-th seam separates atom \(j\) from atom \(j+1\); it does not prevent
atom \(j+1\) from meeting an atom used much earlier.  Thus Corollary 2.3
does not assert an owner factor.

### Theorem 2.4 (an exact antipodal \(C_{2m}\) moving-frame packet)

Under (0.1), let \(P\) run from its low endpoint \(U\) to its high
endpoint \(X\), and write \(U_A=U\cap A\), \(X_A=X\cap A\), and
similarly in \(B\).  There is a simple cycle

\[
                  {\cal C}=(Z_0,Z_1,\ldots,Z_{2m-1})
                  \cong C_{2m}                         \tag{2.15}
\]

such that:

1. \((Z_0,\ldots,Z_h)=P\);
2. \(Z_{j+m}=Z_j^c\) for every \(j\pmod m\);
3. the cyclic support word is \(H'\)-safe for every integer
   \(1\le H'\le m\);
4. each half of the cycle contains

   \[
             1+2\left\lfloor{r\over h+1}\right\rfloor       \tag{2.16}
   \]

   complete length-\(h\) product-BTK atoms, each allowed its own explicit
   coordinate frame.

If \(h=o(m)\), the number in (2.16) is
\((1+o(1))m/(h+1)\).  If also \(h\to\infty\), this is
\((1+o(1))m/h\).

#### Proof

Let \(S_A=X_A\setminus U_A\) and
\(S_B=U_B\setminus X_B\) be the \(h\) inserted and removed labels of
\(P\).  The four unused pools

\[
 A^-=U\cap A,qquad A^+=A\setminus X,qquad
 B^-=X\cap B,qquad B^+=B\setminus U                 \tag{2.17}
\]

all have size \(r\).  Here the expressions involving complements in
(2.17) are understood inside their indicated halves.  These pools are
disjoint from \(S_A\cup S_B\).

Put

\[
             t=\left\lfloor{r\over h+1}\right\rfloor,
             \qquad s=r-t(h+1),qquad0\le s<h+1.      \tag{2.18}
\]

Partition each of the four pools into \(t\) blocks of size \(h+1\) and
one residual block of size \(s\).  Starting at \(X\), perform the
following four operations in each round:

1. an internal-\(A\) seam removing one unused label of \(A^-\) and
   inserting one unused label of \(A^+\);
2. a high-to-low length-\(h\) product atom removing the other \(h\)
   labels of that \(A^-\)-block and inserting \(h\) labels of the
   corresponding \(B^+\)-block;
3. an internal-\(B\) seam removing one unused label of \(B^-\) and
   inserting the remaining label of that \(B^+\)-block;
4. a low-to-high length-\(h\) product atom removing the other \(h\)
   labels of that \(B^-\)-block and inserting the other \(h\) labels of
   the corresponding \(A^+\)-block.

After every round the current owner is again of high type.  The two atom
words in a round are arbitrary ordered cross-half active words, so the
explicit ordering argument in (2.11)--(2.14), with the two halves or
orientations interchanged as necessary, installs each as a complete BTK
product diagonal.  Every round consumes exactly \(h+1\) labels from each
pool.  After the \(t\) rounds, pair the \(s\) residual \(A^-\)-labels
with the residual \(A^+\)-labels by internal-\(A\) swaps, and do the same
with the two residual \(B\)-pools.

The resulting first-half length is exactly

\[
                  h+2t(h+1)+2s=h+2r=m.               \tag{2.19}
\]

Its edge supports use every physical coordinate exactly once.  More
explicitly, they give disjoint pairs

\[
              e_j=\{u_j,v_j\},qquad
              u_j\in U,\quad v_j\in U^c,\quad1\le j\le m,  \tag{2.20}
\]

in an order whose first \(h\) edges are \(P\).  Thus

\[
 Z_j=U-\{u_1,\ldots,u_j\}+\{v_1,\ldots,v_j\},
 \qquad0\le j\le m,                                  \tag{2.21}
\]

is a monotone geodesic from \(U\) to \(U^c\).

For the second half, use \(e_1,e_2,\ldots,e_m\) again in the same order,
but remove \(v_j\) and insert \(u_j\).  Hence

\[
 Z_{m+j}=U^c-\{v_1,\ldots,v_j\}+\{u_1,\ldots,u_j\}
          =Z_j^c,qquad0\le j\le m.                  \tag{2.22}
\]

The complement of every first-half product block is again an arbitrary
ordered monotone product block and therefore has a coordinate-BTK frame.

It remains to check simplicity and cyclic chronology.  In the first half,
the chosen member of pair \(e_k\) is \(v_k\) exactly when \(k\le j\).
In the second half it is \(u_k\) exactly when \(k\le j\).  These two
prefix patterns cannot agree at internal indices; the only repeated owner
is \(Z_{2m}=Z_0\).  Thus (2.15) is a simple \(2m\)-cycle.

Its cyclic support word is

\[
                       e_1,e_2,\ldots,e_m,
                       e_1,e_2,\ldots,e_m.             \tag{2.23}
\]

The \(e_j\) are pairwise coordinate-disjoint, and the two occurrences of
each are exactly \(m\) edges apart in either cyclic direction.  Every
window of at most \(m\) consecutive edges therefore contains each
physical coordinate at most once.  This proves cyclic \(H'\)-safety for
all \(1\le H'\le m\).  The construction used one initial atom and two atoms in
each round, proving (2.16). \(\square\)

### Corollary 2.5 (exact sign balance of one packet)

For every \(q\le H\), let \(L_{j,q}\) and \(U_{j,q}\) denote the
intersection and union of the cyclic \(q\)-window beginning at \(Z_j\).
Then

\[
                         L_{j+m,q}=(U_{j,q})^c.        \tag{2.24}
\]

Equivalently, \(U_{j+m,q}=(L_{j,q})^c\).

Consequently the packet has equally many distinct lower and upper targets
and exactly equal lower and upper hole counts.  It also retains every
internal window of every constituent product atom.  Thus

\[
 \operatorname{Supp}^{\pm}_q({\cal C})
 \supseteq
 \bigcup_{R\text{ a constituent atom}}
          \operatorname{Supp}^{\pm}_q(R).             \tag{2.25}
\]

This remains relative support monotonicity: the packet may occupy owners
belonging to other atoms of a reference factor, whose displaced target
towers are not accounted for by (2.25).

At the Gaussian atom scale \(h=\Theta(\sqrt m)\), one packet absorbs
\(\Theta(\sqrt m)\) whole-atom occurrences into one component.  An
owner-disjoint near-packing of these packets would have

\[
                       K=O(W/m),
 \qquad HK=O(HW/m)=o(W)\quad(H=o(m)).                 \tag{2.26}
\]

Thus Theorem 2.4 reaches the exact component scale required by the
coefficient-one compiler.  Only the owner-packing and displaced-shadow
ledgers are missing.

## 3. Complement and exact shadow ledger

For a route \({\cal R}=(X_0,\ldots,X_L)\), put

\[
             {\cal R}^{\dagger}=(X_L^c,\ldots,X_0^c).       \tag{3.1}
\]

Coordinate complementation exchanges inserted and removed queues, and
reversal restores forward chronology.  Hence \({\cal R}^{\dagger}\) is
\(H\)-safe whenever \({\cal R}\) is.  Every dagger atom is again an
ordered monotone product path and is therefore realized by some
coordinate-conjugate BTK frame; this need not be the original fixed
frame.

For the two-atom block in Theorem 2.1, \(L=2h+1<m\).  Indeed (0.1) gives
\(m=2r+h\ge2H+h>2h+1\).  No two owners of the block are complementary:
their Johnson distance is at most their distance along the block, which
is at most \(L<m\), whereas complementary middle owners have Johnson
distance \(m\).  Therefore

\[
                  V({\cal R})\cap V({\cal R}^{\dagger})
                  =\varnothing.                       \tag{3.2}
\]

The length hypothesis is essential; dagger-disjointness is not automatic
for an arbitrary long route.

For \(q\le H\), define

\[
 \begin{split}
 \operatorname{Supp}_q^-({\cal R})
 &=\left\{\bigcap_{j=0}^{q}X_{t+j}:0\le t\le L-q\right\},\\
 \operatorname{Supp}_q^+({\cal R})
 &=\left\{\bigcup_{j=0}^{q}X_{t+j}:0\le t\le L-q\right\}.
                                                               \tag{3.3}
 \end{split}
\]

Fusion in Theorem 2.1 deletes no internal window of either atom.  Hence,
for both signs and every \(q\le H\),

\[
 \boxed{
 \operatorname{Supp}_q^{\pm}(P;(X,Y);Q)
 \supseteq
 \operatorname{Supp}_q^{\pm}(P)
 \cup
 \operatorname{Supp}_q^{\pm}(Q).}                    \tag{3.4}
\]

Every additional crossing window has the correct rank by literal
\(H\)-safety.  Thus the fusion has zero missing-shadow loss relative to
the union of the already selected open atoms \(P,Q\).  Equation (3.4)
does not say that different crossing windows have different targets, nor
that independently selected atoms give global support.  If one replaces
an old seam or an old collar, its deleted targets must be charged by the
exact support identity

\[
 M_q^{\rm new}-M_q^{\rm old}
   =|Z_q\cap U_q^{\rm old}|-|Z_q\cap U_q^{\rm new}|, \tag{3.5}
\]

where \(Z_q\) is the set of targets unsupported by the unchanged
background.  Chronology alone never implies (3.5) is nonpositive.

## 4. Why the fixed sink disappears

Suppose complete monotone atoms \(P,Q\), together with a connector of
\(d\) edges, have total length at most \(H\).  Then all their edge
supports lie in one protected window.  Since the supports inside either
monotone atom are already pairwise disjoint, the concatenation is
\(H\)-safe if and only if

1. every connector support is fresh, and
2. the active coordinate sets of \(P\) and \(Q\) are disjoint.

For one direct high-end seam, condition 2 is precisely

\[
 S_A(P)\cap S_A(Q)=\varnothing,qquad
 S_B(P)\cap S_B(Q)=\varnothing.                       \tag{4.1}
\]

The fixed BTK record-tail theorem forces a label in these intersections
within the last and first three atom edges, giving inclusive span at most
seven.  Theorem 2.1 chooses both new ordered active alphabets outside the
actual live supports, so (4.1) holds.  The obstruction is therefore
coherence of one fixed active-word catalogue, not finite-memory entropy.

There is a useful robust remnant.  For equal length-\(h\) atoms in one
fixed BTK frame, after a \(d\)-edge endpoint displacement the certified
active-tail overlap is at least

\[
                              h-4d.                   \tag{4.2}
\]

This is the record-tail Lipschitz lemma proved in
`MATH_OBSTRUCTION_BTK_EXPIRATION_COLLAR_LINEAR_MASS_TOLL_20260726.md`;
no orbit averaging is used in it.

If surgery deletes or replaces at most \(b_P,b_Q\) relevant carrier
transitions in the two atoms, a repeated carrier remains whenever

\[
                         4d+b_P+b_Q<h.                \tag{4.3}
\]

If the retained pieces and connector still fit in one \(H\)-window, this
repeat makes the route illegal.  Hence \(d,b_P,b_Q=o(h)\) cannot repair
the fixed frame in the Gaussian regime \(H/h\to\infty\).  The connector
of Theorem 2.1 escapes (4.3) by replacing an entire length-\(h\) active
word: it is an active-alphabet avalanche, not a bounded edit.

## 5. Exact internal-atom surgery

### Lemma 5.1 (one-atom owner rigidity)

Let \(P=(X_0,\ldots,X_h)\) be a monotone product diagonal.  Then

\[
                         d_J(X_i,X_j)=|i-j|.           \tag{5.1}
\]

Consequently the Johnson graph induced on \(V(P)\) is exactly the path
\(P\).  Any spanning owner-preserving surgery whose new edges all remain
inside \(V(P)\) is \(P\) or its reversal.

#### Proof

Between positions \(i<j\), the path removes \(j-i\) distinct labels and
inserts \(j-i\) distinct labels, none used elsewhere.  Thus
\(|X_i\setminus X_j|=|X_j\setminus X_i|=j-i\), proving (5.1).  Two
owners in the induced graph are adjacent exactly when their indices
differ by one.  A spanning path in this induced path graph has only its
two orientations. \(\square\)

Thus genuine internal surgery must use at least two old atoms or introduce
new owners.

### Lemma 5.2 (the minimal two-atom square switch)

Let \(C\) be an \((m-2)\)-set and let
\(e_0,e_1,f_0,f_1\notin C\) be distinct.  Put

\[
 V_{ij}=C\cup\{e_i,f_j\},qquad i,j\in\{0,1\}.       \tag{5.2}
\]

The replacement

\[
 \{V_{00}V_{10},V_{01}V_{11}\}
 \longleftrightarrow
 \{V_{00}V_{01},V_{10}V_{11}\}                      \tag{5.3}
\]

preserves the four owners, their degrees, and their exposed endpoint set,
and is the unique nontrivial parallel-edge recoupling on this \(Q_2\).

Suppose that, for each proposed new seam, its axis support together with
the incoming suffix and outgoing prefix through \(H-1\) edges are
pairwise coordinate-disjoint.  If the two resulting collars can meet
again within \(H\) edges, require the same condition on their joint cyclic
window (disjoint collars are a sufficient special case).  Then installing
the new shore of (5.3) and pairing the four old pieces accordingly gives
literal \(H\)-safe routes.

#### Proof

The owner, degree, and endpoint assertions are immediate from (5.2).  The induced
graph is a four-cycle; its two perfect matchings are exactly the two
shores of (5.3), proving uniqueness.  Under the stated fringe condition,
each new seam support is disjoint from every support with which it can
share an \(H\)-window.  The two parallel new seams have the same axis
support, but they lie on different routed pieces.  If those pieces are
subsequently joined, the joint-collar hypothesis requires the seams to be
more than \(H-1\) edges apart.  Thus no protected window sees the repeated
axis, and (1.3) accepts both recoupled routes. \(\square\)

Lemma 5.2 is a conditional chronology and owner connector, not an
existence or abundance theorem for suitable squares inside the fixed BTK
atlas, and not a missing-shadow theorem.  For full interior or cyclic
collars, at depth \(q\) a separated square recoupling deletes \(2q\) old
crossing occurrences and creates \(2q\) new ones per sign.  Path-boundary
truncation changes this number.  In either case the old and new columns
need not agree.  The exact zero-loss condition is still (3.5), with the
actual boundary counts, summed over the chosen squares.

## 6. A frame-independent potential for internal surgery

Fix the same physical split \(A\dot\cup B\) and define

\[
                    \phi(Z)=|Z\cap A|^2+|Z\cap B|^2. \tag{6.1}
\]

All results in this section are independent of the SCD, coordinate order,
and local frame **relative to this fixed outer bipartition**.  They do not
obstruct an atlas which changes the outer split itself.

### Theorem 6.1 (all-depth half-rank defect)

Let \(X_0,\ldots,X_q\), \(q\le H\), be an \(H\)-safe window.  In its
\(q\) exchanges, let \(r_A,i_A\) be the numbers of removed and inserted
\(A\)-coordinates, and define \(r_B,i_B\) similarly.  With

\[
                    L=\bigcap_{j=0}^qX_j,qquad
                    U=\bigcup_{j=0}^qX_j,             \tag{6.2}
\]

one has the exact identity

\[
 \boxed{
 \phi(L)+\phi(U)-\phi(X_0)-\phi(X_q)
        =2(r_Ai_A+r_Bi_B).}                           \tag{6.3}
\]

In particular the defect is nonnegative.  It vanishes exactly when, in
each half separately, the window uses coordinates in at most one of the
two roles.

#### Proof

Let \(a=|X_0\cap A|\).  Safety makes all exchanged coordinates distinct,
so the four relevant \(A\)-counts are

\[
                 a-r_A,\quad a+i_A,\quad a,\quad
                 a-r_A+i_A.                           \tag{6.4}
\]

Therefore

\[
 (a-r_A)^2+(a+i_A)^2-a^2-(a-r_A+i_A)^2=2r_Ai_A.      \tag{6.5}
\]

The identical calculation in \(B\) proves (6.3). \(\square\)

Every internal window of an oriented product diagonal has zero defect:
one half only inserts and the other only removes.  A window which reverses
direction has positive defect.  For example, a block containing \(u\)
up-moves and \(v\) down-moves, all cross-half and all support-disjoint,
has

\[
               r_Ai_A+r_Bi_B=2uv,qquad
               \text{defect}=4uv.                    \tag{6.6}
\]

### Corollary 6.2 (cyclic target-multiset invariant)

For a cyclic \(H\)-safe owner route \((X_t)_{t\in\mathbb Z/n\mathbb Z}\),
where the cyclic \(q\)-windows are defined and safe (in particular
\(q<n\)), sum (6.3) over all cyclic starts.  Then

\[
 \boxed{
 \sum_t\bigl(\phi(L_{t,q})+\phi(U_{t,q})\bigr)
 =2\sum_t\phi(X_t)
  +2\sum_t(r_A(t)i_A(t)+r_B(t)i_B(t)).}               \tag{6.7}
\]

Thus an owner-preserving surgery which preserves both signed depth-\(q\)
target multisets preserves the total defect in (6.7).  It cannot replace
zero-defect windows by positive-defect windows unless it removes equal
defect elsewhere.

This is a multiset statement.  For support-only objectives it upgrades to
multiset equality only when all of the following hold separately at the
relevant sign and depth: every removed old column is locked by the
unchanged background, the affected old columns are distinct, and the old
and new affected occurrence counts agree.  Internal product-SCD windows
do have the required distinctness.  Indeed, if

\[
                         X_i=C_i\cup D_{m-i},          \tag{6.7a}
\]

then

\[
 L_{i,q}=C_i\cup D_{m-i-q},
 \qquad
 U_{i,q}=C_{i+q}\cup D_{m-i}.                         \tag{6.7b}
\]

The two half restrictions, the fixed half-SCD partitions, and the ranks
recover \(C,D,i\), so each internal lower map and each internal upper map
is injective.  Later seam or collar windows can nevertheless witness the
same target and destroy lockedness.  Without the full locked condition,
target recycling can hide the potential change.

### Corollary 6.3 (depth-one same-half invariant)

For any Johnson edge \(e=XY\), with \(L=X\cap Y\) and \(U=X\cup Y\),

\[
 \boxed{
 \phi(L)+\phi(U)
 =\phi(X)+\phi(Y)+2\mathbf 1_{\{e\text{ is same-half}\}}.}  \tag{6.8}
\]

Consequently, for every path/cycle cover graph \(G\),

\[
 \sum_{e\in G}\bigl(\phi(L_e)+\phi(U_e)\bigr)
 =\sum_X d_G(X)\phi(X)+2E_{\rm same}(G).              \tag{6.9}
\]

If owner degrees and both depth-one target multisets are preserved, then
\(E_{\rm same}\) is invariant.  In particular a product-diagonal atlas,
whose internal edges are all cross-half, cannot acquire a same-half edge
under an exact column-preserving, endpoint-preserving surgery.

For path covers with the same owner set and the same number of paths, let
\({\cal E}_0,{\cal E}_1\) be the old and new endpoint-deficit multisets;
an ordinary path contributes its two endpoints and an isolated owner
contributes two copies.  If the old edges are all cross-half and both
depth-one target multisets are preserved, then

\[
 2E_{\rm same}(G_1)
   =\sum_{X\in{\cal E}_1}\phi(X)
     -\sum_{X\in{\cal E}_0}\phi(X).                  \tag{6.10}
\]

Writing \(\eta(X)=2|X\cap A|-m\), the constants cancel and this is

\[
 \boxed{
 4E_{\rm same}(G_1)
   =\sum_{X\in{\cal E}_1}\eta(X)^2
     -\sum_{X\in{\cal E}_0}\eta(X)^2.}              \tag{6.11}
\]

Thus same-half seams can be paid for only by moving path endpoints outward
in squared half-height, or by changing/recycling depth-one columns.

Applied to Lemma 5.2, if the old \(e\)-edges are cross-half and the new
\(f\)-edges are same-half, the combined new lower-plus-upper potential
exceeds the old value by exactly \(4\).  No nonempty collection of such
squares can be exact zero-loss when its deleted depth-one columns are
locked.  If both axes are cross-half, the depth-one potential difference
is zero.  Hence a cross-half square circulation, with orientation coherent
inside every protected window, is the first internal-surgery move not
excluded by this invariant.  Higher-depth column routing remains to be
proved.

The qualification about the outer split is essential.  If one averages
(6.3) over all balanced choices of \(A\), then for fixed disjoint removal
and insertion sets of size \(q\),

\[
 \mathbb E_A(r_Ai_A+r_Bi_B)
                    ={q^2(m-1)\over2m-1},             \tag{6.12}
\]

independent of their routing.  Full outer-frame symmetrization therefore
erases this quadratic separator.

### Corollary 6.4 (quantitative locked-column demand at a reversal)

Fix a depth \(q\).  Consider an owner-preserving cyclic or local exchange
for which the affected old \(q\)-windows have zero defect, the sum of
their two endpoint potentials is unchanged, and all affected middle
endpoints obey

\[
                         |2|X\cap A|-m|\le B.          \tag{6.13}
\]

Put

\[
              D_q=\sum_{\text{new affected windows}}
                    (r_Ai_A+r_Bi_B).                  \tag{6.14}
\]

Assume that the affected old signed columns are distinct and that old and
new affected occurrence counts agree.  If all but \(u_q\) of the combined
lower and upper columns are locked and reproduced, then

\[
 \boxed{
                         u_q\ge {4D_q\over(B+q)^2}.}   \tag{6.15}
\]

#### Proof

At either fixed target rank, subtract the rank-dependent constant from
\(\phi\).  The remaining term is one half the square of the target's
half-imbalance.  A safe \(q\)-window whose middle endpoints satisfy
(6.13) has target half-imbalance at most \(B+q\).  Thus one unlocked
combined column can absorb potential drift at most \((B+q)^2/2\).
Theorem 6.1 says that the total new-minus-old drift is \(2D_q\).  Division
gives (6.15). \(\square\)

For one fully exposed change from at least \(q\) coherent up-edges to at
least \(q\) coherent down-edges, the crossing \(q\)-windows have splits
\(a,q-a\), \(1\le a<q\).  Therefore

\[
 D_q=2\sum_{a=1}^{q-1}a(q-a)
                  ={q(q^2-1)\over3},                 \tag{6.16}
\]

and

\[
               u_q\ge {4q(q^2-1)\over3(B+q)^2}.      \tag{6.17}
\]

When \(B=O(q)\), this is \(\Omega(q)\) changed or unlocked columns at
depth \(q\), hence \(\Omega(H^2)\) through depths \(q\le H\) if the
same scale relation holds throughout.  An unlocked column may be supplied
by an unchanged duplicate rather than becoming a hole, so (6.17) is an
exact recycling-demand bound, not an unconditional hole lower bound.

## 7. The genuine frame-independent global current cut

The moving-frame connector rules out a local frame-independent sink.  A
global endpoint current nevertheless survives every frame change and
every internal surgery.

Let

\[
 \begin{split}
 {\cal V}_0&=\{X:|X\cap A|=r\},\\
 {\cal V}_h&=\{X:|X\cap A|=m-r\},\\
 N_r&=|{\cal V}_0|=|{\cal V}_h|=\binom mr^2,
 \qquad h=m-2r.                                      \tag{7.1}
 \end{split}
\]

Let \({\cal P}\) be any owner-disjoint family of
\(M=N_r-\ell\) directed Johnson paths from distinct owners of
\({\cal V}_0\) to distinct owners of \({\cal V}_h\).  The paths may
backtrack internally and may use arbitrary frames and surgeries.  For
\(z\in A\), put

\[
 j_z(P)=\#\{\text{insertions of }z\text{ on }P\}
        -\#\{\text{removals of }z\text{ on }P\}.     \tag{7.2}
\]

Let \(L_0(z),L_h(z)\) count boundary owners containing \(z\) which were
not selected as starts and ends, respectively.  These are unselected
endpoint slots; a path allowed to backtrack may still visit such a
boundary owner internally.

### Theorem 7.1 (exact signed-current identity and weighted dual)

For every \(z\in A\),

\[
 \boxed{
 \sum_{P\in{\cal P}}j_z(P)
   ={h\over m}N_r-L_h(z)+L_0(z),
 \qquad
 \left|\sum_Pj_z(P)-{h\over m}N_r\right|\le\ell.}   \tag{7.3}
\]

More generally, let \(\psi_z\ge0\), and put

\[
 \Psi=\sum_{z\in A}\psi_z,qquad
 K_\psi=\max_{S\in\binom A{m-r}}\sum_{z\in S}\psi_z.       \tag{7.4}
\]

If every legal path under consideration satisfies

\[
                 \sum_{z\in A}\psi_zj_z(P)\le\beta,        \tag{7.5}
\]

then, whenever numerator and denominator are positive,

\[
 \boxed{
 \ell\ge
 N_r\,{(h/m)\Psi-\beta\over K_\psi-\beta}.}         \tag{7.6}
\]

#### Proof

For each path, (7.2) telescopes to
\(1_{\{z\in X_{\rm end}\}}-1_{\{z\in X_{\rm start}\}}\).
Among all high boundary owners, exactly
\((m-r)N_r/m\) contain \(z\); among all low boundary owners, exactly
\(rN_r/m\) contain it.  Subtracting the unselected endpoint incidences
proves the equality in (7.3).  Both endpoint-deficit counts lie in
\([0,\ell]\), so their
difference has absolute value at most \(\ell\).

After weighting and summing (7.3), the total current is at least

\[
                         {h\over m}N_r\Psi-\ell K_\psi.      \tag{7.7}
\]

On the other hand (7.5) bounds it above by
\((N_r-\ell)\beta\).  Rearrangement gives (7.6). \(\square\)

For \(\psi=1_{\{z\}}\) and \(\beta=0\), Theorem 7.1 gives the sharp
common-forbidden-coordinate endpoint deficit

\[
                              \ell\ge {h\over m}N_r.  \tag{7.8}
\]

Sharpness here is in the unrestricted owner-only slab.  Split the layered
monotone network according as \(z\) is always absent or always present.
In the absent sector the smaller boundary has \((r/m)N_r\) owners, and
in the present sector the smaller boundary has the same size.  Every
intermediate sector layer, of size say \(v_t\), is at least this large.
Consecutive layers are
biregular, so placing uniform load \((r/m)N_r/v_t\le1\) on a layer and
splitting it uniformly over outgoing edges gives a conserved fractional
flow of value \((r/m)N_r\) in each sector.  Vertex splitting and integral
max flow give owner-disjoint integral paths.  The two sectors therefore
pack exactly

\[
                       {2r\over m}N_r
                       =\left(1-{h\over m}\right)N_r, \tag{7.9}
\]

leaving exactly (7.8).  These attaining paths are monotone, so in this
sharpness construction the endpoint deficit is also a literal unused
boundary-owner leave.

This cut is completely independent of BTK, chronology, or internal path
shape.  Its missing premise in the present problem is commonality: the
terminal record obstructions of different fixed-frame atoms do not force
one weight \(\psi\) satisfying (7.5) with a positive gap.  Theorem 2.1
chooses atom-specific fresh active alphabets, so no such common local
weight follows from the fixed BTK sink.

## 8. Exact proved boundary

The following statements are proved here.

1. Under (0.1), every actual high-end queue state admits the explicit
   moving-frame continuation counted in (2.3); the low-end dual also
   holds.
2. The new atom is a literal complete product-BTK diagonal in an explicitly
   specified coordinate order, not a signed or fractional relaxation.
3. Consecutive atoms are owner-disjoint, the complete chronology is
   \(H\)-safe, and dagger pairing is owner-disjoint under the proved
   length inequality.
4. Every initial atom extends to the exact complement-equivariant
   \(C_{2m}\) packet of Theorem 2.4.  It is cyclically \(H\)-safe, has the
   correct \(\Theta(m)\) owner mass, and contains \(\Theta(m/h)\) whole
   moving-frame atoms.
5. Fusion retains all internal targets of the two selected atoms at every
   depth, as in (3.4).
6. Bounded fixed-frame editing remains obstructed by (4.3); the positive
   connector necessarily makes a \(\Theta(h)\) active-word change.
7. One-atom owner-preserving surgery is trivial.  The \(Q_2\) switch is
   the minimal exact owner-, degree-, and endpoint-preserving two-atom
   recoupling, with a literal sufficient chronology condition.
8. The all-depth potential identity (6.3), its cyclic sum (6.7), the
   depth-one edge identity (6.8), and the endpoint ledger (6.11) are exact
   surgery constraints relative to a fixed outer split.
9. The signed-current theorem (7.3)--(7.6) is an exact global cut valid
   under arbitrary frames, backtracking, and internal surgery.

The following statements are not proved.

1. The independently rooted \(C_{2m}\) packets have not been packed with
   owner capacity one.  Consecutive disjointness inside one packet does not
   imply disjointness of different packets.
2. The connector does not prove target uniqueness or global
   aggregate \(o(W)\) missing shadow.  Equation (3.4) is relative to the
   two atoms already selected.
3. Cross-half \(Q_2\) circulations pass the potential test but have not
   been routed through all depths or packed globally.
4. No common current weight with a coefficient-scale gap has been derived;
   hence Theorem 7.1 is a dual template, not a new lower bound for the full
   moving-frame problem.

The smallest remaining positive hypothesis is therefore an integral
packing of the antipodal configurations in Theorem 2.4 (or of
potential-null cross-half square columns) which covers all but \(o(W)\)
owners and has aggregate all-depth missing shadow \(o(W)\).  Such a
packing would already have \(O(W/m)\) components and exact sign balance.
The fixed BTK sink supplies no further local obstruction to that
hypothesis.
