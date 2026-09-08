# Adjacent necklaces: repeated hub fans reduce to a binary upward socket flow

**Date:** 2026-08-05  
**Method:** pair passive circulation petals and route each pair into one
adjacent double-expansion pair; no computation  
**Status:** unconditional occurrence-level reduction.  A hub colour used
with arbitrary multiplicity exports at most one singleton receiver, not one
per excess use.  All other receiver deletions occur in adjacent pairs one
cut level higher.  Quotient-coalesced packing of those receiver pairs and
extension of the next-level matching remain open.

## 1. Two passive petals make one balanced receiver pair

Let `x_H` be a literal hub.  Let two endpoint-disjoint shifted-cut edges
over it have cut-position pairs

\[
                         \{p,p+1\},
 \qquad                  \{r,r+1\}.
\tag{1.1}
\]

By the split-block compatibility lemma, every cross-choice of one cut from
each pair is jointly admissible.

Assume `x_H` has already been matched outside these two petals.  Orient the
first passive petal to expose

\[
                         y_p=x_{H\cup\{p\}},
\]

and the second to expose

\[
                         y_r=x_{H\cup\{r\}}.
\]

Define

\[
 z_0=x_{H\cup\{p,r\}},
 \qquad
 z_1=x_{H\cup\{p+1,r\}}.
\tag{1.2}
\]

Then

\[
                         y_pz_0,
 \qquad                  y_rz_1
\tag{1.3}
\]

are literal cut-insertion edges.  Moreover

\[
                         z_0z_1
\tag{1.4}
\]

is the shifted-cut horizontal edge `p <-> p+1` over the hub
`x_{H\cup\{r\}}`.

### Theorem 1.1 (balanced two-petal promotion)

If `x_H` is already saturated externally and `z_0,z_1` are fresh, the two
passive petals together with the edges (1.3) have a relative perfect
matching: every vertex other than the externally saturated hub is covered.
After adjoining the external matching edge at `x_H`, the whole gadget is
perfectly matched.  The only vertices consumed at the next cut level are
the adjacent pair `z_0z_1`.

#### Proof

In each passive petal, match its odd cycle after deleting the already used
hub `x_H`.  This covers the nonexposed critical endpoint and every
circulation interior.  The two edges in (1.3) cover the exposed endpoints
and the two receivers.  Joint admissibility proves that both receiver
states exist, and (1.4) proves that they form one complete adjacent pair at
the next level. \(\square\)

The same proof applies when `x_H` is not externally saturated but a third
petal is put in the active state.  The active petal covers the hub; any two
remaining passive petals are then promoted by Theorem 1.1.

## 2. Exact parity law for one hub fan

Let `d>=1` pairwise endpoint-disjoint shifted edges use one hub colour.
Let

\[
 \epsilon=
 \begin{cases}
 0,&\text{the hub is free and one petal may be active},\\
 1,&\text{the hub is already consumed by an incoming lower-level edge}.
 \end{cases}
\tag{2.1}
\]

The number of passive petals is

\[
                         m=d-1+\epsilon.
\tag{2.2}
\]

Pair as many passive petals as possible and apply Theorem 1.1 to each
pair.  If `m` is odd, one passive petal remains.  Give it one compatible
anchor cut and one single double-expansion receiver, as in the one-hub fan
promotion theorem.

When `epsilon=0`, the active petal itself supplies such an anchor cut.  If
`epsilon=1` and `d>=3`, one of the paired petals supplies it.  In the
degenerate state `epsilon=1,d=1`, the incoming lower-level receiver must
retain a cut which is compatible with one endpoint of the sole petal; this
is the only additional sidecar premise needed by the parity rule.

### Theorem 2.1 (binary hub-current law)

Provided the chosen receiver vertices are fresh and pairwise distinct, and
subject in the exceptional state `epsilon=1,d=1` to the compatible-anchor
premise above, all `d` petals at one literal hub can be saturated using:

\[
 \left\lfloor{d-1+\epsilon\over2}\right\rfloor
 \quad\text{adjacent receiver pairs}
\]

and

\[
                         \eta=d-1+\epsilon\pmod2
\tag{2.3}
\]

singleton receivers, where `eta` is zero or one.

Thus arbitrary hub multiplicity exports at most one singleton deletion.
The outgoing binary state satisfies

