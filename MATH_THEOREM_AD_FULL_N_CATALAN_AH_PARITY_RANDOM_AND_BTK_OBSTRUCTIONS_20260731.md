# Full-\(N\) uniformly directed Catalan repair: critical sparsity, dummy antisymmetry, and the BTK edit barrier

Date: 2026-07-31  
Status: exact all-dimension obstructions to the direct AH, independent-random,
ordinary exterior-parity, and canonical BTK/SCD routes; no all-\(m\)
directed-repair construction is claimed

## 0. Verdict

Put

\[
 M=\binom{2m}{m},\qquad
 N=\binom{2m}{m+1}=mK,\qquad
 K=\operatorname {Cat}_m,
 \qquad m\ge2.
\]

The full-\(N\)-host signed formulation for the uniformly outgoing directed
subclass does not acquire the reserve needed by the standard black-box
matching theorems.  The unrestricted one-of-two switch has twice as many
records and an additional endpoint resource; it is not claimed to be
covered by the catalogue and parity statements below.

1. Its directed repair catalogue has exactly \(mK=N\) records.  The host
   and lower-colour shores both have average degree exactly one.  Thus no
   high-degree quasiregular nibble hypothesis follows from Boolean
   incidence.
2. The exact full-\(N\) dummy-token formulation is a rainbow matching of
   \(N\) graph families.  Aharoni--Haxell asks for matching number
   \(>2(N-1)\), while the resource graph has matching number at most \(N\).
3. With \(q=N-K=(m-1)K\) labelled dummy tokens, every uniformly outgoing
   physical repair has exactly \(q!\) perfect-matching lifts.  Ordinary
   mod-two parity and every dummy-antisymmetric exterior sum therefore
   vanish for every \(m\ge2\).
4. Uniform random host banks are a linear Hamming distance from the
   necessary source bank in the floor case, with probability tending to
   one.  Independent Bernoulli host sampling leaves linearly many omitted
   facets with no selected host, with fully quantified dependency.
5. The standard BTK two-rank matching, every coordinate conjugate, and
   every \(o(K)\)-perturbation have no Hamilton physical lift.  There are
   \(\operatorname {Cat}_{m-3}>K/64\) disjoint three-edge overload
   certificates.

These are route obstructions, not an obstruction to an arbitrary
\(\Theta(K)\)-scale correlated rethread.  The scalarized determinant
coefficient from the hypergraph-flow note also remains open because it
quotients out the dummy symmetry.

## 1. The full directed catalogue is critically sparse

Use a saturating cycle

\[
 C_0,U_0,C_1,U_1,\ldots,C_{N-1},U_{N-1},C_0
 \tag{1.1}
\]

and put

\[
 {\cal E}=\binom{[2m]}m\setminus\{C_i:i\in\mathbb Z_N\},
 \qquad
 {\cal L}=\binom{[2m]}{m-1},
 \qquad
 b_i=C_i\cap C_{i+1}.
 \tag{1.2}
\]

For the uniformly outgoing convention, a directed repair record is

\[
                    (X,i,t_i(X)),\qquad
 t_i(X)=X\cap C_{i+1},\qquad X\subset U_i.
 \tag{1.3}
\]

Let \({\cal R}\) be the set of all such records.

### Theorem 1.1 (exact incidence parameters)

The raw catalogue satisfies

\[
 |{\cal R}|=mK=N,                                        \tag{1.4}
\]

\[
 \deg(X)=m,\qquad
 \deg(i)\le m-1,\qquad
 \deg(L)\le m+1,                                        \tag{1.5}
\]

and

\[
 \deg(X,i)\le1,\qquad
 \deg(i,L)\le1,\qquad
 \deg(X,L)\le m.                                        \tag{1.6}
\]

The average degree on the host shore and on the lower-colour shore is
exactly one.

#### Proof

