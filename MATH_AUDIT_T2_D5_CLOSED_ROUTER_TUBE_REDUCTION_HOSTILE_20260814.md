# Hostile audit: the closed common-core C6 tube does not realize a D5 three-state reset

**Date:** 2026-08-14  
**Audited note:**
`MATH_REDUCTION_THREE_STATE_FIXED_BANK_RESIDENT_SWITCHBOX_TO_CLOSED_ROUTER_TUBE_20260814.md`  
**Verdict:** **FAIL** for the claimed exact composition reduction and D5
substitution.  The cited common-core carrier is a valid fixed-`X/Y` internal
trade, but both of its complete states have identity outer monodromy.  It
cannot implement a tail-fixed transposition.  Its derived immediate-lower
tickets also collide, and its terminal q2 collars are not audited.

## 1. Fatal permutation mismatch

Let `tau=(012)`.  The cited carrier has two stages.  In the old packet their
port actions are

\[
                             1,\quad 1,
\]

and in the new packet they are

\[
                    \tau^{-1},\quad\tau.              \tag{1.1}
\]

Therefore the complete old and new outer actions are both

\[
                             1.                         \tag{1.2}
\]

This is the point of the carrier's inverse-monodromy closure.  Its Theorem
4.1 explicitly says that both packets take `E_(0,i)` to `F_i`.

The D5 reset requested at a tail of state `a` is instead

\[
                   \rho_a=(bc),\qquad\{a,b,c\}=\{0,1,2\},   \tag{1.3}
\]

which fixes `a` and exchanges the other two terminals.  It is an odd
permutation.  A common-core `C6` matching contributes a three-cycle, hence an
even permutation.  Coordinate or terminal relabelling only conjugates a
permutation: it sends identity to identity and a three-cycle to a
three-cycle.  It cannot turn either `(1.1)` or `(1.2)` into `(1.3)`.

Consequently Section 3 of the audited reduction contains a direct
contradiction.  The instruction

```text
relabel the closed tube ... use the twist state to exchange the latter two
```

is impossible for this packet.  Suppressing the complete tube yields the
same outer matching in both states, not the frozen D5 incidence toggle.

### Why the composition lemma does not rescue it

For the two-stage state pair

```text
pass  = pass/pass,
twist = twist/twist,
```

the two boundary permutations are `1` and `tau^(-1) tau=1`.  Calling the
second state “twist” records an internal trade, not a terminal twist.  Using
only one twisted stage exposes `tau` or `tau^(-1)`, but then the packet is not
closed and still is not the transposition `(1.3)`.

One could attach D5 paths at the intermediate `E_1` seam, where a nontrivial
three-cycle is visible.  That would be a tapped multi-boundary gadget: the
seam vertices currently have degree two, so opening them changes the bank,
the collar list, and the substitution topology.  No such theorem appears in
the audited note or the cited carrier.

This alone invalidates Lemma 1.1 as applied in Section 2 and Theorem 3.1.

## 2. What the existing carrier really fixes

The H100 replay independently substituted every displayed set formula in the
rank-10 packet.  It confirms:

```text
ground set                                      20
old/new owner X bank                   33 = 33, simple
old/new immediate-upper Y bank         30 = 30, simple
old/new outer action                 identity = identity
old/new internal lower residence                  PASS
old/new internal upper residence                  PASS.
```

Thus the common-core carrier is a genuine literal, internally resident
zero-monodromy trade.  The audit does not challenge that theorem.

It is not, however, a fixed bank in the stronger occurrence-simple
three-ledger sense required by the D5 reset interface.

## 3. Immediate-lower collision

The derived immediate-lower ticket on a Johnson edge `XX'` is `X intersect
X'`.  The old and new ticket **multisets** are equal, as also follows from
the carrier's `Delta_1=0`.  They contain 30 occurrences but only 26 literal
sets:

```text
multiplicity 1: 24 tickets
multiplicity 3:  2 tickets.                              (3.1)
```

The two triple tickets are precisely the stage common cores

\[
\begin{aligned}
 K_1&=\{h,k_1,t_{1,0},t_{1,1},t_{1,2},
             a_{0,0},a_{0,1},a_{0,2},b_0\},\\
 K_2&=\{h,a_{0,0},a_{0,1},a_{0,2},
             a_{1,0},a_{1,1},a_{1,2},b_0,b_1\}.
\end{aligned}                                           \tag{3.2}
\]

