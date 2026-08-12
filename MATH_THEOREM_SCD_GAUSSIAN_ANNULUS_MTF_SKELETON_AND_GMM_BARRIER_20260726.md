# SCD Gaussian-annulus endpoint skeletons and persistent GMM prefix barriers

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad W=\binom{2m+1}{m},
 \qquad H=\lceil A\sqrt m\rceil,
 \qquad h=o(\sqrt m),
\tag{0.1}
\]

where \(A>0\) is fixed.  The preceding long-endpoint theorem shows that
any \(W+o(W)\) Gaussian-annulus word must have simultaneous
positive-density Gaussian-length lower left flags and upper right flags.
This note tests the most direct SCD/Hamilton construction of those flags.

There are three exact conclusions.

1. **Positive reduction.**  An SCD equipped with a move-to-front schedule
   of total length \(W+o(W)\) that exposes the annular part of every chain
   gives one literal \(W+o(W)\) word covering both signs of the annulus.
   Lower and upper flags are simultaneous because they are members of the
   same symmetric chains.  Thus a low-transition annular SCD schedule is
   a sufficient endpoint skeleton.

2. **The known SCD-extended Hamilton order still fails after annular
   truncation.**  In the Gregor--Mička--Mütze recursive order, every
   sufficiently long parent chain creates a directed prefix-contaminant
   boundary--first-star in one orientation and reverse-last-star in the
   other--at which one move-to-front update can expose at most one set of
   the next chain's annular truncation.  In dimension \(2m+1\), the number
   of such forced two-update boundaries is at least

   \[
    \boxed{
    B_{m,H}=\binom{2m-1}{m-H-2}.}
   \tag{0.2}
   \]

   Moreover,

   \[
    \boxed{
    {B_{m,H}\over W}
    =\left({1\over4}+o_A(1)\right)e^{-A^2}.}
   \tag{0.3}
   \]

   Hence every checkpoint-faithful move-to-front realization of this
   order has length at least

   \[
    \boxed{
    \left(1+{e^{-A^2}\over4}-o_A(1)\right)W.}
   \tag{0.4}
   \]

   The positive-density obstruction is not caused by requiring the whole
   SCD chain: it remains when only the Gaussian annulus and a central
   owner are required.

3. **Exact reflection symmetry is unavailable.**  No Boolean SCD in
   dimension at least two is permuted chainwise by complementation.
   Separately, complementation cannot act as a reflection of a Middle
   Levels Hamilton cycle; it can only act as a half-turn, and in dimension
   \(2m+1\) that requires \(m=2^t-1\).  Thus neither one complement-stable
   SCD nor a generic reflection-symmetric Middle Levels chronology supplies
   the missing two-sided skeleton.

The note does not rule out a noncanonical SCD/order with only \(o(W)\)
annular prefix barriers, nor a chronology interleaving two different
complementary SCDs.  Those are the exact surviving constructive variants.

## 1. Move-to-front states and literal words

Let

\[
 \Pi=(B_1,\ldots,B_s)
\tag{1.1}
\]

be an ordered partition of the ground set.  Appending a nonempty mask
\(X\) updates it by

\[
 \operatorname {MTF}_X(\Pi)
 =(X,B_1\setminus X,\ldots,B_s\setminus X),
\tag{1.2}
\]

with empty blocks deleted.  If a word prefix has last-occurrence
partition \(\Pi\), then the ORs of its suffixes are exactly the nonempty
prefix unions

\[
 B_1,\quad B_1\cup B_2,\quad\ldots,\quad
 B_1\cup\cdots\cup B_s.
\tag{1.3}
\]

Write a saturated chain as

\[
 C=(L;z_1,\ldots,z_d),
\tag{1.4}
\]

meaning the sets

\[
 L\subset L+z_1\subset\cdots\subset L+z_1+\cdots+z_d.
\tag{1.5}
\]

A state exposes a subchain when the corresponding sets occur among the
prefix unions (1.3).

### Definition 1.1 (annular MTF schedule)

Fix an SCD \(\mathscr C\) of \(2^{[2m+1]}\).  An annular MTF schedule is
an ordering \(C_1,\ldots,C_W\) of its chains, masks
\(X_1,\ldots,X_T\), and checkpoint times

\[
 0<t_1<\cdots<t_W\le T,
\tag{1.6}
\]

such that the state after mask \(t_i\) exposes the two central members and
every member of \(C_i\) whose rank belongs to

