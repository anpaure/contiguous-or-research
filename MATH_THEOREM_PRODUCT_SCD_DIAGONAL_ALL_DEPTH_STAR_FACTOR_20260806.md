# Product-SCD diagonals give an explicit all-depth star factor above theta

**Date:** 2026-08-06  
**Method:** two symmetric-chain decompositions, constant-rank diagonals,
and an explicit Gaussian tail window  
**Status:** unconditional standalone literal target-packing theorem, with a
theta-beating count and a static containing-owner lift.  The subsequent
audit
`MATH_AUDIT_PRODUCT_SCD_DIAGONAL_FIXED_ADDITIVE_OWNER_WINDOW_NOGO_20260807.md`
proves that runs with more than `C+1` consecutive fully marked endpoints
cannot occur in any word of length `B(k)+C` for fixed `C`: their forced
central-length windows have rank below the middle rank.  Thus this theorem
does **not** provide fixed-additive warm-up amortization or a PBBS lift.

## 1. Product-SCD diagonal paths

Partition the ground set into two shores

\[
                         [n]=X\mathbin{\dot\cup}Y,
 \qquad |X|=N_1,\quad |Y|=N_2,\quad N_1+N_2=n.             \tag{1.1}
\]

Fix one symmetric-chain decomposition of \(B(X)\) and one of \(B(Y)\).
Write their chains as

\[
 C=(C_a,C_{a+1},\ldots,C_{N_1-a}),
 \qquad
 K=(K_b,K_{b+1},\ldots,K_{N_2-b}),                        \tag{1.2}
\]

where subscripts denote ranks.

Fix a bottom rank \(s<n/2\).  For every pair \((C,K)\), define

\[
 I(C,K)={i: a\le i\le N_1-a,
                 \ b\le s-i\le N_2-b\}.                  \tag{1.3}
\]

When this interval is nonempty, order it increasingly and put

\[
                         B_i=C_i\cup K_{s-i}
                         \qquad(i\in I(C,K)).               \tag{1.4}
\]

### Theorem 1.1 (diagonal Johnson path factor)

The nonempty words (1.4), over all pairs of SCD chains, partition the
complete rank-\(s\) layer.  Every word is a simple Johnson path.

#### Proof

Every rank-\(s\) set \(B\) has a unique decomposition

\[
                         B=(B\cap X)\cup(B\cap Y),          \tag{1.5}
\]

and each shore part lies on a unique SCD chain.  Its \(X\)-rank determines
the unique index \(i\), proving the partition.

When \(i\) increases by one, \(C_i\) gains one coordinate and
\(K_{s-i}\) loses one coordinate.  Thus consecutive sets in (1.4) differ
by one Johnson exchange.  No set repeats because its \(X\)-rank strictly
increases. \(\square\)

## 2. Every internal suffix chain is full and globally unique

For an endpoint \(i\in I(C,K)\) with at least \(j-1\) predecessors in the
same path, the union of its last \(j\) bottom sets is

\[
 \begin{aligned}
 Z_{i,j}
 &=\bigcup_{h=0}^{j-1}
       \left(C_{i-h}\cup K_{s-i+h}\right)\\
 &=C_i\cup K_{s-i+j-1}.                                   \tag{2.1}
 \end{aligned}
\]

The second equality uses that the \(C\)-sets increase with their index and
the \(K\)-sets do likewise.

### Theorem 2.1 (global all-depth disjointness)

For every \(d\), all targets

\[
                         Z_{i,j},qquad1\le j\le d,          \tag{2.2}
\]

whose complete history lies inside its diagonal path are pairwise distinct
over every endpoint, depth, and path.  Moreover

\[
                         |Z_{i,j}|=s+j-1.                   \tag{2.3}
\]

Thus, after discarding the first \(d-1\) vertices of each path, every
remaining vertex is a full rank-\(s\) endpoint and all its marked targets
are globally disjoint.

#### Proof

Equation (2.1) gives

\[
                         |Z_{i,j}|=i+(s-i+j-1)=s+j-1.       \tag{2.4}
\]

Suppose two displayed targets agree.  Their ranks first give the same
depth \(j\).  Intersecting with \(X\) gives

\[
                         C_i=C'_{i'},                       \tag{2.5}
\]

