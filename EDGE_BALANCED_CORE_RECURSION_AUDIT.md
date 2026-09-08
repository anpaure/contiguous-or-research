# Audit of `EDGE_BALANCED_CORE_RECURSION.md`

## 1. Proof-grade verdict

The note contains several correct and useful necessary conditions, but its
final recursive implication is not valid as written.

The following statements are correct.

* The edge encoding and Ferrers-box description are exact.
* The low fold is injective and misses exactly the new first-column edges.
* The occurrence count and one-top-row-hole inventory in the order-free
  lift are exact.
* Every valid edge-balanced core with `S>=4` repeats `P_1` or `E_(2,1)`.
* If `P_1` is unique, the nested barriers force every
  `D_1,...,D_(S-3)` to repeat.
* The support of the nonzero stars is a vertex cover of
  `1-2-...-S`.
* The parity corridor covers every strict height-one target, and its star
  support is minimum among supports that contain the compulsory `P_1`.
* The finite cores `V_3,V_4,V_5` and the completed `R=6` word agree with
  the stated inventories and pass independent interval enumeration.

Three corrections are essential.

1. The lean reset in Theorem 4 is an exact **multiset** identity, but it is
   not a viable recursive core profile.  Its output has unique `P_1` and
   repeats only `D_1`.  Theorem 5 therefore proves that no ordering of that
   output can be a valid core once its parameter is at least five.
2. The star-cover bound can be sharpened from `floor(S/2)` to
   `ceil(S/2)`, because `P_1` is compulsory.  Consequently the source's
   conclusion that `P_1` repeats for `S>=8` is correct but non-sharp: the
   same proof forces it already for `S>=7`.
3. The edge-braid lemma in Section 9 is not sufficient for induction.
   It asks to order the raw multiset from Theorem 2, although Theorem 3
   itself rules out that multiset after lifting any lean core with one
   loop.  It also transports only the strict lower targets, which covers
   upper targets with `u>=2,x>=2`; it leaves the upper family
   `u=1,x>=2` unaccounted for.

Thus the proved contribution is a sharp collection of multiset and ordering
obstructions, not an all-`S` edge-braid recurrence.  The conjectural bound

\[
                         \rho(R)\le R-1
\]

remains conditional.

## 2. Conventions and the exact portal ledger

Under

\[
 E_{s,y}\longleftrightarrow\{y,s\},\qquad 0\le y<s\le S,
\]

the nonpeak cells are the edges not incident with zero.  There are

\[
                         \binom S2
\]

such edges.  An edge-balanced core has length

\[
                         \binom{S+1}{2},
\]

contains every nonpeak except one top-row hole, and contains a terminal
loop.  The present distinct nonpeaks and that loop therefore occupy

\[
                         \left(\binom S2-1\right)+1
                         =\binom S2
\]

positions.  Exactly

\[
                         \binom{S+1}{2}-\binom S2=S                 \tag{2.1}
\]

positions remain.  Every nonzero-star occurrence, every extra nonpeak
occurrence, and every extra loop occurrence consumes one of these `S`
portal positions.

This is the precise ledger used in the duplication and barrier arguments.
It does not assume that the portal occurrences are all stars.

For an ordinary edge `e={a,b}`, `a<b`, an interval has box
`[u,r]x[0,x]` exactly when

\[
 \min h=u,\quad\max h=r,\quad\min\ell=0,\quad\max\ell=x.
\]

Staying inside the corresponding Ferrers set and attaining these four
extrema is therefore necessary and sufficient.  Section 1 of the source is
correct.

## 3. Exact audit of the low-fold image

The map is

\[
 \{0,a\}\mapsto\{0,a+1\},\qquad
 \{a,b\}\mapsto\{a+1,b+1\},
\]

with the old loop mapped to `{0,1}`.

It is injective, including at the loop: the old loop is the unique preimage
of `{0,1}`; old stars map to `{0,2},...,{0,S+1}`; and old nonstars map to
edges whose lower endpoint is at least two.  Hence the missing ordinary
edges in `K_(S+2)` are precisely

\[
                         \{1,j\},\qquad2\le j\le S+1.               \tag{3.1}
\]

There are `S` of them, exactly as in Lemma 1.

Suppose the old top-row hole is `{a,S}`, `1<=a<S`.  Its image is the
top-row hole `{a+1,S+1}`.  Adding the `S` edges in (3.1) supplies every
other new nonpeak.  Adding a new loop gives total occurrence count

\[
 \binom{S+1}{2}+S+1=\binom{S+2}{2}.                 \tag{3.2}
\]

Therefore Theorem 2's size, spanning inventory, and shifted-hole statement
are exact.