\[
 [m-H,m-h-1]\cup[m,m+1]
 \cup[m+h+2,m+1+H].
\tag{1.7}
\]

Empty portions of a short chain impose no condition.

### Theorem 1.2 (SCD schedule compiler)

If an annular MTF schedule has

\[
 T=W+o(W),
\tag{1.8}
\]

then its mask word, preceded by at most \(n\) initialization masks,
is a literal word of length \(W+o(W)\) covering every lower and upper
Gaussian-annulus target and both central ranks.

#### Proof

Every Boolean set belongs to exactly one SCD chain.  A chain containing a
rank at most \(m\) passes through rank \(m\), and a chain containing a
rank at least \(m+1\) passes through rank \(m+1\).  Thus the checkpoint
conditions collectively cover every target in (1.7).

At checkpoint \(t_i\), equation (1.3) represents every exposed set by a
suffix of the actual mask word ending at \(t_i\).  An arbitrary desired
initial ordered partition can be installed with at most \(n\) singleton
masks.  Since \(n=o(W)\), (1.8) gives the stated length. \(\square\)

This is a genuine simultaneous-endpoint reduction.  It does not append a
second annulus word: all chain flags are suffixes of one common sequence
of masks.  The long-endpoint theorem then forces the same word to contain
the corresponding left-endpoint flags under a different target-to-owner
matching; no additional construction is needed for that necessary
conclusion.

## 2. A truncated first-star transition is still impossible in one update

The following lemma strengthens the full-chain first-star obstruction.

Let \(A\) have ordered stars

\[
 z_1,z_2,z_3,\ldots,z_d.
\tag{2.1}
\]

Its first-star child is

\[
 f(A)=(L+z_2;z_3,z_4,\ldots,z_d),
\tag{2.2}
\]

with \(z_1\) fixed outside every member of \(f(A)\).

### Lemma 2.1 (truncated directed first-star barrier)

Suppose a state \(\Pi\) exposes a nonempty saturated subchain of \(A\)
whose members all contain \(z_1\), and whose later varying coordinates
occur among \(z_3,\ldots,z_d\) in that order.  For every mask \(X\), the
updated state \(\operatorname {MTF}_X(\Pi)\) exposes at most one member
of any strictly nested subchain of \(f(A)\) with at least two members.

#### Proof

In \(\Pi\), the coordinate \(z_1\) lies in the prefix forming the least
displayed member of the \(A\)-subchain.  Every coordinate which varies
later in that displayed subchain lies in a singleton block after that
prefix.

Every member of \(f(A)\) excludes \(z_1\).  Therefore, if an updated
prefix represents such a member, then \(z_1\notin X\); otherwise the
first new block already contaminates it.  The residual old block
containing \(z_1\) remains before every later old singleton block not
selected by \(X\).  Hence a new prefix which excludes \(z_1\) must end
before that residual block.  It can contain a later varying coordinate
only when that coordinate was put into \(X\).

Now suppose two strictly nested \(f(A)\)-sets \(F\subsetneq G\) were
both exposed.  Every updated prefix contains the first block \(X\), so
\(X\subseteq F\).  Choose

\[
 y\in G\setminus F.
\]

Then \(y\notin X\).  Its residual singleton lies after the residual
\(z_1\)-block, so no prefix excluding \(z_1\) can reach it.  This
contradicts exposure of \(G\). \(\square\)

Thus a directed transition from an \(A\)-checkpoint to an
\(f(A)\)-checkpoint needs at least two appended masks whenever the latter
checkpoint must expose two annular sets.  The reverse directed transition
need not have this truncated obstruction: one mask may put the least
required \(A\)-set into the new first block and leave its later increments
in their old order.  Direction is therefore load-bearing.

There is a second directed obstruction needed in odd dimension.  The
last-star child is

\[
 \ell(A)=(L+z_d;z_1,z_2,\ldots,z_{d-2}).
\tag{2.3}
\]

### Lemma 2.2 (truncated reverse-last-star barrier)

Suppose a state exposes a saturated lower-annular subchain of
\(\ell(A)\), so every displayed member contains \(z_d\).  Suppose the
corresponding lower-annular members of \(A\) exclude \(z_d\).  Then one
move-to-front update exposes at most one member of that \(A\)-subchain.

#### Proof