which, by the SCD partition, forces \(C=C'\) and \(i=i'\).  Intersecting
with \(Y\) then gives the same vertex of the same unique chain \(K\), so
\(K=K'\).  Hence the occurrences were identical. \(\square\)

This is stronger than pairwise packet matching: all depths are serialized
by one named path factor, with no random-order or growing-uniformity step.

### Corollary 2.2 (distinct rank-\(t\) boundary tickets)

At every endpoint with \(d\) predecessors in its path, equation (2.1)
also applies at depth \(d+1\):

\[
 Z_{i,d+1}=C_i\cup K_{s-i+d},
 \qquad |Z_{i,d+1}|=s+d.                                  \tag{2.6}
\]

These depth-\((d+1)\) values are pairwise distinct by the same proof.  In
the top PBBS slab \(s=m-2d\), they have rank

\[
                         s+d=m-d=t.                         \tag{2.7}
\]

Thus every selected run may be shortened by one endpoint, if necessary,
to carry a distinct literal rank-\(t\) boundary ticket in addition to its
complete strict-lower piece.  This is a target/envelope ticket statement;
it does not by itself identify that ticket with a prescribed PBBS owner.

### Corollary 2.3 (static containing-owner injection)

Every selected family \(\mathcal T\) of distinct rank-\(t\) boundary
tickets admits an injection

\[
                         \phi:\mathcal T\longrightarrow{[n]\choose m},
 \qquad T\subseteq\phi(T).                                \tag{2.8}
\]

#### Proof

In the rank-\(t\) to rank-\(m\) inclusion graph, every left vertex has
degree \(\binom{n-t}{m-t}\), while every right vertex has degree
\(\binom mt\).  For every \(\mathcal F\subseteq\mathcal T\), double
counting its outgoing incidences gives

\[
 |N(\mathcal F)|
 \ge {\binom{n-t}{m-t}\over\binom mt}|\mathcal F|
 ={\binom nm\over\binom nt}|\mathcal F|
 \ge|\mathcal F|,                                         \tag{2.9}
\]

because \(t<m\le n/2\). Hall's theorem proves the injection. \(\square\)

Thus static owner-envelope capacity can be added without losing a selected
ticket.  The corollary does not make the owners consecutive Johnson
neighbours or put them in one owner-exact Euler chronology.

## 3. A counted bank of long diagonals

Now use the odd top-slab parameters

\[
 n=2m+1,qquad s=m-2d,qquad
 {d^2\over n}\longrightarrow{\pi\over8},                  \tag{3.1}
\]

and take the balanced shore sizes

\[
                         N_1=m,qquad N_2=m+1.              \tag{3.2}
\]

Put

\[
                         \Delta={n\over2}-s=2d+{1\over2}.  \tag{3.3}
\]

For a symmetric chain in \(B_{N_i}\) beginning at rank \(a\), define its
radius

\[
                         \rho={N_i\over2}-a.                \tag{3.4}
\]

The index interval (1.3) is the intersection of two real intervals with
centres \(N_1/2\) and \(N_1/2-\Delta\), and radii \(\rho_C,\rho_K\).

Take

\[
                         c={4\over5}.                       \tag{3.5}
\]

If

\[
                         \rho_C,\rho_K\ge c\Delta,          \tag{3.6}
\]

then the overlap length is at least

\[
                         (2c-1)\Delta={3\over5}\Delta.     \tag{3.7}
\]

After integer rounding, the corresponding diagonal path has at least

\[
                         {6\over5}d-O(1)                    \tag{3.8}
\]

vertices, and therefore at least

\[
                         {1\over5}d-O(1)                    \tag{3.9}
\]

full endpoints after its first \(d-1\) vertices are discarded.

## 4. Exact asymptotic abundance

An SCD of \(B_N\) has

\[
                         {N\choose a}-{N\choose a-1}       \tag{4.1}
\]

chains beginning at rank \(a\).  Hence the number whose radius is at least
\(c\Delta\) telescopes exactly to

\[
                         {N\choose\lfloor N/2-c\Delta\rfloor}.          \tag{4.2}
\]

The uniform local central-binomial estimate gives, for each shore,

\[
 { {N_i\choose\lfloor N_i/2-c\Delta\rfloor}
   \over
   {N_i\choose\lfloor N_i/2\rfloor}}
 \longrightarrow e^{-2c^2\pi}.                            \tag{4.3}
\]

Indeed \(\Delta^2/N_i\to\pi\).  Also, with

\[
                         W={2m+1\choose m},                 \tag{4.4}
\]

Stirling's formula gives

\[
 {d
   {m\choose\lfloor m/2\rfloor}
   {m+1\choose\lfloor(m+1)/2\rfloor}
  \over W}
 \longrightarrow1.                                       \tag{4.5}
\]

Combining (3.9), (4.2)--(4.5) yields the following.

### Theorem 4.1 (explicit positive-density full bank)

The product-SCD diagonal factor contains at least

\[
 \boxed{
 \left({1\over5}e^{-64\pi/25}-o(1)\right)W}               \tag{4.6}
\]

full endpoints whose complete depth-\(d\) target chains are pairwise
disjoint.

These endpoints occur in literal runs in the **standalone rank-\(s\)
target factor**.  If one endpoint per run is discarded, the remaining
standalone endpoint count differs from (4.6) by only

\[
 O\!\left(
 {m\choose\lfloor m/2\rfloor}
 {m+1\choose\lfloor(m+1)/2\rfloor}
 \right)=O(W/d)=o(W).                                      \tag{4.7}
\]

Thus the same coefficient (4.6) survives this purely combinatorial
per-run deletion.  It is not available as a shared serialization bank in
a word of length \(B(k)+C\): Theorem 6.1 below rules out the required long
fully marked runs for every fixed \(C\).

## 4A. A canonical protected central-owner lift

The full endpoints counted above may be chosen so that their owner
envelopes are not merely supplied by abstract Hall matching.

Use the centred \(X\)-rank coordinate

\[
                         x=i-{N_1\over2}.                   \tag{4.8}
\]

For a long chain pair satisfying (3.6), retain the integer indices in the
guaranteed interval

\[
 -c\Delta+d\le x\le -\Delta+c\Delta.                     \tag{4.9}
\]

Its length is

\[
 (2c-1)\Delta-d={1\over5}d+O(1),                          \tag{4.10}
\]

exactly the endpoint bank used in (4.6).  The left deletion supplies the
required depth-\(d\) source history.

For such an endpoint, its rank-\(t\) boundary ticket from Corollary 2.2 is

\[
                         P_i=C_i\cup K_{t-i}.               \tag{4.11}
\]

Define

\[
                         \Omega_i=C_{i+d}\cup K_{t-i}.      \tag{4.12}
\]

### Theorem 4A.1 (shifted-diagonal owner path)

Every set in (4.12) exists, has rank \(m\), and contains \(P_i\).  Along
each selected run, the \(\Omega_i\)'s form a simple Johnson path.  Over all
selected runs:

1. all owners \(\Omega_i\) are distinct;
2. all immediate lower colours \(\Omega_i\cap\Omega_{i+1}\) are distinct;
3. all immediate upper colours \(\Omega_i\cup\Omega_{i+1}\) are distinct;
4. more generally, all unions of \(h\) consecutive owners are distinct at
   every fixed width \(h\) for which they lie inside a run.

#### Proof

In centred coordinates, the rank-\(s\) diagonal is the intersection of
intervals centred at \(0\) and \(-\Delta\).  The rank-\(m\) diagonal is
the intersection of intervals centred at \(0\) and \(-1/2\).  For
\(x\) in (4.9), direct endpoint comparison gives

\[
 x+d\in[-\rho_C,\rho_C]
 \cap[-1/2-\rho_K,-1/2+\rho_K],                           \tag{4.13}
\]

using \(\rho_C,\rho_K\ge c\Delta\), \(c=4/5\), and
\(\Delta=2d+1/2\).  Thus both vertices in (4.12) exist.

Its rank is

\[
                         (i+d)+(t-i)=t+d=m,                 \tag{4.14}
\]

and (4.11) is a subset because \(C_i\subset C_{i+d}\).

Consecutive owners satisfy

\[
 \Omega_{i+1}
  =C_{i+d+1}\cup K_{t-i-1},                               \tag{4.15}
\]

so one \(X\)-coordinate is inserted and one \(Y\)-coordinate deleted.
This is a Johnson edge.  Simplicity and global owner uniqueness follow by
intersecting an owner with \(X\) and \(Y\): the two SCD vertices recover
the unique chain pair and index.

The immediate colours are explicitly

\[
 \Omega_i\cap\Omega_{i+1}
   =C_{i+d}\cup K_{t-i-1},                                \tag{4.16}
\]

and

\[
 \Omega_i\cup\Omega_{i+1}
   =C_{i+d+1}\cup K_{t-i}.                                \tag{4.17}
\]

The same shore-intersection argument proves their global uniqueness.
Finally,

\[
 \bigcup_{a=0}^{h-1}\Omega_{i+a}
   =C_{i+d+h-1}\cup K_{t-i},                              \tag{4.18}
\]

which proves the all-width assertion. \(\square\)

Thus the counted theta bank has a literal lower source trace, distinct
rank-\(t\) boundary tickets, and a **static** containing doubly-rainbow
central Johnson path in the same order.  This does not say that the owner
path is the depth derivative of the source trace.  The fixed-additive audit
cited above proves that it cannot be that derivative on a long fully marked
run.

## 5. Its standalone coefficient strictly beats theta

The theta coefficient is

\[
                         \eta=4\sum_{r\ge1}e^{-4\pi r^2}.  \tag{5.1}
\]

Since \(r^2\ge1+3(r-1)\),

\[
 \eta\le {4e^{-4\pi}\over1-e^{-12\pi}}<8e^{-4\pi}.       \tag{5.2}
\]

On the other hand,

\[
 {1\over5}e^{-64\pi/25}
  >8e^{-4\pi},                                             \tag{5.3}
\]

because (5.3) is equivalent to

\[
                         e^{36\pi/25}>40,                  \tag{5.4}
\]

and \(36\pi/25>4\) while \(e^4>40\).  Therefore

\[
 \boxed{
 {1\over5}e^{-64\pi/25}>\eta.}                            \tag{5.5}
\]

Numerically, the standalone diagonal target bank is larger than the
complete theta reset deficit.  This comparison is a useful supply
calculation only.  It does not imply that these targets can be realized as
shared joins in a fixed-additive PBBS word.

## 6. Literal concatenation and boundary scope

Concatenate the diagonal words in any order.  Only endpoints whose last
\(d\) source positions lie wholly in their own diagonal path are marked.
Their target values remain exactly (2.1); cross-path windows create only
unmarked extra occurrences and cannot destroy a marked witness.

The total number of source positions used by the complete diagonal factor
is exactly

\[
                         {n\choose s}=(e^{-\pi}+o(1))W,      \tag{6.1}
\]

well below the merged-region endpoint supply.  The selected long-path
subbank may of course be used on its own.

What is proved here is an exact standalone integral all-depth target factor.
It is **not** a fixed-additive realization of the former two-endpoint reset
gate.  The fixed-additive audit shows that the long marked runs cannot lie
in the prescribed middle row at all; merely finding an owner path which
contains their boundary tickets does not change that conclusion.

### Theorem 6.1 (fixed-additive long-run obstruction)

Fix \(C\).  For all sufficiently large dimensions, no word of length
\(B(k)+C\) can realize more than \(C+1\) consecutive fully marked
product-SCD diagonal endpoints at every depth \(1,\ldots,d\).

Indeed, for a marked endpoint interval \(J=[L,U]\), intersecting all of
its declared suffix unions forces every source letter in
\(G=[L-d+1,U]\) into the diagonal envelope.  Consequently, every
length-\(h\) interval inside \(G\) which meets \(J\) has union rank at
most

\[
                         s+h-1.                           \tag{6.2}
\]

At physical length \(B(k)+C\), take \(h=d+C+1\).  If
\(|J|\ge C+2\), then \(G\) contains such an interval, but its rank is at
most

\[
 s+h-1=(m-2d)+(d+C+1)-1=m-d+C<m                         \tag{6.3}
\]

for \(d>C\).  The architecture-free endpoint-interval lemma says that
every interval of this length contains a selected middle witness and must
therefore have rank at least \(m\), a contradiction.  The full envelope
proof is recorded in
`MATH_AUDIT_PRODUCT_SCD_DIAGONAL_FIXED_ADDITIVE_OWNER_WINDOW_NOGO_20260807.md`.

## 7. Scope

Proved here:

* a literal path factor of the complete rank-\(s\) layer;
* exact simultaneous target disjointness at every depth \(1,\ldots,d\);
* distinct rank-\(t\) depth-\((d+1)\) boundary tickets after one further
  boundary deletion;
* an injective static assignment of those tickets to containing central
  owners;
* a canonical in-order containing owner lift whose local owner paths are
  simple, doubly rainbow, and all-width target-disjoint;
* explicit long runs in the standalone lower-target factor;
* a rigorous shared-join coefficient
  \(\frac15e^{-64\pi/25}\), strictly larger than theta.

Not proved here, and for the unchanged long fully marked runs refuted by the
fixed-additive audit:

* containment in the varying maximal PBBS owner envelopes or any
  `B(k)+C` middle row with fixed `C`;
* owner/q1 exactness at the joins to the rest of the merged construction;
* connected owner-compatible Euler fusion;
* transport of the global strict-lower compiler through those joins; or
* \(\nu(k)\le B(k)+O(1)\).

The all-depth target-packing identities are closed.  Fixed-additive warm-up
accounting is not: a useful descendant must sparsify the marked endpoints,
insert a genuine rank-restoring reset, or change the history interface.