This is only an order-free inventory theorem.  It does not say that the
transported multiplicities admit a core ordering.  In fact, Section 4 of
this audit records a general obstruction to the raw transported multiset.

## 4. The low-portal duplication theorem

Theorem 3 is correct.  Here is the argument with the implicit interval step
made explicit.

The height-two suffix has box

\[
                         [0,3]\times[0,2].
\]

It must contain `E_(3,2)`, the unique cell attaining lower coordinate two
without exceeding high coordinate three.  Choose such an occurrence `q`.
Every high-`S` occurrence is before the start of this suffix, hence before
`q`, because `S>3`.

The height-one suffix must contain `E_(2,1)`.  Since it cannot contain `q`,
it starts after `q`, so it supplies an occurrence of `E_(2,1)` after `q`.

The target `[1,S]x[0,1]` requires a high-`S` occurrence and `P_1`.  If
`P_1` were unique and lay after `q`, every interval joining it to a
high-`S` occurrence would cross `q`, whose lower coordinate two
contaminates a height-one target.  Thus unique `P_1` lies before `q`.

The target `[1,2]x[0,1]` requires both `P_1` and `E_(2,1)`.  With unique
`P_1` before `q`, its witness cannot use the suffix occurrence of
`E_(2,1)` after `q`, again because it would cross `q`.  Hence a second
`E_(2,1)` occurs before `q`.

Consequently every valid core with `S>=4` repeats `P_1` or `E_(2,1)`.
The source's corollary that a star-complete exact-once multiset is
impossible is also correct.

The finite data is consistent with the theorem:

* the valid `V_4` has unique `P_1` and repeats `E_(2,1)`;
* the valid `V_5` repeats both;
* a star-complete `S=3` core exists, so the threshold `S>=4` is real.

## 5. The lean reset: correct algebra, impossible recursion

The lean profile consists of

* every nonpeak once except one hole;
* one extra `E_(2,1)`;
* `S-1` nonzero-star occurrences;
* one loop.

Its total size is

\[
 \left(\binom S2-1\right)+1+(S-1)+1
 =\binom{S+1}{2}.
\]

Under the low fold, the extra `E_(2,1)` becomes an extra `E_(3,2)`, the
old `S-1` star occurrences shift upward, and the old loop supplies one
`P_1`.  The new loop is then appended.  Removing the extra `E_(3,2)` and
adding an extra `E_(2,1)` restores the lean occurrence counts without
changing the hole or the total length.  Theorem 4 is therefore an exact
order-free multiset identity.

However, the output of this reset has:

\[
             P_1\text{ occurring exactly once},\qquad
             D_1=E_{2,1}\text{ the only repeated nonpeak}.         \tag{5.1}
\]

All old nonzero stars shift to labels at least two, so the old loop is the
only source of `P_1`.  The reset itself adds no star.

For output parameter `S' >= 5`, Theorem 5 requires both `D_1` and `D_2`
to repeat whenever `P_1` is unique.  Profile (5.1) repeats only `D_1`.
Therefore:

> **Corollary.** No ordering of the lean-reset output is a valid
> edge-balanced core for any output parameter `S'>=5`.

This is stronger than saying that an interval-preserving switch has not yet
been found: the proposed lean reset cannot be realized by any ordering in
that range.

The finite cores illustrate the break.  The reset of a lean `S=3`
multiset produces a possible `S=4` multiplicity profile, for which only
`D_1` is forced.  But the certified `V_5` is not the reset of `V_4`: it has
a second `P_1`, precisely escaping the unique-`P_1` hierarchy.

A more plausible order-free trade is to replace the shifted extra diagonal
by an extra `P_1`, rather than by an extra `E_(2,1)`.  This is the
21-letter candidate multiset isolated independently in
`R7_CERTIFICATE_STRUCTURE.md`.  It passes the obstructions audited here,
but no valid ordering of it is certified.

## 6. Nested barriers

Theorem 5 is correct for every

\[
                         1\le y\le S-3.
\]

Let `q` be an occurrence of

\[
                         D_{y+1}=E_{y+2,y+1}
\]

inside the height-`y+1` suffix.  Every high-`S` occurrence lies before the
start of that suffix because `S>y+2`, hence before `q`.

The target `[1,S]x[0,y]` cannot cross `q`, whose lower coordinate is
`y+1`.  If `P_1` is unique, it follows that `P_1` lies before `q`.

The target `[1,y+1]x[0,y]` requires `D_y`, the unique cell attaining lower
coordinate `y` while high coordinate is at most `y+1`.  Its witness also
cannot cross `q`; hence one `D_y` lies before `q`.

The height-`y` suffix contains a `D_y` but cannot contain `q`.  Since both
are literal suffixes ending at the same final position, the height-`y`
suffix starts after `q`.  It supplies a second `D_y` after `q`.