\[
                         \boxed{\eta\equiv d-1+\epsilon\pmod2.}
\tag{2.4}
\]

#### Proof

Use one active petal exactly when `epsilon=0`; all remaining petals are
passive.  Pair the passive petals.  Every pair is closed by Theorem 1.1,
and an odd final passive petal is closed by one single receiver.  All
circulation interiors at this cut level are distinct by fixed-level
injectivity.  Formula (2.4) is the parity of the number of passive petals.
\(\square\)

## 3. Strictly increasing potential

If the petal endpoints have `k` cuts, every receiver in Sections 1--2 has
`k+1` cuts.  Therefore

\[
                         \Phi(x)=\#\{\text{cuts of }x\}
\tag{3.1}
\]

strictly increases along every exported singleton or paired receiver.
The resulting dependency graph is a DAG.  No receiver can reopen a lower
cut level.

This dictates the proof order: construct the global ear system from low
cut count upward, carrying only:

1. disjoint adjacent receiver pairs already saturated from below; and
2. at most one occurrence-labelled singleton state at any routed socket,
   together with its retained anchor cut.

The top cut level is terminal.  In the `q=3 mod 6` branch its exceptional
special path is closed by the three-tail two-blossom reset, with only the
`q=3` parity socket.

## 4. The exact next-level extension gate

An adjacent receiver pair `z_0z_1` is not matched by that horizontal edge:
its two vertices are already saturated by the lower vertical edges (1.3).
Nevertheless it is a **balanced prescribed deletion**.  If a
next-level critical matching can be chosen to contain the abstract edge
`z_0z_1`, deleting that edge leaves a matching of every other vertex and
introduces no socket.

Consequently the remaining ordinary-sector theorem can be stated without
arbitrary hub multiplicities.

> **Protected capacity-two extension theorem.**  At every cut level,
> after deleting the adjacent receiver-pair bank generated below and at
> most one marked incoming singleton, choose parity-optimal matchings of
> the capacity-two sectors modulo their odd rotational stabilizers which:
>
> 1. extend every prescribed receiver-pair edge abstractly;
> 2. respect the two hub colours contracted by the special reset;
> 3. admit the fan pairing of Theorem 2.1; and
> 4. route the resulting singleton currents upward according to (2.4),
>    leaving at most one terminal radial socket.

Because the potential (3.1) is strict, this is a triangular extension
problem rather than a cyclic regeneration problem.  What remains hard is
the extension/Hall condition inside one level, not feedback to an earlier
level.

## 5. Quotient boundary

The construction above is literal and occurrence-labelled.  Before taking
necklace quotients, each passive pair has four possible adjacent receiver
pairs, obtained by choosing its two orientations.  After quotienting,
different pointed pairs can coalesce.  A global proof must choose
pairwise-disjoint receiver **orbits**, not merely pointed states.

Thus Theorem 2.1 proves the parity and level structure but does not silently
prove the orbit packing.  A bipartite SDR whose right vertices are
receiver-**edge** orbits is only necessary: distinct edge orbits may share
a receiver vertex orbit.  The exact selector must price both endpoint
capacity and extension to the next-level matching.

`MATH_THEOREM_PAIRED_RECEIVER_SQUARE_AUGMENTATION_AND_EVEN_LEVEL_TU_20260805.md`
does this without a post-hoc extension step.  Each passive pair gives a
quotient-stable `K_(2,2)` receiver rectangle; adding two private vertices
per passive pair turns receiver selection, endpoint disjointness,
next-level extension, the two contracted reset colours, and the possible
singleton into one augmented perfect-matching problem.  At even cut
length its exact cuts are Hall/TU cuts; at odd cut length they are Tutte
blossom cuts.

## 6. Scope

Proved:

1. a literal perfect two-petal promotion using an adjacent receiver pair;
2. the exact binary hub-current law (2.4);
3. at most one singleton receiver per arbitrarily large hub colour class;
4. strict increase of cut level, hence acyclicity of the global dependency;
5. reduction of the global problem to protected within-level matching
   extension plus an occurrence-coalesced receiver-edge SDR.

Not proved:

1. the protected capacity-two extension theorem;
2. Hall for every even-level augmented receiver graph and Tutte for every
   odd-level augmented receiver graph;
3. collision-free cross-level circulation phase assignment;
4. preservation of the PBBS physical halo; or
5. the complete adjacent-necklace theorem.
