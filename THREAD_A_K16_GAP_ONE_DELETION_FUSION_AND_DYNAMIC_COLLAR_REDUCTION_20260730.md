# K16 gap one: deletion, fusion, and the exact dynamic-collar reduction

Date: 2026-07-30

Status: authenticated upper certificate; exact pure-deletion, arbitrary
adjacent two-to-one fusion, and best-deletion radius-one no-gos; exact
three-profile fixed-gap reduction.  No length-12,873 word is claimed.

## 1. Frozen headline and lineage

Let

```text
U = answers/k16_upper12874.word
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
```

Then `|U|=12874`.  Independent suffix-state replay covers all `65535`
nonzero masks, with at most eleven distinct ending-OR states at any endpoint.
Consequently

\[
                         12873\le \nu(16)\le12874.        \tag{1.1}
\]

The lower bound is the monotone-deadline bound `W+d=12870+3`.

The word is the decoded solution of the exact `(5,9,4)` collar model over

\[
[0,5),\qquad[6436,6445),\qquad[12870,12874).             \tag{1.2}
\]

Relative to

```text
scratch/k16_append0200_12874_onehole.word
SHA-256 aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18
```

the frozen word changes exactly twelve, not fourteen, cells:

\[
0,1,3,4,6436,6438,6439,6440,6442,12871,12872,12873.     \tag{1.3}
\]

The four positions exposed beyond the old `(4,7,3)` atlas are

\[
                 \{4,6436,6444,12870\};                 \tag{1.4}
\]

only `4` and `6436` actually change.  Thus “four newly exposed positions”
is correct, while “fourteen of eighteen changed” is not correct relative to
the authenticated append-`0200` source.  The independent certificate audit
is

```text
scratch/ad_k16_upper12874_phase_collar_independent_20260730.audit.json
SHA-256 dc800a738a0c771a50c01dd9b8cfb39df6e3b4e25769f713814d0926b5b458ea
```

## 2. Exact deletion identity

For a word `w=(x_0,...,x_(n-1))` of nonzero letters, let `c_w(T)` be the
number of intervals whose OR is `T`.  At position `p`, define

\[
L_p(a)=\#\{i<p:\bigvee_{t=i}^{p-1}x_t=a\},\qquad
R_p(b)=\#\{j>p:\bigvee_{t=p+1}^{j}x_t=b\},              \tag{2.1}
\]

and add one distinguished empty-side occurrence of value zero on each side,
denoted `L_p(0)=R_p(0)=1`.

### Theorem 2.1 (deletion multiplicity formula)

Deleting `x_p` gives

\[
\begin{aligned}
c_{w\setminus p}(T)=c_w(T)
&-\sum_{a,b}L_p(a)R_p(b)
  {\bf1}_{a\vee x_p\vee b=T}\\
&+\sum_{a\ne0,\ b\ne0}L_p(a)R_p(b)
  {\bf1}_{a\vee b=T}.                                  \tag{2.2}
\end{aligned}
\]

#### Proof

Every removed old interval is uniquely a left suffix, `x_p`, and a right
prefix, with either side possibly empty; this is the first sum.  Every new
interval is uniquely an interval crossing the new seam, hence a nonempty
left suffix followed by a nonempty right prefix; this is the second sum.
All other intervals are unchanged.  This proves (2.2). \(\square\)

Let

\[
 \mathcal C_p=\{T:\hbox{every witness of }T\hbox{ in }w\hbox{ contains }p\}.
                                                                    \tag{2.3}
\]

If `w` is universal, (2.2) immediately gives the exact criterion

\[
w\setminus p\text{ is universal}
\iff
\mathcal C_p\subseteq
\{a\vee b:L_p(a)>0,R_p(b)>0,a,b\ne0\}.                 \tag{2.4}
\]

This is an equality of literal interval catalogues, not a marginal or Hall
relaxation.

### Theorem 2.2 (complete deletion census for `U`)

No one-cell deletion of `U` is universal.  The unique minimum is the
zero-based deletion

\[
                 p=1,\qquad U_p=\mathtt{2800}.           \tag{2.5}
\]

The resulting word

```text
B = scratch/k16_upper12874_best_delete.word
SHA-256 a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
```

has length `12873` and sole hole

\[
                         D=\mathtt{2c6d}.                 \tag{2.6}
\]

Every other deletion leaves at least two holes.  The exact hole-count
histogram over all `12874` deletions is retained in

```text
scratch/k16_upper12874_deletion_census.audit.json
SHA-256 c2990f25c9ef15d7c3a4ddc5eda5f5ca4ce60e75dabe93dfc8c4988b349cd619
```

