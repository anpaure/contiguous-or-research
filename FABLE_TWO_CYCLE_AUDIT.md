# Independent audit of Fable Section 11: Proposition Q, Lemma R, and Theorem P

## 1. Verdict

* **Proposition Q is correct** for the section's explicit notion of literal
  adjacency `l'=r+1`.
* **Lemma R is false as written at equality seams.**  A rise-to-fall seam
  with equal `z` values creates a two-position maximal `z`-plateau of cost
  one.  It does not create “no new run.”  The lemma is repairable by replacing
  “cost-zero” with “cost at most one” and treating this equality case as a
  separator.
* **Theorem P is not proved as stated.**  Its proof uses a fixed lower bound
  `lambda>=ca+1` on every plateau, but the theorem statement assumes no such
  threshold.  Without it, the number of seams inside one `4a+2` edge-mass
  block can be `Theta(a)`, so the claimed `L+O(1)` service spacing does not
  follow.
* The intended theorem **can be repaired** if “one chain” is read literally:
  for a fixed `c>0`, one contiguous chain of mutually adjacent directed peak
  plateaux, all longer than `ca` and covering all but `o(a^2)` word positions,
  is incompatible with `D=o(a^2)`.  Equality seams cost one rather than zero,
  which is still negligible in the capped-sum argument.  Merely assuming
  `o(a^2)` total positions in interspersed gaps is not enough for the written
  service argument; every such gap can reset the `z` trend.

Consequently Section 11 has identified a useful cheap-seam mechanism, but the
ledger should not mark Lemma R or Theorem P proved in their displayed forms.
The broad sentence that the scalar profile `2 delta_(3/2)` has no two-letter
realization also needs the missing reduction from a profile realization to
the corrected long-plateau chain hypotheses.

## 2. Proposition Q

Let `P=[l,r]` be an internal peak plateau of coordinate `x` at level `t`, and
let `P'=[r+1,s]` be another internal peak plateau of `x` at level `t'`.
Because `P` is a peak, its right neighbor (the first point of `P'`) satisfies

\[
                              t'<t.
\]

Because `P'` is a peak, its left neighbor (the last point of `P`) satisfies

\[
                              t<t'.
\]

This is impossible.  If `t=t'`, maximality would already merge the two
constant blocks.  Thus Proposition Q is correct.

Scope qualification: Section 11 defines adjacency as disjoint literal
adjacency `l'=r+1`.  Different-coordinate peak plateaux may instead share one
endpoint (`l'=r`) under the vertex-union convention used elsewhere.  Such a
shared seam is not covered by Proposition Q's wording, although same-coordinate
plateaux cannot share an endpoint without merging.

## 3. Exact seam taxonomy for Lemma R

Inside every directed `x`- or `y`-plateau, the complementary coordinate `z`
is strictly monotone.  At a seam write

\[
 p=z_-\quad\text{(last value of the left plateau)},
 \qquad q=z_+\quad\text{(first value of the right plateau)}.
\]

Denote the incoming and outgoing strict trends by `+` (rising) or `-`
(falling).  The exact upper-threshold taxonomy is:

| incoming | outgoing | condition | seam behavior |
|---|---|---|---|
| `+` | `+` | `q<p` | singleton peak at `p`, cost 0 |
| `+` | `+` | `q>=p` | no seam peak |
| `-` | `-` | `q>p` | singleton peak at `q`, cost 0 |
| `-` | `-` | `q<=p` | no seam peak |
| `+` | `-` | `q<p` | singleton peak at `p`, cost 0 |
| `+` | `-` | `q>p` | singleton peak at `q`, cost 0 |
| `+` | `-` | `q=p` | **two-position peak plateau, cost 1** |
| `-` | `+` | any `p,q` | a valley seam; no forced upper peak |

The two strict cases highlighted in the notebook are correct.  The equality
sentence is not: equality is harmless for equal trends and for a
fall-to-rise valley, but not for a rise-to-fall reversal.

### 3.1 Concrete equality counterexample

For `a>=1`, the following consecutive points lie in `H_a`:

```text
(0, 0, 0), (1, 0,-1), (1,-1, 0),
(-1,1, 0), (0, 1,-1), (-1,0, 1).
```

The middle two points of the `x=1` plateau have `z=-1,0`; the following
two points of the `y=1` plateau have `z=0,-1`.  Both coordinate plateaux are
directed internal peaks: their outside `x` or `y` values are strictly below
one.  Across their seam the `z` word is