Every \(m\)-set \(X\) has exactly \(m\) one-element extensions in
\([2m]\), and the \(U_i\) enumerate every \((m+1)\)-set once.  Thus every
\(X\in{\cal E}\) has exactly \(m\) records, giving
\(|{\cal R}|=m|{\cal E}|=mK=N\).

A block \(U_i\) has \(m+1\) middle facets.  Its two boundary facets
\(C_i,C_{i+1}\) do not belong to \({\cal E}\), so at most \(m-1\)
omitted facets produce records at \(i\).

Fix \(L\in{\cal L}\).  In a record with \(t_i(X)=L\), put
\(C=C_{i+1}\).  Then \(C\supset L\).  Conversely, choosing such a
successor facet \(C\) fixes its occurrence index \(i+1\), hence fixes
\(U_i\), and the only possible token is

\[
                         X=L\cup(U_i\setminus C).         \tag{1.7}
\]

There are exactly \(m+1\) middle supersets \(C\supset L\), proving the
lower-colour degree bound and \(\deg(i,L)\le1\).
The other codegrees follow directly from (1.3), with
\(\deg(X,L)\le\deg(X)=m\).  Since both resource shores have \(N\)
vertices and receive the \(N\) records, their average degrees are one.
\(\square\)

In particular, the usual high-minimum-degree or growing-quasiregular
hypotheses of a Pippenger--Spencer type nibble are not consequences of the
Boolean degrees and codegrees.  A proof would first need a cycle-specific
viable core; it cannot obtain one from the universal parameters alone.

## 2. The full-\(N\) Aharoni--Haxell obstruction

Let

\[
 q=N-K=(m-1)K
 \tag{2.1}
\]

and introduce \(q\) formal dummy tokens \({\cal D}_0\).  On the resource
set \(I\sqcup{\cal L}\), where \(I=\mathbb Z_N\), associate a graph family
to every token:

\[
 {\cal F}_X=\{\{i,t_i(X)\}:X\subset U_i\}
       \qquad(X\in{\cal E}),                              \tag{2.2}
\]

and

\[
 {\cal F}_d=\{\{i,b_i\}:i\in I\}
       \qquad(d\in{\cal D}_0).                            \tag{2.3}
\]

### Theorem 2.1 (exact full-token rainbow form)

A uniformly outgoing directed repair exists if and only if the \(N\)
families

\[
       ({\cal F}_t:t\in{\cal E}\sqcup{\cal D}_0)
 \tag{2.4}
\]

have a rainbow matching of size \(N\).

#### Proof

A selected \(X\)-edge chooses its host and replacement colour.  A selected
dummy edge chooses one unmatched host and its retained base colour.
Resource disjointness says exactly that every host and every lower colour
is used once.  This is the perfect-matching equivalence of the uniformly
outgoing full signed three-partite hypergraph, with the token shore used as
family indices.
\(\square\)

### Theorem 2.2 (full-\(N\) AH capacity barrier)

The rank-two Aharoni--Haxell sufficient hypothesis cannot hold for (2.4)
for any \(m\ge2\).

#### Proof

For the full set of \(N\) families,

\[
 \nu\!\left(\bigcup_t{\cal F}_t\right)\le N,             \tag{2.5}
\]

because each of the two resource shores has size \(N\).  The rank-two
Aharoni--Haxell theorem would require

\[
 \nu\!\left(\bigcup_t{\cal F}_t\right)>2(N-1).           \tag{2.6}
\]

Here \(N=mK\ge4\), so \(N\le2(N-1)\).  Thus (2.6) is impossible.
\(\square\)

This is stronger than the fixed-\(K\)-bank capacity obstruction: keeping
all \(N\) hosts does not rescue the direct all-token AH formulation.
It does not exclude a staged argument which first solves a linear-sized
deterministic subsystem and then changes the resource families.

## 3. Exact random-bank and dependency obstructions

### 3.1 Uniform \(K\)-bank plus a sublinear absorber

Assume \(m\ge3\) and that the base word has the floor profile