with driver SHA-256
`fc8ce6aec17be6ad7a0bb072fd04332361394896e7dbe4312d55178656baf348`.
The original word has the unique `D` witness `[1,4]`.

## 3. Adjacent collapse and OR fusion

Replace adjacent cells `x_p,x_(p+1)` by one arbitrary nonzero mask `y`.
Let `L_p` be the set of distinct suffix ORs of `w[0,p)`, including zero,
and let `R_(p+1)` be the set of distinct prefix ORs of `w[p+2,n)`, including
zero.  Let

\[
\mathcal C_{p,p+1}={T:T\text{ has no witness wholly in either outside
segment}\}.                                             \tag{3.1}
\]

### Theorem 3.1 (one-variable collapse criterion)

The collapsed word is universal if and only if

\[
 \forall T\in\mathcal C_{p,p+1}\ \exists a\in L_p,\ b\in R_{p+1}:
                         a\vee y\vee b=T.                \tag{3.2}
\]

#### Proof

Every interval in the collapsed word either avoids `y`, in which case it is
an unchanged outside interval, or contains `y`, in which case its OR has the
displayed form.  These alternatives exhaust the intervals. \(\square\)

Put

\[
K_p=\bigcap_{T\in\mathcal C_{p,p+1}}T,\qquad
B_p=\{a\vee b:a\in L_p,b\in R_{p+1}\}.                  \tag{3.3}
\]

Every solution has \(0<y\subseteq K_p\).  For fixed `p`, (3.2) is therefore
an exact one-variable problem with at most `2^16-1` values, at most 289 side
bases, and only the critical target rows.

For the special OR fusion \(y=x_p\vee x_{p+1}\), every new interval through
`y` has the same OR as the corresponding old interval containing both
cells.  Hence OR fusion creates no new OR label; it only deletes occurrences
from intervals containing exactly one of the two cells.

### Theorem 3.2 (complete adjacent-OR-fusion census)

Every one of the `12873` adjacent OR contractions of `U` fails.  The minimum
hole count is two, attained only at

\[
\begin{array}{c|c}
p&\text{holes}\\ \hline
0&\{\mathtt{2c6d},\mathtt{4879}\},\\
2&\{\mathtt{146d},\mathtt{546d}\}.
\end{array}                                               \tag{3.4}
\]

The exact artifact is

```text
scratch/k16_upper12874_adjacent_fusion_census_20260730.audit.json
SHA-256 8f8441844dff8470723566f38818d0e17da2af81fe66dbbd007e9040cdb6195e
payload 2b35f6e62cdf264f39425b07d55e47b522e16d0094951326d863a553a100516e
```

and the driver SHA-256 is
`6a4089b4599fc174d4ebc1a126a6210db19ed36577f0562bbe3a14d45cbc20e6`.

### Theorem 3.3 (complete arbitrary-collapse census)

Every one of the `12873` adjacent positions and every arbitrary nonzero
replacement value in (3.2) fails.  Exactly nine operations have one hole;
all leave `0x2c6d`:

```text
p=0: y=0x4879;
p=1: y in {0x2008,0x2009,0x2028,0x2029,
           0x2048,0x2049,0x2068,0x2069}.
```

The first operation and the last position-one operation give the same word,
so these are eight distinct one-hole words.

For completeness, let `R` be (3.1), put `K=intersection(R)`, and suppose a
value `y` works on all but a set `S` of at most one target.  Then

```text
y subseteq K_S := intersection(R \ S).
```

If `a OR y OR b=T` for a surviving target, then also
`a OR K_S OR b=T`: the latter contains the former value `T`, while every
term remains a submask of `T`.  The intersection of an empty family is
understood as `0xffff`.  Thus `K_S` is closure-maximal.  Testing `K`
and every leave-one-out `K_S`, and then directly replaying every nonzero
submask of a successful maximal value, is therefore exhaustive for zero and
one hole.  The retained audit finds no zero and lists exactly the nine rows
above:

```text
scratch/k16_upper12874_arbitrary_two_to_one_fusion_census_20260730.audit.json
SHA-256 9c9451aa69f80778ec0843dbb4471757ce779d9678a43ed6f97161a99bf7597a
payload 02ecfdcdd561fd7bd727154ade27eb3bb561f60404da9ae94409e92390ba9861

scratch/audit_k16_upper12874_arbitrary_two_to_one_fusion_census_20260730.py
SHA-256 deade2971c563312153b47ff6d6b2b6202daa8c38331507d621fc33bdf9ad279
```