```text
                         -1, 0, 0, -1.
```

Hence the two equal seam points form a maximal internal threshold run of
`{z>=0}` with one ordering edge—cost one.  This directly falsifies the
claim that equality creates no run.

### 3.2 Corrected monotone-stretch lemma

On a stretch containing no seam peak of cost at most one:

1. a `+ -> -` transition cannot occur;
2. consecutive rising plateaux join with `q>=p`;
3. consecutive falling plateaux join with `q<=p`; and
4. at most one `- -> +` valley transition can occur.

Thus `z` weakly falls and then weakly rises, while every plateau edge is a
strict integer change in `z`.  Since `-a<=z<=a`, the total number of plateau
edges is at most `2a+2a=4a`; the notebook's `4a+2` is a safe relaxed bound.

It follows that a two-letter segment of plateau-edge mass `T` contains at
least

\[
              \left\lceil{T\over4a+2}\right\rceil-1
\]

distinct seam peaks of cost at most one.  The notebook's weaker floor bound
is also safe after replacing “cost zero” by “cost at most one.”

Without the equality correction, arbitrarily many rise-to-fall resets at
equal seam height are not counted, so the claimed `4a+2` decomposition does
not follow from the lemma as written.

## 4. Hidden length hypothesis in Theorem P

The proof writes, for each valley block,

\[
 m_k\le {4a+2\over ca+1}=O_c(1),                  \tag{4.1}
\]

where `m_k` is the number of plateaux in that block.  Equation (4.1) uses