\[
                         0^K1^{N-2K}2^K.                 \tag{3.1}
\]

Let \(P\subset I\) be the \(2K\) block occurrences carrying duplicated
base colours.  These occurrences are partitioned into \(K\) pairs, one
pair for each duplicated colour.

Every uniformly outgoing directed repair uses exactly one host from each
pair.  Indeed the \(K\) absent colours require \(K\) incoming replacement
outputs, exhausting all \(K\) arcs.  Thus no arc can terminate at a
singleton or duplicated base colour.  The multiplicity equation at every
duplicated colour then forces exactly one of its two occurrences to be cut,
while a singleton occurrence cannot be cut.  Hence there are exactly
\(2^K\) source banks which pass this necessary test.

### Theorem 3.1 (uniform-bank distance)

If \(H\) is a uniformly random \(K\)-subset of \(I\), then

\[
 \Pr(H\text{ passes the source-bank test})
   =\frac{2^K}{\binom{mK}{K}}
   \le\left(\frac2m\right)^K.                            \tag{3.2}
\]

Moreover, with probability at least \(1-9/K\), at least \(K/6\) selected
hosts must be replaced before \(H\) can pass that test.

#### Proof

The exact count gives the equality.  Also

\[
 \binom{mK}{K}
  =\prod_{j=0}^{K-1}\frac{mK-j}{K-j}
  \ge m^K,                                               \tag{3.3}
\]

which gives the inequality.

Put \(G=|H\setminus P|\).  This is hypergeometric with

\[
 {\bf E}G=\frac{m-2}{m}K\ge\frac K3                     \tag{3.4}
\]

and

\[
 \operatorname {Var}G
 =K\frac{m-2}{m}\frac2m\frac{N-K}{N-1}
 \le\frac K4.                                            \tag{3.5}
\]

Every passing bank lies inside \(P\), so its replacement distance from
\(H\) is at least \(G\).  Since
\({\bf E}G-K/6\ge K/6\), Chebyshev's inequality gives

\[
 \Pr(G<K/6)\le \frac{K/4}{(K/6)^2}=\frac9K.              \tag{3.6}
\]

\(\square\)

Thus an unbiased full-\(N\) bank followed by \(o(K)\) replacements fails
with probability tending to one.  A successful random construction must
bias the bank toward the duplicate pairs from the start.

### 3.2 Independent Boolean host sampling

There is a second obstruction before palette balance.  Select every block
independently with probability \(p=1/m\), so the expected bank size is
\(N/m=K\).  For \(X\in{\cal E}\), let \(A_X\) be the event that none of
its \(m\) hosts is selected, and put

\[
                         Z=\sum_{X\in{\cal E}}{\bf1}_{A_X}.               \tag{3.7}
\]

### Theorem 3.2 (isolated-token dependency ledger)

For \(m\ge3\),

\[
 \Pr(A_X)=\left(1-\frac1m\right)^m\ge\frac14,            \tag{3.8}
\]

and the event \(A_X\) is dependent on at most

\[
                         \Delta=m(m-2)                   \tag{3.9}
\]

other isolation events.  Furthermore

\[
 {\bf E}Z\ge\frac K4,\qquad
 \operatorname {Var}Z\le K(m-1),                         \tag{3.10}
\]

so

\[
 \Pr(Z<K/8)\le\frac{64(m-1)}K.                           \tag{3.11}
\]

On the complementary event, at least

\[
                         \frac{K}{8(m-1)}                \tag{3.12}
\]

additional blocks are needed merely to give every omitted facet one
selected host.

#### Proof

Equation (3.8) is immediate; the displayed sequence is increasing for
\(m\ge2\) and begins at \(1/4\).

Two distinct \(m\)-sets have at most one common \((m+1)\)-superset.
Each of the \(m\) hosts of \(X\) contains at most \(m-2\) other omitted
facets, proving (3.9).  Events with disjoint host sets are independent.
If two host sets meet in their unique common block, their covariance is