In the source state, \(z_d\) belongs to the prefix forming the least
displayed member, before all later varying singleton blocks.  Every target
set excludes \(z_d\).  The proof of Lemma 2.1 applies verbatim with
\(z_d\) as the forbidden prefix coordinate: if \(z_d\in X\), every new
prefix is contaminated; if \(z_d\notin X\), its residual block precedes
every unselected later increment.  Two strictly nested target sets would
require reaching an increment after that block. \(\square\)

## 3. The recursive GMM order contains linearly many annular barriers

The odd-dimensional GMM SCD-compatible Hamilton recursion replaces every
ordinary parent chain \(C\) in dimension \(2m-1\) by four chains in
dimension \(2m+1\):

\[
 A=*C*,\qquad \ell(A),\qquad \ell(f(A)),\qquad f(A),
\tag{3.1}
\]

in the displayed order or its reverse.  Here \(\ell\) is the
last-star operation.

The operations commute on an ordinary long template:

\[
 \ell(f(A))=f(\ell(A)).
\]

In the displayed orientation, the boundary

\[
 \ell(A)\longrightarrow f(\ell(A))
\tag{3.2}
\]

is directed first-star.  In the reverse orientation, the final internal
boundary is

\[
 \ell(A)\longrightarrow A
\tag{3.3}
\]

and is a directed reverse-last-star boundary.  Hence every parent block
contains at least one directed contaminant boundary, independently of its
orientation.

A parent chain in \(2^{[2m-1]}\) with minimum rank \(a\) gives
\(\ell(A)\) minimum rank \(a+1\) and
\(f(\ell(A))\) minimum rank \(a+2\).  Both possible directed boundary
targets reach the lower annulus boundary rank \(m-H\) whenever

\[
 a\le m-H-2.
\tag{3.4}
\]

The number of SCD chains with minimum rank at most \(r\) is exactly
\(\binom{2m-1}{r}\), because each such chain contains exactly one set of
rank \(r\).  Therefore (3.4) holds for exactly

\[
 B_{m,H}=\binom{2m-1}{m-H-2}
\tag{3.5}
\]

parent chains.  For each one, the relevant source and target contain every
rank from \(m-H\) to the centre.  Since \(H-h\to\infty\), their required
lower-annular truncations contain at least two consecutive members.  In
the displayed orientation Lemma 2.1 applies; in the reverse orientation
Lemma 2.2 applies.

### Theorem 3.1 (GMM annular schedule lower bound)

Every move-to-front schedule which visits the GMM chains in their
recursive order and exposes their assigned central and Gaussian-annular
members uses at least

\[
 \boxed{W+B_{m,H}-O(1)}
\tag{3.6}
\]

masks, apart from an arbitrary initial-state installation.

#### Proof

Two distinct SCD chains have different central members.  One MTF state
has at most one prefix union of a given rank, so distinct consecutive
chain checkpoints require at least one update.  This gives the ordinary
\(W-O(1)\) transition count.

For every parent counted in (3.5), one directed boundary is covered by
Lemma 2.1 or Lemma 2.2 according to the block orientation.  A single
update cannot reach a checkpoint exposing two consecutive members of the
target's required lower annulus, so that transition requires at least one
additional mask.  The parent blocks are disjoint in the recursive order.
Opening a cyclic order can delete at most one boundary.  Summing proves
(3.6). \(\square\)

### Proposition 3.2 (Gaussian density of long parents)

For fixed \(A>0\) and \(H=\lceil A\sqrt m\rceil\),

\[
 {B_{m,H}\over W}
 =\left({1\over4}+o_A(1)\right)e^{-A^2}.
\tag{3.7}
\]

#### Proof

Factor the ratio as

\[
 {\binom{2m-1}{m-H-2}\over\binom{2m+1}{m}}
 =
 {\binom{2m-1}{m-1}\over\binom{2m+1}{m}}
 {\binom{2m-1}{m-H-2}\over\binom{2m-1}{m-1}}.
\tag{3.8}
\]

The first factor is exactly

\[
 {m+1\over2(2m+1)}={1\over4}+O(m^{-1}).
\tag{3.9}
\]

The second is a product of central binomial ratios.  Uniformly for
\(H=A\sqrt m+O(1)\), its logarithm is

\[
 -{H^2\over m}+O_A(m^{-1/2}),
\tag{3.10}
\]

and hence it is \(e^{-A^2+o_A(1)}\).  Multiplication proves (3.7).
\(\square\)