Thus unique `P_1` forces all `S-3` extra diagonal occurrences claimed in
the source.  The argument does not assume that the chosen suffix starts are
consecutive; contiguity and the common terminal endpoint are sufficient.

## 7. Star support and the sharpened threshold

For each `r=2,...,S`, the target

\[
                         [r-1,r]\times[0,1]
\]

requires a height-zero cell with high endpoint in `{r-1,r}`.  The loop
cannot be used because it would lower the first-coordinate minimum to zero.
Thus the set

\[
 A=\{j: P_j\text{ occurs}\}
\]

meets every edge of the path `1-2-...-S`.  Lemma 6 and its lower bound
`|A|>=floor(S/2)` are correct.

There is a free sharpening.  The target `[1,2]x[0,1]` forces `P_1`, so
`1 in A`.  A vertex cover of the path constrained to contain vertex one
has minimum size

\[
                         \left\lceil\frac S2\right\rceil.           \tag{7.1}
\]

For even `S`, take `{1,3,...,S-1}`.  For odd `S`, after selecting vertex
one the remaining path on vertices `2,...,S` needs `(S-1)/2` further
vertices, giving `(S+1)/2` total.

If `P_1` were unique, nested barriers consume at least `S-3` portal
positions on extra diagonals, while star support consumes at least
`ceil(S/2)` disjoint portal positions.  Hence

\[
                         S-3+\left\lceil\frac S2\right\rceil>S
\]

for every `S>=7`.  Therefore:

> Every edge-balanced core with `S>=7`, not merely `S>=8`, contains at
> least two occurrences of `P_1`.

The source's `S>=8` corollary remains true; it simply used the weaker
unconstrained path-cover bound.

## 8. Audit of the parity corridor

The proposed corridor scans `s=S,S-1,...,2`, emits `E_(s,1)`, emits `P_s`
when `s` is odd, and finally emits `P_1`.

Fix `1<=u<r<=S`.  Begin at `E_(r,1)`.  Every integer interval `[u,r]`
contains an odd integer.

* If an odd star is encountered above row `u`, continue through
  `E_(u,1)` and stop there.  The star supplies height zero; the first and
  last column edges supply high-coordinate extrema `r` and `u`.
* If the only useful odd label is `u`, continue through `P_u`.
* If `u=1`, continue to the terminal `P_1`.

All letters in the selected interval have high coordinate in `[u,r]` and
lower coordinate zero or one, and all four extrema are attained.  Every
strict height-one target is therefore covered.

The corridor uses every first-column edge exactly once and the odd star
labels

\[
                         1,3,5,\ldots,
\]

up to `S`, exactly `ceil(S/2)` stars.  By (7.1), this is minimum among star
supports that include the compulsory `P_1`.  Lemma 8 is correct.

This is a theorem about the standalone corridor.  Braiding its letters
through an inherited word can destroy corridor intervals by inserting
letters of lower coordinate greater than one.  The source correctly leaves
that continuity problem open.

## 9. Target transport under the low fold

If a lower interval has box

\[
                         [u,r]\times[0,x],\qquad x>=1,
\]

then its low-fold image has box

\[
                         [u+1,r+1]\times[0,x+1].                     \tag{9.1}
\]

A lower star supplies lower coordinate zero after folding, and a lower
nonstar attaining coordinate `x` maps to coordinate `x+1`.  The conditional
transport statement in Section 5 is exact.

The subsequent universal wording is too broad for a completion core.  A
completion core is only required to contain lower strict witnesses with
`u>=1`.  Transporting those witnesses covers upper strict targets

\[
                         u>=2,\qquad x>=2.             \tag{9.2}
\]

It does not cover the upper family

\[
                         u=1,\qquad x>=2.              \tag{9.3}
\]

The preimages of (9.3) are lower positive-height targets with `u=0`, which
are not core requirements.  This is not a merely hypothetical distinction:
the certified `V_5` misses exactly

\[
 (0,4,1),\quad(0,5,1),\quad(0,5,2)
\]

among its lower positive-height targets while covering every strict one.

The perfect suffix fan gives only the minimal-reach boundary boxes
`[0,x+1]x[0,x]`; by itself it does not provide every larger right endpoint
needed in (9.3).  A valid recurrence must therefore add one of the
following explicit conditions:

1. the lower word covers all positive-height boundary targets as well as
   the strict ones; or
2. the upper braid separately constructs every target in (9.3).

## 10. Finite-certificate audit

The existing lightweight checker
`scratch/test_triangular_patterns.cpp` was compiled and run independently.
It reports