\[
 \left(1-\frac1m\right)^{2m-1}
 -\left(1-\frac1m\right)^{2m}
 =\frac1m\left(1-\frac1m\right)^{2m-1}
 \le\frac1m.                                             \tag{3.13}
\]

There are at most \(K\Delta/2\) dependent unordered pairs.  Therefore

\[
 \operatorname {Var}Z
 \le K+2\frac{K\Delta}{2}\frac1m
 =K(m-1).                                                \tag{3.14}
\]

Chebyshev, applied at half the mean, gives (3.11).  Finally one added
block contains at most \(m-1\) omitted facets, proving (3.12).
\(\square\)

This closes an independent Bernoulli bank followed by
\(o(K/m)\) local additions.  It does not exclude a dependent matching
distribution or an absorber of order \(K/m\).

## 4. Dummy antisymmetry kills ordinary parity

Let \(\mathscr H\) be the exact three-partite hypergraph on

\[
 I\sqcup{\cal L}\sqcup({\cal E}\sqcup{\cal D}_0)
 \tag{4.1}
\]

whose repair edges are
\(\{i,t_i(X),X\}\) and whose dummy edges are \(\{i,b_i,d\}\).
Let \(R\) be the number of uniformly outgoing physical directed repairs.

### Theorem 4.1 (dummy-factorial theorem)

\[
                         \#\operatorname {PM}(\mathscr H)=q!\,R,
 \qquad q=(m-1)K.                                        \tag{4.2}
\]

#### Proof

Fix a uniformly outgoing physical repair.  Its \(K\) repair edges are
fixed.  The other \(q\) hosts have pairwise distinct retained base colours,
and every dummy token can use every such host-colour edge.  Choosing the
dummy part of a perfect matching is therefore exactly a bijection from the
\(q\) dummy labels to the \(q\) unmatched host-colour edges, giving \(q!\)
lifts.
Every perfect matching projects uniquely to its \(K\) repair edges, so
these are all lifts. \(\square\)

### Corollary 4.2 (parity and exterior no-go)

For every \(m\ge2\), \(q\ge2\), and hence

\[
                  \#\operatorname {PM}(\mathscr H)\equiv0\pmod2.         \tag{4.3}
\]

More generally, any matching sum which is alternating in the labelled
dummy shore and whose physical weights do not depend on the dummy labels
vanishes over characteristic zero.

#### Proof

Parity follows from (4.2).  For the alternating statement, transpose two
dummy labels.  This is a fixed-point-free involution within every physical
repair fibre, preserves its physical weight, and reverses its sign.
Equivalently the dummy factor is
\(\sum_{\pi\in S_q}\operatorname {sgn}\pi=0\). \(\square\)

Thus a natural labelled-dummy determinant or exterior hyperdeterminant can
never certify repair.  This does **not** apply to the scalarized matrix

\[
 A_{i,L}
 =s\,{\bf1}_{L=b_i}
  +\sum_{\substack{X\subset U_i\\t_i(X)=L}}x_X.          \tag{4.4}
\]

The coefficient

\[
 [s^q\prod_Xx_X]\det A                                  \tag{4.5}
\]

has already divided out the dummy labels; it is the signed repair count,
and modulo two it is the parity of \(R\).  A bespoke triangularity or
sign-coherence proof of (4.5) remains a valid route.

## 5. A Catalan-scale obstruction to canonical BTK/SCD

Let \(\sigma\) be the standard BTK inclusion matching from
\(\binom{[2m]}{m-1}\) to \(\binom{[2m]}{m+1}\).
Represent sets by binary words read left to right.  Match every \(1\) to
the most recent unmatched \(0\).  For a rank-\((m-1)\) word, the BTK
two-step mate is obtained by changing its first two free zeros to ones.

For an inclusion pair \(L\subset U\), let

\[
 \psi(L,U)
 =\{L+a,L+b\},\qquad U\setminus L=\{a,b\},               \tag{5.1}
\]