\[
                         \lambda(P)>ca             \tag{4.2}

for every plateau.  Neither (4.2) nor any fixed `c>0` appears in Theorem P's
statement.

This is not cosmetic.  A block with at most `L=4a+2` plateau edges occupies

\[
       \text{plateau-edge mass} + \text{number of plateaux}
\]

word positions when the plateaux are disjoint and literally adjacent.  Under
(4.2), it has at most `L+O_c(1)` positions.  Without (4.2), it may contain
`Theta(a)` short plateaux and have as many as `2L` positions.  Windows have
only `L` positions, so the asserted almost-complete service coverage by block
boundary peaks no longer follows.

Remark 11.3(i) itself acknowledges the assumption—“the proof did not use
plateau lengths beyond `>=ca+1`”—but that is precisely a hypothesis the
theorem omitted.

Theorem K does not fill this gap: it guarantees many long plateaux, not that
every plateau in an almost-spanning two-letter chain is long.

## 5. Exceptional positions and window coverage

The prose

> block length `<=L+O(1)+o` implies a `1-o(1)` fraction of windows contains
> a boundary peak

needs a summed interval argument.  Pointwise `o` notation for each block is
not sufficient when there are `Theta(a)` blocks.

Here is the correct bookkeeping under the literal one-chain interpretation.
Assume:

* every plateau has more than `ca` edges for one fixed `c>0`;
* one contiguous interval is tiled by mutually adjacent plateaux; and
* the prefix and suffix outside that interval have total size `E=o(a^2)`.

There are only `O_c(a)` plateaux and hence only `O_c(a)` valley blocks.  The
corrected Lemma R and (4.1) give a separation between successive cheap runs

\[
                         d_k\le L+O_c(1).           \tag{5.1}
\]

A cost-zero singleton peak is contained in `L` forward windows; a cost-one
two-position peak is contained in `L-1`.  Therefore the uncovered interval of
window starts between two consecutive service intervals has size at most

\[
                         O_c(1).                    \tag{5.2}
\]

Summing (5.2), and adding prefix and suffix losses, gives

\[
                         O_c(a)+E=o(a^2).           \tag{5.3}

This proves the needed `1-o(1)` coverage under the literal statement.

If exceptions are interspersed as internal gaps, total gap mass alone does
**not** prove (5.3).  A gap can reset the `z` direction without producing a
cheap seam.  The distance from the last cheap run before a gap to the first
one after it can be as large as

\[
                         2L+O_c(1)+G_k,
\]

leaving `L+O_c(1)+G_k` uncovered starts.  As few as `Theta(a)` isolated
one-position gaps—only `O(a)=o(a^2)` exceptional positions—can therefore
leave `Theta(a^2)` starts uncovered.  A gap-tolerant extension needs, for
example, `o(a)` internal gaps, a cheap run attached to almost every gap, or a
new cross-gap trend ledger.  The notebook's unquantified “gap share” does not
supply this.

## 6. Corrected service contradiction

Under the strengthened hypotheses, assign every forward start whose
`L`-window contains a cheap seam peak that peak.  Each selected run:

* is internal and avoids the assigned start;
* has cost at most one;
* has one-sided span at most `L+1=4a+3`; and
* contributes endpoint congestion at most `L+1`, because all assignments
  point forward.

By (5.3), only `o(a^2)` forward starts remain.  Assign each of those the
universal internal peak supplied in its `L`-window, whose cost is at most
`2a`.  Leave the final `L=O(a)` indices unassigned, as allowed by the subset
form of Theorem I (or count them at cap `h`, contributing only `O(a^2)`).

At `h=3a-1`, the resulting capped cost is

\[
 1\cdot(3a^2+O(a)) + 2a\cdot o(a^2)+O(a^2)
                         =o(a^3).                   \tag{6.1}
\]

The notebook writes zero for the first term; equality seams change it to at
most `O(a^2)`, which is still negligible.  Theorem I with `D=o(a^2)` requires
at least `4a^3-o(a^3)`, a contradiction.

Thus the following corrected theorem is proved by the intended method:

> **Corrected pure two-cycle theorem.**  Fix `c>0`.  No order with
> `D=o(a^2)` can contain one contiguous interval, covering all but `o(a^2)`
> word positions, tiled by mutually adjacent directed internal peak plateaux
> alternating between two fixed coordinates, if every plateau has cost
> greater than `ca`.

## 7. Does the `2 delta_(3/2)` conclusion follow?

Not directly from Theorem P as presently stated and proved.

An actual realization of the atom profile `2 delta_(3/2)` would supply the
missing fixed lower length bound after discarding a lower-order exceptional
family: choose any fixed `c<3/2`.  Edge saturation `sigma->3` also forces
the total nonplateau vertex/gap mass to be `o(a^2)` through the audited gap
identity.  If one additionally assumes that all these long plateaux use only
two coordinates and tile one contiguous word interval, then the corrected
theorem excludes it.

However, a scalar profile by itself does not specify:

* that its plateaux form one literal-adjacency chain;
* how shared-endpoint seams are linearized;
* that all other peak plateaux or exceptional positions can be discarded
  without changing the two-letter structure; or
* the required word-order transition pattern.

Those reductions must be stated and proved before claiming that the profile
has “NO two-letter realization.”  The corrected theorem kills the clean
long, dense two-letter realization, which is still a meaningful result.

## 8. Remaining scope issues

1. **Shared endpoints.**  Lemma R is written for disjoint adjacent plateaux
   (`l'=r+1`).  Different-coordinate plateaux may share one endpoint under
   the global plateau convention.  At a shared endpoint, a rise-to-fall
   equality produces a cost-zero singleton rather than the two-position
   cost-one plateau, so a similar argument should work, but it is not written.
2. **Small gaps.**  The corrected interval-service proof does not tolerate
   `Theta(a)` independent trend-resetting gaps merely because their total mass
   is `o(a^2)`.  A separate cross-gap lemma or an `o(a)` gap-count hypothesis
   is required.
3. **Nondirected plateaux.**  Each has an internal cost-zero cross-coordinate
   peak, but inserting many of them changes the segment decomposition.  The
   claimed robustness is valid only after their positions and service gaps
   are included in the same summed exceptional ledger.
4. **Earlier scalar correction.**  The independent Theorem O audit shows that
   `2 delta_(3/2)` is not the unique scalar survivor; even a fully repaired
   Theorem P would not reduce the whole scalar problem to aperiodic saturated
   patterns.

## 9. Final theorem ledger

### Proved as written

* Proposition Q for disjoint literal adjacency.

### False as written but repairable

* Lemma R's equality claim and its “cost-zero” consequence.  Replace them by
  the exact taxonomy in Section 3 and “cost at most one.”

### Not proved as stated

* Theorem P without a fixed lower plateau length.
* The unqualified claim that `2 delta_(3/2)` has no two-letter realization.
* Robustness to nondirected plateaux without explicit exceptional-gap
  bookkeeping.

### Proved after adding the missing hypotheses

* The corrected pure two-cycle theorem in Section 6 for one contiguous
  literal-adjacency chain, including equality seams and boundary exceptions.