This closes every frozen-complement adjacent two-to-one fusion, not a fusion
followed by further rethreading elsewhere.

## 4. The unique best deletion has no radius-one repair

For a one-hole word `B` and a position `q`, let `V_q` consist of its hole
together with every covered target all of whose witnesses contain `q`.
Let

\[
 \Gamma_q(y)=\{a\vee y\vee b:a\in L_q,b\in R_q\},       \tag{4.1}
\]

where empty sides are allowed.

### Theorem 4.1 (exact one-substitution criterion)

Replacing `B_q` by `y` makes `B` universal if and only if

\[
                             V_q\subseteq\Gamma_q(y).    \tag{4.2}
\]

In particular, every candidate satisfies

\[
                    0<y\subseteq\bigcap_{T\in V_q}T.    \tag{4.3}
\]

#### Proof

Intervals avoiding `q` survive unchanged.  Thus only the targets in `V_q`
need replacement witnesses, and every new witness through `q` has a unique
left-suffix/right-prefix form (4.1).  This proves (4.2); every cell of a
`T`-witness is a subset of `T`, giving (4.3). \(\square\)

### Theorem 4.2 (complete radius-one no-go)

For the length-`12873` word `B`, criterion (4.2) was evaluated at every
position and every arbitrary nonzero replacement value.  Exactly `77153`
necessary-domain values were tested and none completes the word.  Thus:

\[
\boxed{\text{Deleting the unique best cell and changing at most one
remaining cell cannot attain length }12873.}             \tag{4.4}
\]

The exact audit is

```text
scratch/k16_12873_phase_delete_radius1.audit.json
SHA-256 475f35023004eb7402bfb7da42135b26f277a8bf3ccf3eb904b89af4d31196f2
```

and its driver SHA-256 is
`cbfcce2d1d52904364b260b0507875fe59df96ded8ee46b138b7a01591cf6ec6`.

The minimum collateral is one at exactly sixteen central portals:

\[
 q=6440,\qquad y=\mathtt{0440}\vee s,qquad s\subseteq\mathtt{002d};
                                                               \tag{4.5}
\]

each transfers the sole hole from `0x2c6d` to `0xa86d`.  This is a new
named latch, not a completion.  The supporting provider ledger is

```text
scratch/k16_upper12874_best_delete_oneedit.audit.json
SHA-256 a05ea412d4a7e0105226d48e4d9764922388f21ff3fabab211836ce28651dafa
```

Theorem 4.2 concerns the unique best pure deletion.  A worse initial
deletion may have two or more holes which one cooperative replacement could
in principle cover simultaneously; no global delete-plus-one-substitution
theorem is claimed here.

## 5. A symbolic check at the best deletion seam

The relevant witnesses in `U` are

\[
\begin{array}{c|c}
T&\text{all witnesses}\\ \hline
\mathtt{4879}&[0,0],\\
\mathtt{6879}&[0,1],[0,2],\\
\mathtt{2c6d}&[1,4],\\
\mathtt{246d}&[2,4],\\
\mathtt{346d}&[2,5],\\
\mathtt{766d}&[2,7].
\end{array}                                               \tag{5.1}
\]

For an arbitrary collapse of `(0,1)`, the critical set contains
`0x2c6d,0x4879,0x6879`.  Every nonempty right context contains bit `0x2000`,
which `0x4879` omits, so covering `0x4879` forces the singleton
`y=0x4879`.  That inserts bit `0x4000`, forbidden by `0x2c6d`.

For an arbitrary collapse of `(1,2)`, the critical set is

\[
\{\mathtt{246d},\mathtt{2c6d},\mathtt{346d},
  \mathtt{6879},\mathtt{766d}\}.                         \tag{5.2}
\]

The only side bases contained in `0x2c6d` are

\[
                       0,\quad\mathtt{0065},\quad\mathtt{0465}. \tag{5.3}
\]

They all omit bit `0x0800`, so covering `0x2c6d` forces that bit into `y`;
the target `0x246d` forbids it.  Hence neither arbitrary neighboring
collapse repairs the best deletion.  This is a direct forced-bit proof,
independent of the exhaustive radius-one audit.

## 6. The exact fixed-gap length-12873 collar gate

Write the authenticated `(5,9,4)` architecture abstractly as

\[
                A_5\mid G_1\mid B_9\mid G_2\mid C_4,     \tag{6.1}
\]

where `G_1,G_2` are frozen and the three named blocks are arbitrary nonzero
words of the indicated lengths.  Their exact ORs are