be its lifted Johnson edge.

### Theorem 5.1 (general physical-overload cut)

Let \(\tau\) be any inclusion perfect matching between the lower and upper
colour shores, and put

\[
 F_\tau=\{\psi(L,\tau(L)):L\in\binom{[2m]}{m-1}\}.       \tag{5.2}
\]

If a Johnson Hamilton cycle \(P\) contains a common lower/upper edge
transversal inducing a matching \(\mu\), then

\[
 |\{L:\mu(L)\ne\tau(L)\}|
 \ge\frac12\sum_{v\in\binom{[2m]}m}
                   (\deg_{F_\tau}(v)-2)_+.              \tag{5.3}
\]

#### Proof

Every agreement \(\mu(L)=\tau(L)\) forces the physical edge
\(\psi(L,\tau(L))\) into the transversal and hence into \(P\).
At most two such forced edges can be incident with a fixed middle vertex
\(v\).  Therefore at least
\((\deg_{F_\tau}(v)-2)_+\) incidences at \(v\) belong to disagreeing rows.
Summing over \(v\) counts each disagreeing row-edge at most twice, proving
(5.3). \(\square\)

The standard BTK matching admits a much sharper disjoint certificate.

### Theorem 5.2 (BTK constant-fraction edit barrier)

For every \(m\ge3\), if \(P\) and \(\mu\) are as in Theorem 5.1, then

\[
 |\{L:\mu(L)\ne\sigma(L)\}|
 \ge\operatorname {Cat}_{m-3}
 >\frac{\operatorname {Cat}_m}{64}.                     \tag{5.4}
\]

The same statement holds for every coordinate conjugate of \(\sigma\).

#### Proof

Let \(D\) range over the Dyck words of semilength \(m-3\), so there are
\(\operatorname {Cat}_{m-3}\) choices.  Put

\[
                         v_D=D\,101010.                  \tag{5.5}
\]

Delete in turn the three suffix ones, at relative positions \(0,2,4\).
The resulting lower words have suffixes

\[
               001010,\qquad100010,\qquad101000.         \tag{5.6}
\]

The Dyck prefix is internally fully paired, so the BTK scan factors
through the displayed suffix.  The first two free-zero positions are,
respectively,

\[
                       \{0,5\},\qquad\{1,2\},\qquad\{3,4\}.               \tag{5.7}
\]

Consequently the three lifted BTK edges are

\[
 \begin{split}
 v_D&\,--\,D\,001011,\\
 v_D&\,--\,D\,110010,\\
 v_D&\,--\,D\,101100.                                   \tag{5.8}
 \end{split}
\]

If \(\mu\) agreed with \(\sigma\) on all three lower rows in (5.6), the
Hamilton cycle \(P\) would contain all three edges in (5.8), contradicting
\(\deg_P(v_D)=2\).  The three-row families are disjoint as \(D\) varies,
so at least one distinct disagreement is forced for every Dyck prefix.

Finally

\[
 \frac{\operatorname {Cat}_n}{\operatorname {Cat}_{n-1}}
 =\frac{2(2n-1)}{n+1}<4.                                \tag{5.9}
\]

Applying (5.9) three times gives
\(\operatorname {Cat}_m<64\operatorname {Cat}_{m-3}\).
Coordinate conjugation preserves all physical degrees and disagreements.
\(\square\)

Equivalently, if \(y_{D,j}\) indicates agreement with the three BTK rows
in (5.6), every exact full-\(N\) master has the pairwise disjoint valid
cuts

\[
                         y_{D,0}+y_{D,1}+y_{D,2}\le2.     \tag{5.10}
\]

Thus exact BTK, every coordinate conjugate, and every \(o(K)\)-edit are
impossible before host injection, cap-two placement, or endpoint-threshold
orientation is considered.  This is distinct from the one-port GMM
recursion obstruction: it applies to the static canonical SCD matching
itself.

