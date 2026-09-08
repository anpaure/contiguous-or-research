# The singleton `T2` clock closes the entire immediate-upper row; its remaining ungraded current is `2h-1`, and local reflection needs a residence halo

**Date:** 2026-08-13  
**Status:** unconditional symbolic theorem for the immediate-upper row and
exact H100 classification of the natural wider current through `h=12`.
The displayed `2h-1` residual and reflection formulas are symbolic in
`h`.  This theorem does not claim that the wider residual is globally
absorbed.

## 1. Construction and tag quotient

Work on the complete rank-seven upper-owner cycles of the frozen `T2`
relay.  Put

```text
a = 1010110011010,
b = 1011100011010, c = 1011110001010,
d = 1010011011010, e = 1000111011010.
```

The old neighbours of `a` are `d,b`, and the new neighbours are `c,e`.
Replace `a` by the singleton owner

\[
                         C+V_a+p_0+D_0.             \tag{1.1}
\]

Every other owner `v` is replaced by the forward doubled block

\[
\begin{aligned}
 (&C+V_v+p_{t(v)}+D_0,\ldots,C+V_v+p_{t(v)}+D_h,\\
  &C+V_v+p_{t^+(v)}+D_h,\ldots,
                    C+V_v+p_{t^+(v)}+D_{2h}),       \tag{1.2}
\end{aligned}
\]

where `D_(2h)=D_0`.  Impose the common-successor relations on every normal
tail and

\[
                         t(a)=t(b)=t(e)=0.           \tag{1.3}
\]

The equality quotient has `1711` classes, with size histogram

```text
1710 classes of size 1; one class of size 6,
```

and no required tag-change loop.  Its conflict graph has `1710` vertices
of degree two and the exceptional class of degree ten.  A deterministic
DSATUR replay gives a proper three-colouring with tag loads

```text
793, 792, 131.
```

Writing the `1716` lines as `owner-word tag` in increasing integer owner
order, the exact colouring certificate has SHA-256

```text
5246abd53f4573c2cbd7534434590f3fb41326da2debb2a3b6764ce0db0ea2a4.
```

The six-element class is

```text
1010110101010, 1011100011010, 1010110011010,
1000111011010, 1010010111010, 1100100011110.
```

The graph legality and positive residence then follow from
`MATH_THEOREM_ONE_SINGLETON_EXCEPTION_POSITIVE_RESIDENT_CLOCK_AND_WEIGHTED_SUPPORT_20260813.md`.

## 2. One forced untouched backup

Let

```text
Z = 1000111011110.
```

The old base factor has exactly the two seams

```text
1000110011110 -> 1000111011010,
1000111011100 -> 0000111011110,
```

with union `Z`.  The first seam is deleted by `T2`; the second is literal
in both states.  Add the legal tag equality

\[
                         t(0000111011110)=0.          \tag{2.1}
\]

The head in `(2.1)` is a singleton quotient class and is not adjacent in
the conflict graph to the exceptional six-element class.  Hence the same
three-colour construction remains proper.

### Theorem 2.1 (all-height immediate-upper closure)

For every `h>=2`, the construction `(1.1)--(2.1)` is a literal Johnson
two-factor, is positively `h`-resident, retains the named new `T0,B,C`
seams, and loses no old immediate-upper value.

### Proof

Every normal join has the same old/new endpoint payload and performs only
the base Johnson exchange.  The singleton neighbour condition is literal:
the old neighbours omit distinct `a`-coordinates `4,5`, and the new
neighbours omit `8,2`.  Thus every base positive run through `a` extends
into a normal block.  Normal tag and clock runs have length at least `h`,
and a run through the singleton concatenates an old terminal run, the
singleton, and a new initial run.  This proves positive residence.

At a base seam `v->w`, the two block-boundary owners have auxiliary union

\[
                         \{p_{t(w)}\}\cup D_0.       \tag{2.2}
\]

The finite changed-seam ledger with the forced colouring has support

\[
                         1285\subseteq1287           \tag{2.3}
\]

for the signatures `(V_v union V_w,t(w))`, with loss zero and birth two.
The only base seam union whose changed occurrence needed a second witness
is `Z`; equation `(2.1)` makes the untouched seam carry exactly the lost
payload `{p_0} union D_0`.  The singleton boundaries give both `B,C` the
same payload in the old and new states, and the new `T0` seam also carries
`{p_0} union D_0`.  These facts are independent of `h`, proving the
immediate-upper assertion for every height.  `square`

Owner and immediate-lower tickets are simple in the exact replay.
Immediate-upper ticket multiplicity is at most three; upper support, not
upper-ticket simplicity, is the assertion of Theorem 2.1.

## 3. Graded residual census

When physical width is retained, the baseline unforced colouring has loss

\[
                  {h^2+45h+24\over2}.              \tag{3.1}
\]

Forcing the untouched `Z` backup reduces this exactly to

\[
                         \boxed{21h+11}.            \tag{3.2}
\]

The H100 values for `h=2,...,12` are

```text
53, 74, 95, 116, 137, 158, 179, 200, 221, 242, 263.
```

The base-span (equivalently base-rank) rows are

