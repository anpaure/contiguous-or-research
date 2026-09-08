# Pointwise screens cannot close the folded-C8 graded residue

Date: 2026-08-01  
Lane: H2, quotient-folded C8 physical/compiler interface  
Status: solver-free composition lemma plus exact exhaustive replay of every
ray-clean folded Hamilton face for `2<=d<=12`.  This is a scoped obstruction
to phase-common screened composition, not a no-go for phase-sensitive
collars, quotient overlaps, or other folds.

## 0. Result

The quotient fold and the isolated two-host component solve two different
problems:

* the fold gives a simple owner Hamilton carrier and two exclusive nested
  source rays;
* the opposite two-host word supplies exactly the missing **set values** and
  has zero abstract terminal Hall defect after antitone pairing.

They do not form a graded contextual relation merely by juxtaposition and a
common screen.  For the four relevant folded faces, the exact signed
width-graded distances after adding the opposite ray component are:

| folded face | upper support after cut | same-address anchors | folded `L1` | residual `L1` |
|---|---:|---:|---:|---:|
| minimum signature | 15 | no | `6d+4` | `2d+8` |
| aligned upper-15 | 15 | yes | `10d+12` | `6d+16` |
| minimum upper-safe | 16 | no | `10d+20` | `6d+24` |
| minimum upper-safe and aligned | 16 | yes | `22d+44` | `18d+48` |

The last face is nonempty: there are exactly `4d+4` upper-safe aligned rows
in the authenticated catalogue, and its minimum has common ray-base
addresses

\[
                         p=4d+10,\qquad q=5d+10.       \tag{0.1}
\]

Thus the earlier statement “upper-safe has no aligned sockets” is false if
alignment is allowed at addresses other than `4d+12,5d+12`.  What remains
true is stronger and more relevant: none of the four faces is closed by the
opposite ray component plus a phase-common pointwise screen.

## 1. The pointwise-screen additivity lemma

For a finite word `W`, let `D(W)` be the counter indexed by `(width,OR
value)` of all nonempty intervals, and put

\[
                  \Delta(W_0,W_1)=D(W_0)-D(W_1).       \tag{1.1}
\]

Consider two phase pairs `A_0,A_1` and `B_0,B_1`.  Suppose a seam/collar is
inserted so that every interval meeting both sides has the same OR value at
the same width in phase zero and phase one.  Equivalently, the complete
suffix-by-prefix grid is pointwise phase common.  Then

\[
 \boxed{\Delta(A_0\mid B_0,A_1\mid B_1)
       =\Delta(A_0,A_1)+\Delta(B_0,B_1).}              \tag{1.2}
\]

Here the vertical bar may contain any common screen or common collar
satisfying the displayed pointwise condition.

### Proof

Partition the intervals of the concatenation into those wholly in `A`,
those wholly in `B`, and those meeting the seam.  The first two classes give
the two terms on the right of (1.2).  By hypothesis the third class has
identical addressed `(width,value)` entries in both phases, so its signed
counter is zero.  This proves (1.2).  The same partition shows that adding
arbitrary common exterior context changes neither side once the exposed
prefix and suffix grids are pointwise phase common.  \(\square\)

The lemma explains the correction conceptually: a common screen suppresses
the only cross term that could pay an internal graded residue.  Pointwise
screening is therefore incompatible with cancellation unless the two
internal signed decks already sum to zero.

## 2. Exact opposite-ray calculation

Suppress the fixed core and write

\[
\begin{array}{ll}
 L_0=za_3f_1,&L_1=za_1f_1,\\
 R_0=za_1f_d,&R_1=za_3f_d.
\end{array}                                             \tag{2.1}
\]

The isolated two-host words are

\[
 G_e=(L_0\cup L_1),L_e,zf_2,\ldots,zf_{d-1},R_e,
      (R_0\cup R_1).                                    \tag{2.2}
\]

They have graded distance `4d-4`.  Their exclusive set supports are exactly
the two prefix/suffix rays, so for every ray-clean folded source pair
`S_0,S_1`,

\[
 \operatorname{supp}D(S_0)\cup\operatorname{supp}D(G_1)
 =\operatorname{supp}D(S_1)\cup\operatorname{supp}D(G_0). \tag{2.3}
\]

Equation (2.3) is set-support equality only.  Applying (1.2) to the opposite
composition gives the nonzero rows in the table of Section 0.

The residual width profiles are exact:

1. minimum signature: one unit per sign at every width
   `3d+7,...,4d+10`;
2. aligned upper-15: one unit per sign at every width
   `2d+5,...,5d+12`;
3. minimum upper-safe: per-sign multiplicities `1,2,3,...,3,2,1` on
   `3d+6,...,4d+11`;
4. minimum upper-safe and aligned: the same capped-triangular profile on
   `2d+4,...,5d+13`.

The per-sign residual masses are respectively

\[
             d+4,\quad3d+8,\quad3d+12,\quad9d+24.     \tag{2.4}
\]

In particular, a valid contextual closure on one of these exact faces must
use a **phase-sensitive** seam grid whose signed counter is the negative of
the corresponding profile.  Formula (2.4) is an occurrence-debt lower
bound, not a source-length lower bound: one changed source letter can affect
many crossing intervals.

## 3. Relation to the antitone birail theorem

There is no contradiction with the exact abstract terminal Hall theorem.
For the canonical two-ray marginal on each shore,

\[
             \{0^{d-1},1,\ldots,d-1\},\qquad N=2d-2,   \tag{3.1}
\]

one has `E_L=E_R=d-1`, so antitone pairing gives Hall deficiency zero.  The
birail matching therefore closes **after** legal ray cells and arbitrary
pairing are available in one cap state.

The obstruction here is earlier and physical: source chronology must expose
those cells while also cancelling the addressed width profile in Section 2,
preserving owner rank, both q1 palettes, residence, and the transported
common-cap matching.  The isolated two-host theorem supplies the ray cells;
it does not supply this contextual composition.

## 4. Exact surviving gate

Any successful lift must do at least one of the following:

* use a phase-sensitive collar whose cross-grid counter pays the profile in
  Section 2;
* overlap/quotient source addresses so the residual occurrences are
  identified rather than added;
* choose another physical fold/cut outside the audited catalogue; or
* transport the residual occurrences into an ambient matching-closed bank
  and prove they are recycled without accumulating `chi`.

A common phase-independent screen, even one which equalizes every exposed
prefix and suffix pointwise, cannot do this by (1.2).  Consequently the
remaining all-dimensional theorem is not two-ray Hall; it is a
phase-sensitive owner-legal host/regeneration theorem.

## 5. Replay

Run

```text
PYTHONPATH=scratch python3 \
  scratch/audit_h2_c8_pointwise_screened_composition_residue_20260801.py --write
```

The replay reconstructs all folded candidates directly from the literal
owner catalogue, checks all four face minima and the full common-screen
direct-sum identity for every `2<=d<=12`, and fails closed on any formula,
support, address, or upper-palette mismatch.