\[
                         \bigvee G_1=\mathtt{7fff},\qquad
                         \bigvee G_2=\mathtt{ffff}.       \tag{6.2}
\]

The fixed-run audit identifies the residual targets not already witnessed
inside `G_1` or `G_2`; none can cross a complete frozen gap.  Therefore all
their candidate witnesses lie in one variable block with an exact adjacent
fixed suffix and prefix.  Bit variables for the variable cells and one
witness variable per legal interval form give an exact CNF, as in Theorem
3.1 with several consecutive variable cells.

### Theorem 6.1 (three-profile reduction)

Every length-`12873` word obtained by shortening exactly one variable block
of (6.1), while retaining both fixed gaps, belongs to exactly one of

\[
                 (4,9,4),\qquad(5,8,4),\qquad(5,9,3).    \tag{6.3}
\]

Conversely every word in one of the three profiles is such a shortening.
The position of the removed cell inside a block is irrelevant because every
remaining cell of that block is arbitrary.

#### Proof

The total variable length must fall from `18` to `17`; keeping both gaps
fixed removes one position from exactly one of the three blocks.  This gives
the three profiles in (6.3).  Since a block is an unrestricted ordered word,
deleting any one of its old slots and then allowing all remaining entries to
vary yields precisely the set of all words of the shorter block length.
This proves both directions. \(\square\)

The first branch `(4,9,4)` is already encoded exactly:

```text
scratch/build_ad_k16_12873_phase_fusion_cnf_20260730.py
SHA-256 a653e47a56307b3f648bfd98cf4471f8b46dbe944cb63ac071cf728523a292e6

scratch/decode_verify_ad_k16_12873_phase_fusion_cnf_20260730.py
SHA-256 f0b70293b9cdc9b0ed8280d1eaaf8592bf3b03006b76513f0bcd9397b6a27c6e
```

Its variable positions in the shortened word are exactly

\[
[0,4),\qquad[6435,6444),\qquad[12869,12873).             \tag{6.4}
\]

The generated exact instance and map are

```text
scratch/ad_k16_12873_phase_fusion_4_9_4.cnf
SHA-256 206581940afea13d9be331cf4d44f028dda9f79c7ffc705dea3dd2a1c928cf80

scratch/ad_k16_12873_phase_fusion_4_9_4.cnf.map.json
SHA-256 eb6f43d2b1a1b4838a6c5553840936a497abb8b4e57bccac8da6291bac378ac5
payload 31fa0be6295651058e4bc9e8057fbe868c97c0edd630d29423440996f9493b46
```

They contain `4739` variables and `145704` clauses: `272` cell-bit
variables, `4467` witness variables, `17` nonzero-cell clauses, `57`
residual-target clauses, `33300` positive witness implications, and
`112330` zero-bit exclusions, from `461` exact interval patterns.  The
decoder pins the source, emitter, CNF and map hashes; recomputes the map
payload; verifies the exact profile and all counts; rejects contradictory,
out-of-range or incomplete solver literals; clause-checks the total model;
then replays all `65535` targets literally.

There is no solver verdict or proof log.  A SAT result must pass that frozen
decoder; an UNSAT result must retain a checked DRAT/LRAT proof.  Resource
exits are `UNKNOWN`.  The sibling profiles `(5,8,4)` and `(5,9,3)` are not
yet encoded.

No heavy local or H100 job was launched in this lane.

## 7. Exact remaining boundary

The following are now closed for the frozen upper word:

1. pure deletion at every position;
2. arbitrary adjacent two-to-one fusion at every boundary;
3. arbitrary one-cell repair after the unique best deletion;
4. arbitrary collapse at either boundary adjacent to that best deletion.

The smallest constructive gate is feasibility of the three exact profiles
in (6.3), beginning with the ready `(4,9,4)` model.  Independently, a global
delete-plus-one-substitution audit must still include the nonminimum initial
deletions.  A collapse followed by additional nonlocal rethreading also
remains open.

If all three profile CNFs are proved UNSAT, only the fixed-gap `(5,9,4)`
shortening class is closed; unrelated length-`12873` words remain possible.
If any profile is SAT and full replay passes, (1.1) immediately becomes

\[
                              \nu(16)=12873.              \tag{7.1}
\]

The old trimmed-lift deletion and fixed-copy rethread no-gos remain valid
only for their stated standard-lift architectures.  The proof-closed old
`(4,7,3)` collar result covers exactly its one-change slice.  None of those
theorems may be relabelled as an obstruction to the present mixed `(5,9,4)`
carrier or the three profiles (6.3).
