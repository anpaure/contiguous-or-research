# K16 exact229 restricted-A endpoint rigidity

Date: 2026-07-30  
Lane: AD, split-packet source return  
Status: **proved exhaustive finite no-go for the stated two-packet face**

## 1. Frozen antecedent and exact scope

The source chronology is

`scratch/root_k16_a_fourtoken_q1hole_direct_moves_20260730/best_upper_complete_bad2.targets`

with SHA-256

`dc336b93f981d09bbba9f44969bef46da51c6feeab595b05c2fd6b26b340638d`.

Fix

\[
 B=[1266,1295)
\]

with reverse orientation.  Let (A'=[a,b)) be any nonempty contiguous
subinterval of

\[
 A=[2186,2217).
\]

Orient (A') forward or backward, and insert (A') and (B), consecutively
in either order, immediately before old row 3846.  Delete the two source
occurrences.  No row value is changed.

Source and destination legality mean the literal depth-three identity on
every crossing seven-row window.  Any seam survivor is then checked by the
complete variable-depth middle replay and by unrestricted upper interval-OR
enumeration.  Thus this face has no run-length surrogate and no fixed-window
upper restriction.

The face does **not** include a third packet, a gap between the two inserted
packets, a changed (B), a moving destination, or replacement of a boundary
row.

## 2. Exact finite size

There are

\[
 \binom{31+1}{2}=496
\]

nonempty subintervals of (A).  Two orientations and two destination orders
give exactly

\[
 4\cdot496=1984
\tag{2.1}
\]

formal choices.  Length-one orientation labels can describe the same word;
(2.1) is the exact labelled model size used in the exhaustive theorem.

## 3. Restricted-A rigidity theorem

### Theorem 3.1

Among the 1984 formal choices in Section 1:

1. exactly 33 unoriented intervals close their source gap;
2. hence exactly 132 formal choices survive the source test;
3. exactly one formal choice survives the destination test;
4. that choice is

   \[
   A'=[2186,2217),\quad\text{forward},\quad\text{order }AB;
   \]

5. its materialized chronology is byte-for-byte the already frozen
   `exact_229.targets`, SHA-256

   `cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974`;

6. this sole survivor has exact middle capacity 32063, equality positions
   (6320,12869,12871), no zero source envelope, and no upper hole.

In particular, no proper subinterval of (A) gives an exact two-packet
chronology in this face.

### Proof

For a source interval ([a,b)), only the six old rows immediately before
(a) and the six old rows immediately after (b) can participate in a new
depth-three window.  Concatenate those two six-row strings and test each of
the six crossing seven-row windows.  For a seven-row string
(x_0,\ldots,x_6), the exact test is

\[
 e_j=x_j\cap x_{j+1}\cap x_{j+2}\cap x_{j+3}\ne\varnothing
 \quad(0\le j\le3),
\]

and

\[
 e_0\cup e_1\cup e_2\cup e_3=x_3.
\tag{3.1}
\]

Applying (3.1) to all 496 source gaps leaves the 33 intervals frozen in the
audit artifact.  Orientation does not affect source closure, and there are
two destination orders, giving (33\cdot4=132) formal source survivors.

For each survivor, concatenate the six rows before old row 3846, the two
oriented packets in the chosen order, and the six rows beginning at old row
3846.  Apply (3.1) to every crossing window.  Exactly one concatenation
passes: full (A), forward, followed by (B).  Literal deletion/insertion
then reproduces `exact_229.targets`; the independently implemented complete
middle and upper replays give the values in item 6.  The audit contains every
source-surviving interval and the unique destination survivor.  This proves
the finite statement.  □

### Boundary-state factorization

Let (L) and (R) be the six frozen rows immediately to the left and right
of the destination.  The fixed reversed packet (B) satisfies

\[
 L\not\to B,qquad B\to R.
\tag{3.2}
\]

Thus every order (BA') is killed at its first seam, independently of the
choice of (A').  Nine of the 33 source-exact intervals have length at least
six, so their three destination seams factor without overlap.  In forward
orientation,

\[
 L\to A'
\]

holds only for the prefix `[2186,2200)` and full (A), while

\[
 A'\to B
\]

holds only for the suffix `[2200,2217)` and full (A).  Their sole common
choice is full (A).  No reversed long interval passes either required
boundary family.  The remaining 24 short intervals were checked with the
overlapping windows intact, and none passes.  Hence the destination literally
demands both the left boundary state and right boundary state of (A); a
third packet must replace one of these states rather than merely add an
arbitrary exact source block.

## 4. Endpoint-halo consequence

The two source endpoint charts isolated by the exact233 comparison are
supported inside the untouched target halos

\[
 [2183,2192)\qquad\text{and}\qquad[2214,2223).
\tag{4.1}
\]

Exactly 27 of the 33 source-exact intervals satisfy

\[
 2192\le a<b\le2214.
\tag{4.2}
\]

Therefore they leave both complete halos in (4.1) literally unchanged.
Those halos carry the five pairwise-distinct local lower cells already
authenticated in the exact233 exchange:

| shore target | canonical source interval | allowed | mandatory |
|---|---:|---:|---:|
| `091d` | `[2186,2188)` | `091d` | `001d` |
| `291c` | `[2187,2189)` | `291c` | `2014` |
| `291d` | `[2186,2189)` | `291d` | `201d` |
| `2e28` | `[2217,2219)` | `2e28` | `0e00` |
| `2f28` | `[2217,2220)` | `2f28` | `0f08` |

The table uses original-source tuple labels, not final numerical word
positions.  Removing (B) translates both charts left by 29 rows; removing
an interior (A') translates the suffix chart by a further (|A'|).  Their
masks and local legality are unchanged.

The five targets lie in five different deficiency-one components of the
frozen exact229 (212/187) Hall shore.  More explicitly, relative to the
frozen exact229 matching, the following five augmenting paths are
vertex-disjoint (each parenthesized tuple is a canonical source-tuple cell):

```text
095d -- (6126,6127,6128) --M-- 091d --NEW-- (2186,2187)
291d --NEW-- (2186,2187,2188)
a91c -- (8626,8627) --M-- 291c --NEW-- (2187,2188)
6e28 -- (4049,4050,4051) --M-- 2e28 --NEW-- (2217,2218)
2f28 --NEW-- (2217,2218,2219) --M-- 2c0c -- (5461)
```

Consequently, **conditional on retention of the displayed old path edges**
(in particular, retention of all 187 old shore cells suffices), flipping the
five paths produces five more matched targets and lowers the frozen shore gap
from 25 to at most 20.

This invariance was not inferred from the displayed target masks alone.  For
each of the 27 source-exact intervals, the audit reconstructs dynamic depths,
maximal envelopes, every relevant bit carrier, and the exact
`(allowed,mandatory)` signature of all five cells.  All 135 signatures agree
with the table.

This is a local Hall dividend, not a completed chronology: Theorem 3.1 proves
that all

\[
 27\cdot2\cdot2=108
\]

formal choices preserving both endpoint halos fail already at the exact
destination seam.  Thus the simple strategy “move an interior part of (A)
and leave both endpoint palettes at the source” is closed.

## 5. Sharp remaining escape

The failure is destination rigidity, not source rigidity and not an upper
shadow obstruction.  A successful source-return construction must change at
least one hypothesis of Theorem 3.1.  In particular it must use one or more
of:

1. a third packet/buffer between (A') and (B);
2. nonconsecutive placement of the two packets;
3. a moving destination or changed boundary row;
4. a modified (B) packet.

This identifies the **proper interior subpacket**
(A'\subsetneq A), fixed-(B), one-extra-packet census as the minimal next
literal face that can retain both source halos; the fixed-full-(A)+C face
keeps the five ears deleted.  Merely shortening (A) without the extra packet
cannot preserve the five source ears while retaining exact229 destination
service.

## 6. Reproducible audit

Independent standard-library replay:

`scratch/audit_ad_k16_exact229_restricted_a_face_20260730.py`

SHA-256:

`c86279919f45a2a5d039d7ec1917d01d296526816fa9d8deb78a5a1bf2a97fd5`.

Frozen compact result:

`scratch/ad_k16_bad2_splitpair_exact_20260730/exact229_restricted_a_face.ad.audit.json`

SHA-256:

`2cc3b1e48d7d1375c6c80c752d97464b8fe7e81ef1f0277b91072d824328e1b9`.

Its stable payload SHA-256 is

`549b43b8682209d02839d72dd073cfe82de8af90f6ba372c65ef6a780cbf9949`.
