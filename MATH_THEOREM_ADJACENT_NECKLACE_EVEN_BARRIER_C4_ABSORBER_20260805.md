# Adjacent necklaces: the even-barrier socket has an exact four-cycle absorber

**Date:** 2026-08-05  
**Method:** four literal adjacent transfers; no computation  
**Status:** unconditional.  It closes the even-barrier socket left by the
short-run macro/gap reduction, provided its uniquely associated long-run
state is reserved from the earlier long-run receiver stage.

## 0. The four states

Let `m>=2` be even and let `e>=1`.  In a cyclic exterior context whose
displayed endpoints are separated from every other positive run, put

\[
\begin{aligned}
 S&=(m,0,1,0^{e+1}),\\
 E&=(m,0,0,1,0^e),\\
 D&=(m-1,1,0,1,0^e),\\
 T&=(m-1,1,1,0^{e+1}).
\end{aligned}                                      \tag{0.1}
\]

All four words have the same coordinate length `e+4` and the same chip
mass `m+1`.

Here:

* `S` is a singleton-key mixed-barrier source: a length-two nonunit
  barrier followed by the first unit of an odd unit segment;
* `E` is the receiver obtained by sliding that unit one place right;
* `D` is the other short all-quiet phase of the even-mass length-three
  barrier; and
* `T` is an all-quiet positive run of length three, with terminal quiet
  pair `(1,1)`.

## 1. Literal four-cycle

### Theorem 1.1 (even-barrier square)

The four necklace vertices in (0.1) are distinct and span the cycle

\[
                              S-E-D-T-S.             \tag{1.1}
\]

Every edge is one adjacent unit transfer.  Consequently the opposite edge
set

\[
                              \{SE,DT\}              \tag{1.2}
\]

saturates all four vertices.

### Proof

The four transfers are visible locally:

\[
\begin{array}{rcll}
S\longrightarrow E
 &: & (0,1)\mapsto(0,0,1) &
 \text{(slide the isolated unit right)},\\[2mm]
E\longrightarrow D
 &: & (m,0)\mapsto(m-1,1) &
 \text{(move one chip into the first zero)},\\[2mm]
D\longrightarrow T
 &: & (0,1)\mapsto(1,0) &
 \text{(move the following isolated unit left)},\\[2mm]
T\longrightarrow S
 &: & (m-1,1)\mapsto(m,0) &
 \text{(collapse the first two entries)}.
\end{array}                                         \tag{1.3}
\]

More explicitly, these are

\[
\begin{aligned}
(m,0,1,0^{e+1})&\leftrightarrow(m,0,0,1,0^e),\\
(m,0,0,1,0^e)&\leftrightarrow(m-1,1,0,1,0^e),\\
(m-1,1,0,1,0^e)&\leftrightarrow(m-1,1,1,0^{e+1}),\\
(m-1,1,1,0^{e+1})&\leftrightarrow(m,0,1,0^{e+1}).
\end{aligned}                                      \tag{1.4}
\]

The four run-type signatures are respectively

\[
\begin{array}{c|c}
S&\text{all singleton runs; every nonunit block has length two},\\
E&\text{all singleton runs; one even nonunit block has length three},\\
D&\text{one distinguished two-slot run }(m-1,1),\\
T&\text{one distinguished three-slot run }(m-1,1,1).
\end{array}                                        \tag{1.5}
\]

They are therefore distinct.  The same signatures also distinguish them
after insertion into a cyclic exterior context of singleton runs.  This
proves (1.1), and (1.2) is a matching of the cycle.  \(\square\)

## 2. Collision-free planting over all singleton-key sources

In the mixed-barrier reduction, every source `S` chosen for the boundary
exit has:

1. all nonunit blocks of length two;
2. one canonically selected odd unit segment;
3. an odd positive extra `e` at the first unit of that segment; and
4. a canonically selected preceding barrier.

For an even selected barrier, associate the four states (0.1).

### Theorem 2.1 (disjoint square bank)

Squares associated with distinct source necklace classes are
vertex-disjoint.  The construction is valid for periodic mass/barrier
skeletons.

### Proof

The source `S` determines its chosen segment necklace-invariantly by the
least-representative rule used in the mixed-barrier reduction.  If several
least representatives occur, they differ by the stabilizer and produce
the same four necklace classes.

Conversely:

* from `E`, locate its unique nonunit macroblock of length three and slide
  the following unit left;
* from `D`, locate its unique distinguished two-slot run whose total is the
  even barrier mass and reverse the `E--D` transfer;
* from `T`, locate its unique distinguished three-slot run ending in
  `(1,1)` and reverse the `S--T` transfer.