Theorems 3.1 and Proposition 3.2 prove (0.4).  The fixed positive loss is
present for every fixed Gaussian \(A\).  Letting \(A\to\infty\) makes the
constant small, but that does not produce the required theorem for each
fixed \(A\), nor a uniform diagonal construction.

## 4. Exact complement/reflection obstructions

The natural way to obtain the upper right skeleton from the lower left
skeleton is to impose complement-reversal symmetry.  One fixed SCD cannot
support this exactly.

### Theorem 4.1 (no chainwise complement-stable SCD)

For every ground-set dimension \(n\ge2\), no symmetric chain
decomposition of \(2^{[n]}\) is permuted as a chain family by set
complementation.

#### Proof

The unique SCD chain containing \(\varnothing\) is a saturated maximal
chain from \(\varnothing\) to \([n]\).  If complementation permuted the
chain family, this chain would map to another chain containing both
endpoints, hence to itself.

Let its rank-one member be \(\{x\}\).  Nestedness forces its
rank-\((n-1)\) member to contain \(x\).  Complement stability would make
that member \([n]\setminus\{x\}\), which excludes \(x\), a contradiction.
\(\square\)

There is a separate obstruction at the Middle Levels chronology itself.

### Proposition 4.2 (reflection is impossible on a complement-invariant Middle Levels cycle)

If a Middle Levels Hamilton cycle in dimension \(2m+1\) is invariant
under complementation, the induced involution of the abstract cycle is a
half-turn.  It cannot be a reflection.  Consequently such a cycle can
exist only when

\[
 W=\binom{2m+1}{m}
\]

is odd, equivalently when \(m=2^t-1\).

#### Proof

Complementation has no fixed vertex.  A vertex-axis reflection is
therefore impossible.  An edge-axis reflection would fix an edge setwise
and exchange its endpoints, forcing an incidence edge

\[
 X--X^c.
\]

But \(X\not\subset X^c\), so no such Middle Levels edge exists.  The only
remaining fixed-point-free involution of a cycle is its half-turn.  The
half-turn swaps the two bipartition shores only when \(W\) is odd.  By
Lucas' theorem this is equivalent to

\[
 m\mathbin{\&}(m+1)=0,
\]

or \(m=2^t-1\). \(\square\)

Even in the Mersenne dimensions, a half-turn Middle Levels cycle controls
only its central incidence chronology.  It does not automatically extend
to complement-paired Gaussian SCD flags.  Theorem 4.1 prevents obtaining
that extension from one complement-stable SCD.

## 5. Exact surviving constructive target

The positive reduction and negative results leave a narrower endpoint
skeleton problem.

> **Low-prefix-barrier annular SCD schedule — open.**  Construct an SCD
> (or two coherently interleaved complementary SCDs) and a chain ordering
> with a move-to-front schedule of total length \(W+o_A(W)\), such that
> every chain's central and Gaussian-annular members are exposed.  Exact
> complement reflection is not required; the resulting word itself must
> supply both annular signs.

Any one-SCD solution gives the simultaneous flags by Theorem 1.2.  The
long-endpoint theorem guarantees that its word then has the required
positive-density Gaussian left and right skeletons, even though the MTF
checkpoints describe them as suffix flags.  What must change from the GMM
construction is now exact: on all but \(o(W)\) long-parent blocks, the
chain transition must avoid directed prefix contamination, or several
parent blocks must be handled by one genuinely nonlocal state change whose
total mask count is subadditive.

An alternative is a two-SCD schedule in which complementation exchanges
the decompositions rather than preserving either one.  Theorem 4.1 does
not obstruct that variant, but a common move-to-front chronology for the
two endpoint skeletons is not proved.

## 6. Status

Proved here:

1. the exact SCD-to-literal-word annular schedule reduction;
2. the directed first-star and reverse-last-star obstructions for
   truncated chain exposure;
3. the exact long-parent census and its Gaussian density;
4. a positive-density excess lower bound for the known GMM recursive
   order; and
5. the impossibility of exact one-SCD complement reflection.

Not proved here:

1. a noncanonical low-prefix-barrier SCD schedule;
2. a coherent two-SCD complement schedule;
3. a PBBS endpoint braid or coefficient one.

Thus the known SCD-extended Hamilton cycle and generic reflection symmetry
do not construct the required endpoint skeleton.  The exact positive
reduction survives, but it now demands a genuinely new chain ordering:
one with \(o(W)\), rather than positive-density, directed prefix
barriers on the Gaussian-long chains.
