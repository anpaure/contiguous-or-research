# Independent audit of the coherent-birail multi-depth Markov basis

> **Subsequent physical-scope correction.**  This audit authenticates the
> finite `C6/C8` state matrices and their integer kernels.  It does not
> authenticate the literal Klein four-block `C8` as a simple-owner,
> strict-q1 physical carrier.  That stronger reading is refuted by
> `scratch/audit_c8_fourblock_physical_owner_palette_nogo_20260801.py` and
> its frozen JSON; the toric conclusions here remain valid.

Date: 2026-08-01  
Verdict: PASS after the strict-\(q1\) scope and complete-terminal-matching
corrections recorded below.

## 1. Cubic \(C_6\) fibre

With cells ordered

\[
             12,13,21,23,31,32,
\]

the three slot sums and the three prefix/suffix label margins have integer
kernel

\[
 \mathbb Z(1,-1,-1,1,1,-1).
\]

Thus the toric ideal is principal,

\[
 x_{12}x_{23}x_{31}-x_{13}x_{21}x_{32},
\]

which is the same binomial as the theorem's orientation convention.  The
support \(K_{3,3}-I\) is chordless \(C_6\), so no supported square exists.

The dependency-free replay exhausts all 64 binary tables.  Their exact
margin signatures give

\[
                 62\text{ singleton fibres}
                 \quad+\quad1\text{ two-state fibre}.
\]

The two-state fibre is the unit-margin fibre, and its difference is the
displayed primitive cubic.  The depth-three audit independently finds four
formal product signs but only two diagonally coherent physical signs.

## 2. Prepared-family generalization

For occurrence-labelled slots of types \(12,23,31\), the allowed graph has
only three label vertices.  Every chordless circuit is therefore either:

1. a \(C_4\) on two distinct slots of one pair type; or
2. a \(C_6\) on one slot of each of the three pair types.

Even-cycle decomposition proves that the supported quadrics and cubics
connect every nonnegative fixed-margin fibre.  If all three active pair
types remain, the selected one-of-each induced \(C_6\) supplies a
unit-margin fibre with no square, so its cubic obstruction is genuine.
The degree-three bound is uniform in \(d\) because one cell carries its
entire deterministic prefix/suffix provider chain.

## 3. Strict-rainbow scope

The common-flag three-packet physical triangle repeats exactly three
cross-packet lower-\(q1\) socket colours.  Its \(C_6\) theorem is therefore
an exact nested lower-provider quotient, not an all-\(d\) strict-rainbow
prepared bank.  Disjoint exterior halos do not repair this internal
collision.

The theorem now states the correct comparison:

* at \(d=2,3\), distinct-filler three-packet cubics are owner- and
  \(q1\)-palette-disjoint;
* uniformly for all \(d\ge2\), the authenticated strict-rainbow twisted
  cube has the chordless \(C_8\) table and one indispensable quartic;
* arbitrary-core rainbow cubic existence for \(d\ge4\) remains open.

The replay exhausts all 256 binary \(C_8\) tables and obtains

\[
                254\text{ singleton fibres}
                \quad+\quad1\text{ two-state fibre},
\]

with the generator and structural zeros stated in the theorem.

## 4. CBC and terminal split

The corrected CBC implication is valid.  For the three-label occurrence
support, literal closure under every applicable whole-chain \(C_4/C_6\),
preservation of the physical class, and occurrence-label fidelity lift an
abstract Markov path step by step.  Square-completeness is unnecessary.
This is a conditional lift theorem, not a proof of packet availability.

The terminal split theorem is also valid with its final hypotheses:

1. the old matching is complete on the entire declared strict-lower bank;
2. a named set \(R\) of its edges is released;
3. every lost width-\(h\) crossing cell has a legal rank-\(m\)
   length-\((h+1)\) hull;
4. \(R\) together with the genuinely new targets matches literally into
   the singleton/two-ray side cells; and
5. all rows occur in one legal common-cap word.

Under these assumptions compiler defect need not factor through the birail
matrix.  The split construction transports the unreleased matching and
installs the replacement rows directly.  In the original scope this left a
pivot-rich terminal-source existence condition.  That local condition is
now superseded by
`MATH_THEOREM_SHARP_PIVOT_APERTURE_AND_RESIDENT_GEODESIC_PACKET_20260801.md`:
the noncanonical pivot-rich geodesic packet is proved.  What remains here is
its ambient common-cap/host embedding, not existence of the local packet.

The sharper actual-letter split in Theorem 7.3 is also exact.  If the old
source contains the merged letter

\[
 X=(A\cup\{f_1\})\cup(B\cup\{f_d\})
\]

between the two mirrored filler traces, splitting it into the two displayed
bases preserves every old interval and realizes both complete coatom flags
on the exclusive rays at cost one.  This removes rank saturation and
compiler factorization on that face.  The canonical \(0110\) source does
not contain the merged host, so the result remains a conditional terminal
theorem rather than an all-\(k\) construction.

## 5. Audit artifacts

~~~text
scratch/audit_r_coherent_birail_multidepth_markov_basis_20260801.py
scratch/r_coherent_birail_multidepth_markov_basis_20260801.audit.json
~~~

Replay status:

~~~text
PASS_R_COHERENT_BIRAIL_MULTIDEPTH_MARKOV_BASIS
~~~

Payload SHA-256:

~~~text
57f11efab00a9343eb0989510fa5800edd5a076101a09bb7bace07c2b38d9e66
~~~