Each reconstruction recovers `S`, the selected barrier, and `e`.  Hence
none of `E,D,T` can be shared by two source squares.  The run signatures
(1.5) prevent a vertex of one role from appearing in another role.  Thus
the square bank is vertex-disjoint.  \(\square\)

The uniqueness assertions here are relative to the reduced source domain:
all other source runs are singletons and all other nonunit barriers have
length two.  This is exactly the domain established before the square is
used.

## 3. Stage-order compatibility

The two vertices `E,D` are precisely the two phases

\[
                    E(m,3)=(m,0,0),\qquad
                    D(m,3)=(m-1,1,0)                \tag{3.1}
\]

of the movable even-mass macroblock.  In the source exterior there are no
other movable macroblocks, so their macro phase fibre has dimension one
and consists exactly of `E,D`.  Replacing its usual matching edge `ED` by
the two edges in (1.2) therefore leaves no phase-fibre casualty.

The vertex `T` is an all-quiet long-run source: in its length-three run,
the first entry is unpaired and the terminal pair is `(1,1)`.  Reserve `T`
before applying the general long-run receiver injection.  Because the
square bank is injective, this deletes one distinct long-run source per
square and no receiver.  The long-run injection remains injective on the
restricted source domain.

Thus the exact safe order is:

1. identify all mixed singleton-key sources and their squares;
2. reserve the associated `E,D,T` vertices;
3. take `SE` and `DT` in every even-barrier square;
4. use the direct `SE` edge at every odd barrier; and only then
5. apply the ordinary macro-phase and long-run matchings on what remains.

No vertex is used twice.

## 4. Mixed-barrier closure

Combine Theorem 1.1 with the gap-pair reduction.

### Corollary 4.1

Every singleton-key mixed-barrier source is saturated without exporting a
socket:

* at an odd barrier `m>=3`, use its direct marked edge `S--E` and reserve
  `E` from the long-odd-singleton exit stage;
* at an even barrier, use the square matching `SE,DT`.

Consequently the mixed family (0.5) of the short-run macro reduction has a
complete matching after all nonsingleton gap-key fibres are matched.

The only recursive residue of the short all-quiet core is the all-unit
face

\[
                            G_{p,q-2p}\cong G_{q-2p,p},
\]

whose odd coordinate length `q-2p` is strictly smaller than `q`.

### Proof

The periodic gap-key quotient matching saturates every nonsingleton key
fibre.  In a singleton key fibre, parity produces the canonical boundary
source `S`.  If its preceding barrier is odd, the uniquely marked direct
edge consumes both endpoints.  If it is even, Theorems 1.1 and 2.1 consume
the disjoint four-vertex square.  Section 3 proves compatibility with all
surrounding stages.  These are the only possible barrier parities.
\(\square\)

## 5. Scope

### Corollary 5.1 (strong-induction closure of the final all-unit face)

Fix one boundary-shell mass `s`.  Assume that, for every positive odd
`q'<q` and every mass `b`, the full adjacent-necklace graph `G_(q',b)` has
a matching of deficiency at most one.  Then the final all-unit face of the
short all-quiet core has a matching of deficiency at most one.

Indeed, Corollary 4.1 perfectly matches every mixed-barrier singleton
fibre.  In the remaining all-unit domain,
the number `p` of positive runs equals the fixed shell mass `s`, because
every positive coordinate carries one chip.  This domain is the single
full graph

\[
                    G_{p,q-2p}\cong G_{q-2p,p},     \tag{5.1}
\]

where `q-2p` is positive, odd, and smaller than `q`; apply the induction
hypothesis.  There is no sum over different values of `p` inside one
shell.  Hence this final face contributes at most one monomer.  The
adaptive radial theorem can transport that arbitrary monomer to the next
shell without requiring a prescribed socket.

This does **not** yet prove the same statement for the complete short core.
The marked exit (4.1) of the preceding macro theorem sends a long-gap
odd-mass singleton into a nonquiet phase fibre.  Consuming that receiver
punctures the fibre, and many such punctures still require one joint
companion-consolidation theorem.  The C4 absorber closes the even-barrier
punctures only; it does not silently close this general receiver bank.

Proved:

1. a literal four-cycle around every even-barrier socket;
2. a collision-free square bank, including periodic skeletons;
3. exact compatibility with the macro-phase and long-run stages; and
4. complete elimination of the mixed-barrier residue without exported
   monomers.

Not proved here:

1. the protected strong-induction hypothesis for the all-unit smaller-slot
   graph;
2. deletion-stable composition with the earlier **general** long-run
   receiver bank in the next zero stratum;
3. terminal absorption of the globally forced parity monomer;
4. PBBS owner/q2-halo compatibility; or
5. any universal-word upper bound.
