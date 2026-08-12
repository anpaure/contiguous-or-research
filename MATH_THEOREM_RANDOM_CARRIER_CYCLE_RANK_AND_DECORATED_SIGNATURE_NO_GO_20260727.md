# Random carrier graphs have extensive cycle rank, but random word tables have no repaired signatures

Date: 2026-07-27

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad \kappa=4H-1,
 \qquad s=n-M+2,
\]

where \(H=o(m)\), \(H\to\infty\), and \(\kappa<M/2\).  Give every
rank-\(M\) top an independent uniformly random cyclic word.  For an
\((M-2)\)-core \(C\), let \(G_C\) be the carrier graph from
`MATH_THEOREM_GROUPED_OWNER_PATH_LINEAR_GAP_ODD_CYCLE_AND_REROOT_CYCLE_RANK_20260727.md`.

There are two sharply opposite conclusions.

1.  For each fixed \(C\),

    \[
       G_C\ \stackrel{d}=\ G\left(s,{2\over M-1}\right).
    \]

    In particular

    \[
       \mathbb E\sum_C\beta(G_C)=\Omega(mN),
       \qquad N=\binom nM.
    \]

    Hence the edge census lying below the forest extremum is not a
    probabilistic obstruction.  Random carrier graphs have extensive
    cycle excess, with a factor \(m\) to spare over the \(\Omega(N)\)
    necessary scale.

2.  With probability \(1-o(1)\), the same random word table contains
    **no** reroot-only repaired twelve-top packet whose two six-row
    tables have equal rooted column multisets.  The obstruction is the
    filler-column signature, not the carrier graph.  Equality of two
    six-row signatures has probability at most

    \[
       { (6!)^M\over (M!)^6}
       =\exp[-(6+o(1))m\log m],
    \]

    whereas the entire structural carrier catalogue has only
    \(\exp[O(m)]\) choices.

Thus a pseudorandom ordinary-frame near-factor does **not** by itself
imply extensive decorated carrier rank.  At the full-word level it
predicts the opposite: uncoloured cycles are abundant and compatible
signature collisions are absent.  The sharp remaining deterministic
condition is deliberate compression of the six-row column signatures
(equivalently, a row-mixed covariance factor), not ordinary graph
expansion or cycle rank.

The polynomial broad-support bank is not affected by this no-go.  The
bank of
`MATH_THEOREM_BROAD_POSITION_THREE_PACKET_SEEDING_AND_OWNER_QUARANTINE_20260727.md`
constructs only \(O(n)\) packets directly and overwrites conflicting
rows at \(O(m^3)=o(W)\) owner cost.  Random carrier graphs are neither
needed nor sufficient for that initialization.  What remains open is a
positive-density recurrent packet circulation.

## 1. Exact Bernoulli law for one core

Fix \(C\in\binom{[n]}{M-2}\).  Its carrier graph has vertex set
\([n]\setminus C\), of size \(s\).  A possible edge \(xy\) is decided
solely by the cyclic word on the top

\[
                         U=C\cup\{x,y\}.
\]

Different possible edges correspond to different tops.  Their events
are therefore independent.  In a uniform cyclic word on \(U\), after
fixing the position of \(x\), exactly two of the remaining \(M-1\)
positions put \(y\) at cyclic distance \(\kappa\).  Consequently

\[
             \Pr[xy\in E(G_C)]={2\over M-1},
\]

which proves the asserted Erdos--Renyi law.

This also identifies the misleading threshold.  The mean edge count is
slightly below \(s-1\), the largest size of a forest, but the mean
degree is asymptotic to two, not one.  A random graph at mean degree two
has linear cycle excess.

## 2. An elementary extensive lower bound

Write \(I(G)\) for the number of isolated vertices.  For every graph on
\(s\) vertices,

\[
       \beta(G)=|E(G)|-s+c(G)\ge |E(G)|-s+I(G).
       \tag{2.1}
\]

For \(p=2/(M-1)\), the exact expectations are

\[
 \mathbb E|E(G_C)|={s(s-1)\over M-1},\qquad
 \mathbb EI(G_C)=s(1-p)^{s-1}.
\]

Therefore

\[
 \begin{aligned}
 \mathbb E\beta(G_C)
 &\ge {s(s-1)\over M-1}-s
        +s\left(1-{2\over M-1}\right)^{s-1}\\
 &= -O(H)+(e^{-2}+o(1))s
  = (e^{-2}+o(1))m.
 \end{aligned}
 \tag{2.2}
\]