## 6. Degree/codegree data alone still do not imply repair

For even \(r\), consider the cyclic Latin three-partite hypergraph with
parts \(A=B=C=\mathbb Z_r\) and edges

\[
                         (a,b,a+b),\qquad a,b\in\mathbb Z_r.             \tag{6.1}
\]

It is \(r\)-regular, every typed pair codegree is one, and every pair
projection is complete.

### Proposition 6.1 (sharp abstract parity obstruction)

The hypergraph (6.1) has no perfect matching for even \(r\), whereas it
has one for odd \(r\).

#### Proof

A perfect matching would choose a permutation \(b=\pi(a)\) such that
\(a+\pi(a)\) is also a permutation.  Put

\[
                         S=\sum_{a\in\mathbb Z_r}a.
 \tag{6.2}
\]

Summing the third coordinates gives \(S=2S\pmod r\).  For even \(r\),
\(S=r/2\pmod r\), a contradiction.  For odd \(r\), take
\(\pi(a)=a\); multiplication by two is then a permutation. \(\square\)

This proves that no sufficient theorem whose only hypotheses are regular
degrees, unit codegrees, and complete pairwise projections can imply a
three-partite transversal.  In particular, an LLL, nibble, absorption, or
parity argument using only those data cannot suffice.  It is
parameter-relevant for infinitely many Catalan sizes, since
\(\operatorname {Cat}_m\) is even whenever \(m\) is even.

It is not a Boolean repair counterexample.  Literal containment forbids
its smallest rectangle.

### Lemma 6.2 (Boolean anti-rectangle and first holonomy)

In the token--hole projection of a literal floor repair core, there is no
\(C_4\).  If three distinct token vertices form a \(C_6\) with three
distinct hole intersections, then those tokens are three facets of one
common \((m+1)\)-set.

#### Proof

Every viable hole \(Z\) has \(Z\subset X\), with ranks \(m-1,m\).
If distinct tokens \(X,X'\) shared two distinct holes \(Z_0,Z_1\), then

\[
                         X=Z_0\cup Z_1=X',
 \tag{6.3}
\]

a contradiction.  This proves \(C_4\)-freeness.

Three pairwise-adjacent \(m\)-sets form a Johnson triangle.  Such a triangle
is either a star, in which all three share one \((m-1)\)-set, or a top, in
which all three are facets of one \((m+1)\)-set.  Distinct edge
intersections exclude the star, leaving the common top. \(\square\)

The anti-rectangle is the first positive structure discarded by the Latin
and generic AH models.  Any viable all-\(m\) proof must exploit this
literal geometry, together with cycle-specific viability or a
unitriangular physical core.

## 7. Exact surviving boundary

The following routes are now formally closed.

1. Direct Aharoni--Haxell on the exact full-\(N\) token families.
2. An unbiased random \(K\)-bank followed by \(o(K)\) replacements in the
   floor regime.
3. Independent Bernoulli host sampling followed by \(o(K/m)\) additions.
4. Ordinary parity or an exterior determinant on the labelled-dummy
   three-shore hypergraph.
5. Exact BTK/GK, a coordinate conjugate, or any \(o(K)\)-edit of that
   canonical inclusion matching.
6. Any theorem whose only hypotheses are regular degrees, bounded
   codegrees, and pairwise Hall expansion.

The results do not exclude:

1. a cycle-specific, highly correlated distribution already supported on
   the duplicate-source bank;
2. a \(\Theta(K)\)-scale rethread using the Boolean \(C_4\)-free/common-top
   geometry;
3. a non-BTK SCD matching whose Boolean lift is already a spanning
   \(K\)-path forest; or
4. a proof that the scalarized coefficient (4.5) is nonzero by genuine
   triangularity or sign coherence.

Accordingly, no all-large-\(m\) directed-repair theorem is proved.  The
sharp replacement target is a correlated physical construction, not
another black-box application of expansion, LLL, or determinant parity.