\[
\begin{array}{c|ccccc}
\text{base span}&2&3&4&5&6\\ \hline
\text{base rank}&8&9&10&11&12\\
\text{loss}&3h-1&4h+3&3h+2&6h+4&5h+3.
\end{array}                                        \tag{3.3}
\]

The total literal target rank is the lifted owner rank plus the excess in
the following exact pattern:

* for each excess `j=2,...,h`, two casualties;
* no casualty at excess `1`;
* four terminal high-rank groups whose counts are the last four entries in
  the complete H100 table.

In particular every residual casualty has target rank at least `R+2`.
The immediate-upper row `R+1` is closed, not merely small.

The residual decomposes more sharply into twelve base-value families.
Exactly `2(h-1)` are the nested singleton-side masks:

```text
B = 1011110011010: h-1 prefix masks;
C = 1010111011010: h-1 reflected prefix masks.
```

The other `19h+13` carry tag union `{p_0,p_1}` and full clock union.  Their
base values and counts are affine in `h`:

\[
\begin{array}{c|c|c}
\text{base value}&\text{span}&\text{count}\\ \hline
1000111011110&2&h+1\\
1000111011111&3&3h+2\\
1000111111110&3&h+1\\
1011111011110&4&2h+1\\
1111101011110&4&h+1\\
1011111111110&5&3h+2\\
1011111011111&5&2h+1\\
1111101111110&5&h+1\\
1111111111110&6&3h+2\\
1011111111111&6&2h+1.
\end{array}                                        \tag{3.4}
\]

Equations `(3.2)--(3.4)` follow by writing the two doubled clock arcs as
the forward lists `D_0,...,D_h` and `D_h,...,D_(2h)` and enumerating the
possible clipped endpoint offsets.  Each displayed family is a single
interval of offsets, so the counts are respectively `h+1`, `2h+1`, or
`3h+2`; the singleton-side families admit offsets `1,...,h-1`.  The H100
replay checks every literal mask and endpoint type through height twelve.

## 4. Reflection nearly closes ungraded support, but breaks residence

Forget physical width and compare literal union support only.  With no
clock reflection, the forced-backup singleton clock has exactly

\[
                         \boxed{2h-1}               \tag{4.1}
\]

ungraded losses:

* the `h-1` nested `B` masks;
* the `h-1` nested `C` masks; and
* the one saturated value
  `1000111011111 + {p_0,p_1} + U_clock`.

Reflecting clock coordinates in blocks `c,d` (mask `6` in the order
`b,c,d,e`) maps the two nested families into one another and leaves only
the saturated value.  The same one-loss result holds for masks
`5,9,10`.  Exact H100 values at `h=2,3,4` are all `1`.

This is not yet a positive construction.  At a boundary between a
reflected and an unreflected normal block, `D_0` is fixed but the two
adjacent clock arcs leave a positive and a zero run of length exactly two.
Thus every nontrivial local reflection mask has

\[
                         \min r_+=\min r_0=2,         \tag{4.2}
\]

which violates height-`h` residence for `h>2`.

Reflecting all `64` normal blocks in the affected 65-owner union
component, every block outside that component, or all `1715` normal
blocks preserves residence, but is a global clock relabelling.  It leaves
the ungraded loss `2h-1` unchanged.  Therefore support cancellation
requires a genuine reflection discontinuity, while residence requires an
`h`-long transition halo at each such cut.  Two halos plus one saturated
backup are the exact remaining local design target.

## 5. Reproducibility

Main verifier:

```text
scratch/audit_msw_t2_singleton_a_clock.py
```

Checkpoint SHA-256 used for the forced-backup artifact:

```text
7375c6ec9103f97a96a25d4d910b3c2defbd2a05f17e506da85423778c4558a0
```

The current verifier, which adds complete loss records and reflection
hooks without changing the construction, has SHA-256

```text
ea93051a8c304e6505b75c28d9605b22441673225b91d0345d190135e1fafd98
```

Forced-backup H100 artifact:

```text
scratch/audit_msw_t2_singleton_a_clock_backup_20260813.h100.out
```

SHA-256:

```text
add2206c200577ed812a34f60f922893b2f2acf35c6f450e628802bf6a859b89
```

Reflection verifier:

```text
scratch/search_msw_t2_singleton_clock_reflections.py
```

SHA-256:

```text
33833c85158d0d0f7b57948f7bf8ed1f99866c988275b0b66e24b93d60da3af4
```

The exact baseline, rank-refined, origin-MILP, and colouring-bank artifacts
are recorded in
`MATH_THEOREM_COMPLETE_ML13_T2_CYCLIC_SUPPORT_AND_RESIDENT_LIFT_GATES_20260813.md`.

All exhaustive runs were executed on `h100`; local work was limited to
proof inspection, patching, and hashing.

## 6. Exact conclusion

\[
 \boxed{\text{literal factor + positive residence + complete immediate
 upper support: PASS for every }h\ge2.}              \tag{6.1}
\]

Full all-width support is not yet proved.  Its exact natural-clock residual
is linear in `h`; ungraded reflection reduces it to one value but creates
a sharp run-two boundary defect.  This isolates a substantially smaller
prepared-prism problem than the original full relay: two resident
reflection halos and one saturated wider backup.