No independence between different cores is required.  Summing (2.2)
and using

\[
 {\binom n{M-2}\over\binom nM}
 ={M(M-1)\over s(s-1)}=1+o(1)
\]

gives

\[
       \mathbb E\sum_C\beta(G_C)
       \ge(e^{-2}+o(1))mN.
       \tag{2.3}
\]

In particular there exists an unconditioned word table satisfying this
bound.  Equation (2.3) is not asserted after conditioning on a
coefficient-one owner resolution; proving such a conditioning theorem
would itself require trajectory information absent from the current
ordinary-frame result.

## 3. Column signatures are overwhelmingly noncolliding

A repaired twelve-top source on a fixed core consists of two
edge-disjoint six-cycles, denoted \(P\) and \(Q\).  After choosing roots,
write their six-row column multisets as

\[
 P_j=\{p_i(j):0\le i<6\}_{\rm multi},\qquad
 Q_j=\{q_i(j):0\le i<6\}_{\rm multi}.
\]

The histogram-neutral packet requires

\[
                         P_j=Q_j\quad(1\le j\le M).
                         \tag{3.1}
\]

Fix the twelve distinct tops, a split into the two cycles, and all root
choices.  Condition on the six \(P\)-words.  At every column, (3.1)
allows at most \(6!\) assignments of the six displayed labels to the
six \(Q\)-rows.  Hence at most \((6!)^M\) six-row arrays can satisfy
(3.1).  The six independent uniform \(Q\)-words have \((M!)^6\)
possible arrays.  Thus

\[
             \Pr[(3.1)]\le{(6!)^M\over(M!)^6}.
             \tag{3.2}
\]

This is an upper bound: it deliberately ignores the requirement that a
column assignment use only labels belonging to its row top and that
each row be a permutation, so it remains valid.

The number of possible structural supports is at most

\[
 \binom n{M-2}\binom s6\,15\,(6!)^2,
\]

and allowing arbitrary rerootings of all twelve rows contributes at
most \(M^{12}\).  Reversal may also be allowed at only another constant
factor per row.  The logarithm of this entire prefactor is \(O(m)\),
whereas Stirling's formula gives

\[
 \log{(6!)^M\over(M!)^6}=-(6+o(1))m\log m.
\]

The union bound proves that an independent random word table contains
no support satisfying (3.1) with probability \(1-o(1)\).  This remains
true before imposing carrier distance, endpoint palettes,
squarefreeness, or owner disjointness, and is therefore a fortiori a
no-go for random repaired packets.

## 4. The exact construction target

For every compatible carrier cycle \(Z\), define its rooted column
signature

\[
             \Sigma(Z)=(Z_1,\ldots,Z_M),
\]

where \(Z_j\) is the multiset of labels appearing in column \(j\) of
its row table.  A repaired bidirectional packet is an edge-disjoint
pair \(P,Q\) with

\[
                         \Sigma(P)=\Sigma(Q),
                         \tag{4.1}
\]

together with the already-audited endpoint-palette and squarefreeness
conditions.

The uncoloured cycle rank \(\sum_C\beta(G_C)\) forgets \(\Sigma\).
Theorem 3 shows that random words make \(\Sigma\) essentially injective
on the available carrier cycles.  Therefore the positive theorem must
do one of the following.

1. Construct a coefficient-one table in which \(\Sigma\) has extensive
   fibres and those fibres contain top-disjoint pairs satisfying (4.1);
2. construct the row-mixed cyclic covariance identity directly; or
3. replace exact histogram cancellation by a new packet whose admissible
   signature space has only \(\exp[O(m)]\), rather than
   \(\exp[\Theta(m\log m)]\), states.

This is strictly sharper than asking for pseudorandom carrier graphs.
The needed table is deliberately anti-random in its column signatures
while remaining sufficiently dispersed in its middle-owner support.

## 5. Audited boundary

Proved:

1. the exact Bernoulli carrier-graph law for independent random words;
2. the unconditional extensive expectation (2.3);
3. an overwhelming-probability absence theorem for the exact
   histogram-neutral repaired signature; and
4. the separation between the already-solved polynomial seed bank and
   the open positive-density circulation.

Not proved:

1. existence of a coefficient-one near-factor whose uncoloured carrier
   graphs obey (2.3);
2. any extensive equal-signature fibre in a coefficient-one table;
3. a row-mixed covariance factor; or
4. a positive-density recurrent repaired-packet chronology.

