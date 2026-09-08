# Independent audit and classification of the append-`0x0200` radius-three census

## 1. Verdict

**PASS, with the scope in Section 7.**  The pinned source is the length-12,874
word

`scratch/k16_append0200_12874_onehole.word`

of SHA-256

`aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18`.

Its exact missing set is the singleton

\[
\{0x287d\}=\{10365\}.
\]

The audited radius-three artifact is

`scratch/k16_append0200_radius3_exact_20260730.audit.json`

of SHA-256

`f9ac9f328b099b3e61be0395c7de77bf697aa6ef5099b487a5871e9ee9ada61a`.

It contains 16 first portal states, exactly 65 collateral-two second states per
portal, hence 1,040 third-stage source states.  It reports no safe third move,
global minimum remaining debt one, and exactly 133,120 global-minimum third
moves.

The decisive additional classification is now independently checked:

> Every one of those 133,120 global-minimum moves changes the same endpoint
> changed by the second move and reopens exactly `0xa879` (43129).

Thus the minimum tier contains no genuine defect-closing transport.  It is a
same-site return to the old one-hole fibre.

## 2. Exact first portal family

Use zero-based position

\[
p=6440,
\]

whose source value is `0xa069`.  The 16 certified first values are

\[
0x2004\lor q,\qquad q\subseteq 0x0069.
\]

Literal replay of every resulting word gives the same exact missing set

\[
\{H\},\qquad H=0xa879=43129.
\]

This replay uses the raw word, not the summaries in the radius-three JSON.

## 3. Exact 65-state second tier

For each of the 16 portal values, the artifact's complete collateral-two tier
equals its 65 listed minimum off-portal rows.  The equality is forced by the
two recorded counts: `collateral_two_row_count = 65`, while the displayed
minimum-off-portal list also has length 65 and its minimum debt is two.

The rows have the following common normal form, independent of the first
portal value.

### 3.1 Left-end family

There are 64 rows at position zero.  The source value there is `0x882c`, and
the service values are exactly

\[
y=0x8010\lor q,\qquad q\subseteq 0x2869.
\]

Each installs `0xa879` and leaves exactly

\[
D_L=\{0xa86d,0xac6d\}=\{43117,44141\}.
\]

### 3.2 Right-end row

There is one row at position 12,873.  It replaces the appended `0x0200` by
`0xa879` and leaves exactly

\[
D_R=\{0xce61,0xce63\}=\{52833,52835\}.
\]

The independent checker replays all

\[
16(64+1)=1040
\]

second states by exact contiguous-OR multiplicity deltas.  Every replayed
missing set equals the debt pair written in the artifact.

## 4. The 128-row same-site restoration halfcubes

Fix a first portal state `U`, with sole hole `H=0xa879`, and one of its 65
second rows.  The third-stage kernel tests replacements that install both
current debts; hence its replacement letter is a nonzero submask of the
intersection of those debts.

The checker independently enumerates only those 255 possible submasks at the
second move's own endpoint and computes the resulting missing set from exact
interval multiplicities.

For a left-end second row, the replacements leaving exactly the singleton
hole `H` are precisely

\[
z=0x8000\lor q,\qquad q\subseteq 0x286d.
\]

There are 128 such values.  For the right-end second row they are precisely

\[
z=0x0200\lor q,\qquad q\subseteq 0xcc61,
\]

again 128 values.  None is the corresponding service value, and every final
word has exact missing set

\[
\{0xa879\}.
\]

The word *backtrack* here means a return to the same one-hole fibre at the
same physical site.  Most rows do not literally restore the site's original
letter; the exact inverse is only one member of its 128-element halfcube.

## 5. Saturation proves the classification

There are 16 first portal choices, 65 collateral-two second rows for each,
and 128 same-site one-debt returns from every second state.  Therefore the
independently constructed class has cardinality

\[
16\cdot65\cdot128=133120.
\]

These are distinct third-move rows in their respective labelled first/second
states.  The pinned exhaustive artifact reports:

* global minimum third debt `1`;
* safe third-row count `0`;
* total global-minimum third-row count `133120`;
* all 1,040 state minima equal to `1`.

Our same-site class already attains the entire reported global-minimum count.
Consequently every global minimum counted by the artifact belongs to this
class.  In particular, no off-site minimum can coexist with it.  All 32
minimum examples retained in the artifact were also checked directly: their
third position equals their second position and their sole debt is `0xa879`.

This count-saturation step is the independent adversarial check missing from
an inspection of the 32 examples alone.

## 6. Reproducer and hashes

The lightweight fail-closed checker is

`scratch/audit_r_k16_append0200_radius3_same_site_classification_20260730.py`

with SHA-256

`afe4a03954f05678cfc15416344ba43e45d37ead90f0b48cfb7c29f560b85727`.

Its audit output is

`scratch/k16_append0200_radius3_same_site_classification_20260730.audit.json`

with SHA-256

`ad6aba6f36a6a8b6ac8bd8467f2a7d1285801b21953badc5bb73de6895d1d9f5`.

The output payload hash is

`7b0785ce4bf104074e4be56e1a2c5cc73ef6ad1021ff8566f6b6b7d36f9c85e0`.

The checker recomputes all contiguous-OR multiplicities by the exact ending-
suffix recurrence, replays all explicit first and second states, derives both
128-element restoration families, and checks the saturation identity against
the pinned radius-three artifact.

## 7. Exact scope and remaining boundary

This is a scoped negative theorem for the route

1. one of the 16 sharp first substitutions at `p=6440`;
2. one of the complete 65-row collateral-two second tiers;
3. one arbitrary one-cell third substitution that installs both current
   debts.

It does **not** exclude:

* a second move with three or more collateral debts;
* a first move outside the 16 sharp portals;
* a simultaneous block replacement or a nonlocal compound not factored
  through one of these 1,040 states;
* a different length-12,874 basin.

The checker does not rerun the expensive all-position third census.  It pins
that census byte-for-byte and independently verifies all of its explicit
state data plus a class whose size saturates its reported minimum total.
Accordingly, the claim is exact conditional only on the pinned artifact's
already certified exhaustive total, and it makes no broader radius-three
no-go assertion.