Each occurs once on each of the three rows, at the `R_s--E_(s+1)` seam.
The explicit signatures in the carrier note prove simplicity of the 33
`X` states and 30 `Y` colours; they do not separate the tickets in `(3.2)`.

Therefore the packet gives

\[
 \boxed{\text{equal owner/upper/lower-ticket multisets, but a nonsimple
 lower-ticket bank}.}                                  \tag{3.3}
\]

If the target compiler requires occurrence-distinct lower resources, another
tagging or seam-splitting construction is mandatory.  Private coordinate
relabeling between different boxes does not split three equal tickets inside
one box.

## 4. Q2 current and collar scope

The carrier is internally q2-biresident because every row is a minimum
geodesic: consecutive exchange supports are disjoint.  The H100 replay also
checks the immediate-upper trace directly.  This audit excludes external
terminal crossings; the cited carrier does not specify the D5 predecessor
and successor collars at its six outer ports.

The q2 support failure is real, but it is broader than the reduction states.
On the 27 internal three-owner windows per state, direct support comparison
gives

| q2 row | old support | new support | old targets lost |
|---|---:|---:|---:|
| lower triple intersection | 25 | 25 | 6 |
| upper triple union | 21 | 21 | 3 |

All nine losses have load one in the displayed internal bank.  Thus the
twelve signed atoms from the lower intersection calculation correspond to
six negative and six positive atoms, while the D5-facing upper-union current
has three further internal casualties.  A complete repair must cover both
rows and all terminal-crossing windows, not only the twelve lower atoms and
the cyclic word terms cited in the reduction.

Nonzero signed current alone would not prove support loss; the direct load
replay above does.  Conversely, q2 **residence** of a crossing collar does not
prove q2 **support-current** safety there.  These are separate tests.

There is also a gap in Lemma 1.1's additivity sentence.  The q2 current of a
concatenation is the sum of the two internal currents only after the windows
crossing the shared socket have been assigned and audited.  Condition 3
checks their transition-support disjointness, but condition 4 as written does
not include their target occurrences.  A seam-current hypothesis is needed.

## 5. D5 substitution does not follow

The three-colouring certificate says that 212 selected rows require one of
the transpositions `(1.3)`.  It does not say that an identity-boundary
internal trade can be substituted for each row.  In particular:

1. the complete C6 tube leaves the row's external successor unchanged;
2. its lower ticket bank has the collisions `(3.2)`;
3. its external predecessor/successor collars are unspecified; and
4. its internal upper and lower q2 support losses have no backup.

Hence suppressing 212 copies of this tube recovers 212 identity port maps,
not the selected incidence changes.  The independently verified `372 -> 1`
topology of the D5 toggle cannot be imported.

## 6. Corrected topology targets

There are two plausible escapes, neither proved by the audited reduction.

### 6.1 An odd local router

Construct a fixed-bank gadget whose pass/twist boundary actions are `1` and
one transposition `(bc)`.  A serial product of three-port common-core `C6`
routers cannot do this: their actions lie in `A_3`.  The smallest escape must
introduce an odd atom, for example a fourth dummy strand/tapped `C8`, or a
nonserial multi-boundary switch.

### 6.2 A global open-C6 atlas

The actual disjoint D5 matching permutation is even.  Its 41 alternating
circuits have 477 rows, so its sign is

\[
             (-1)^{\sum_Q(|Q|-1)}=(-1)^{477-41}=+1.    \tag{6.1}
\]

Equivalently, the frozen length histogram contains 16 even-length owner
cycles, an even number of odd circuit permutations.  Algebraically the full
D5 action therefore admits a decomposition into three-cycles.  This makes
**open** C6 routers a potentially relevant global atlas.  One would still
need to realize that decomposition on literal D5 ports, close only the
unwanted auxiliary monodromy, separate the repeated lower tickets, and audit
all q2 currents.  The inverse pair in the cited closed tube instead erases
the very boundary action that D5 needs.

## 7. Exact verifier

The independent verifier is

```text
scratch/audit_t2_d5_closed_router_tube_reduction_20260814.py
```

and ran only on H100.  Its source/output SHA-256 values are

```text
e7a277d633e31abcb4d01ca91ff9eaafefa92e964625598126eb481a7dd980c9
9198f9c1470c31717f4f1cffa43eef100900de2ee178b9def0e00d95463c7a33.
```

The audited reduction was not assigned a frozen SHA because its central
mathematical implication fails.  The sharp verdict is

\[
 \boxed{\text{valid zero-monodromy common-X/Y carrier}
 \not\Longrightarrow
 \text{tail-fixed D5 reset switchbox}.}
\]