```text
V3 strict-positive miss=0
V4 strict-positive miss=0
V5 strict-positive miss=0
```

and for `V_5` it reports the three `u=0` omissions listed in Section 9.
Direct inventories agree with the source and the prior audit:

* `V_3` has length six, hole `E_(3,1)`, and repeats `E_(2,1)`;
* `V_4` has length ten, hole `E_(4,1)`, and repeats `E_(2,1)`;
* `V_5` has length fifteen, hole `E_(5,2)`, repeats `E_(2,1)`, and has
  two occurrences of `P_1`.

Their displayed diagonal suffixes attain exactly the required boxes.  The
completed word `scratch/triangular_r6_plus5.txt` has 27 cells, spans all 22
letters of `T_6`, and its exhaustive certificate records all 91 targets.
This proves only `rho(6)<=5`, as stated in the audited braid note.

The later file `R7_CERTIFICATE_STRUCTURE.md` supplies a valid
`S=6` completion core of length 24 and excess nine.  It is not an
edge-balanced core, whose target length would be 21.  Its exact decomposition

\[
 \text{raw order-free lift of }V_5+P_1+P_4+P_5
\]

is consistent with Theorems 2 and 3: the raw 21-letter lift has unique
`P_1` and unique `E_(2,1)`, so no ordering of that raw multiset can work;
the valid 24-letter core adds the needed portal freedom.

Thus the source's finite edge-balanced base range `S=3,4,5` is correct.
The `R=7` certificate is evidence for a linear-overhead braid, not a new
edge-balanced base.

## 11. Why the Section 9 edge-braid lemma does not induct

The stated lemma starts from “the multiset from Theorem 2.”  For a lean
lower core with one loop, that raw multiset has:

* exactly one `P_1`, supplied by the folded old loop;
* exactly one `E_(2,1)`, supplied by the new first column; and
* its transported extra nonpeak at `E_(3,2)`.

Theorem 3 proves that **no ordering** of this raw multiset is a valid core.
Therefore the claimed lemma cannot hold for the very base-and-lift sequence
to which it is meant to apply.  A multiplicity trade must be part of the
recursive statement.

The lean trade in Theorem 4 does not fix the recursion beyond parameter
four, by Section 5 of this audit.  A second-`P_1` trade is compatible with
the proved necessary conditions, but remains conjectural at the ordering
level.

Even after correcting the multiset, the three bullets in Section 9 cover
only:

* transported strict targets with `u>=2,x>=2`;
* newly constructed height-one targets; and
* the terminal suffix fan.

They do not include the upper strict family `u=1,x>=2` identified in
Section 9 of this audit.  Hence the assertion that the lemma “immediately
inducts” is unsupported for two independent reasons.

## 12. A corrected sufficient recurrence

A proof-grade edge-braid theorem sufficient for the desired conclusion
would need the following form.

Given an edge-balanced core `V_S`, construct an edge-balanced multiset on
the upper alphabet, not necessarily the raw multiset of Theorem 2, such
that:

1. it contains every upper nonpeak except one top-row hole and has exactly
   one terminal loop;
2. its multiplicities satisfy the low-portal and nested-barrier necessities,
   in particular carrying a second `P_1` from `S>=7` onward;
3. it can be ordered so every transported lower strict witness survives;
4. the ordering separately covers every `u=1,x>=2` strict target;
5. it covers every strict height-one target; and
6. it ends in a diagonal-normalized perfect suffix fan.

The exact occurrence ledger would then make the ordered word an
edge-balanced `(S+2)`-completion core.  Induction from any certified base
would prove

\[
                         \rho(R)\le R-1.
\]

No such theorem is currently proved.  Walecki decompositions, terraces,
Skolem schedules, and parity rotations remain candidate ordering devices;
none automatically preserves the linearly ordered Ferrers intervals in
conditions 3--5.

## 13. Safe statement for the handoff

The defensible mathematical result is:

> The low fold has an exact no-waste occurrence ledger and transports each
> individual positive-height witness.  Valid edge-balanced cores obey a
> low-portal duplication theorem, a nested diagonal-barrier hierarchy, and
> a star-support vertex-cover bound.  The parity corridor optimally solves
> the standalone height-one layer.  These statements sharply constrain an
> eventual edge braid.

The open statement is:

> Choose a recursively admissible portal multiset—necessarily different
> from both the raw lean lift and, from parameter five onward, the lean
> reset—and order it so that transported strict witnesses, the missing
> `u=1` family, the height-one corridor, and the terminal fan coexist.

Accordingly, `EDGE_BALANCED_CORE_RECURSION.md` materially advances the
obstruction theory, but its Section 9 recurrence and the resulting
`rho(R)<=R-1` bound remain conjectural and require the two corrections above.
