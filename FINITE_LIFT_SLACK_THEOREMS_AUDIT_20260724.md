# Independent finite-math audit: lift slack theorems

Date: 2026-07-24

Source audited: `FINITE_LIFT_SLACK_THEOREMS_20260724.md`.

## Scope and source version

This is a symbolic audit only.  No stored word, certificate, solver output,
or search result was inspected or used.  Numerical values denoted `B(k)` or
`U(k)` are treated solely as hypotheses printed in the source; this audit
checks the implications and arithmetic conditional on those values, not the
external claim that they have been certified.

The source changed during the audit.  It was reread after the in-place
sharpening from `k+1` to `k`; the version audited here is the live version
containing Section 9, the coefficient `k` in Theorems 4.1 and 5.1, and the
printed run counts `3,6,12,21`.

## Verdict

The endpoint constructions, all seam witnesses, the product-chain lemma,
the interval-antichain arguments, the high-run classification, and the
abstract double-cover criterion are valid.  No missing witness category was
found.

There is one material mathematical correction:

> At fixed old rank `r`, every seam category used in Sections 4 and 5 is
> bounded by `r`, not merely by `k`.

Thus the source's inequalities with coefficient `k` are valid but not exact
or sharp when `r<k`.  The words “exact constant,” “exact one-transition
ceiling,” and “exact quantitative obstruction” require qualification.  The
stronger valid inequalities are

\[
z\ge M,
\qquad
h\ge M-r,
\qquad
|W|\ge2M-r
\]

for one transition, and

\[
M\le h+r\left(\binom q2+3q\right),
\qquad
|W|\ge2M-r\left(\binom q2+3q\right)
\]

for `q` high runs.  In the four central finite rows this changes the
strongest run-count consequence obtainable from the proof to

\[
5,9,17,31,
\]

not `3,6,12,21`.

A second implication correction is needed.  The high-position ranges force
large high mass only when `q` is fixed at its least permitted value.  The
inequalities alone allow all high runs to be singletons once `q` is much
larger.  Therefore the source proves a run-count/high-mass tradeoff, not the
unqualified simultaneous necessity of long runs and many transitions.

All Section 6 and Section 8 numerical statements are conditional on the
printed `B/U` inputs.  The arithmetic is otherwise correct, subject to the
rank-sensitive strengthening above.

## 1. Formal hypotheses

The natural ranges should be stated explicitly:

\[
k,n\ge1,
\qquad
1\le t\le n,
\qquad
1\le s\le n,
\qquad
1\le r\le k.
\]

The endpoint formulas remain meaningful in the degenerate cases after the
usual empty-block convention, but some indexed displays are formally
undefined without these ranges.  For `r=0`, the proof of `z>=binom(k,r)`
would improperly invoke the empty old target, which is not part of the
universality definition.  All finite applications use `1<=r<=k`.

Classification: **formal correction only**.

## 2. Ordinary trimmed lift

Let `A=(a_1,...,a_n)` be universal on `[k]`.  The word

\[
A,\{x\},\{x\}\cup a_1,\ldots,\{x\}\cup a_{n-1}
\]

has length `2n`.

For every nonempty old target `S`, choose an old witness `[i,j]`.

- The target `S` itself uses that interval in the first copy.
- If `j<n`, the transformed interval from `x union a_i` through
  `x union a_j` has union `S union {x}`.
- If `j=n`, the seam interval

  \[
  a_i,a_{i+1},\ldots,a_n,\{x\}
  \]

  has union `S union {x}`.
- The target `{x}` uses the singleton.

The cases exhaust every nonempty target in the lifted dimension.

Classification: **valid**.

## 3. One-ended endpoint compression

Put `p=n-t+1` and assume

\[
a_p\supseteq a_{p+1}\supseteq\cdots\supseteq a_n.
\]

The proposed word is

\[
a_1,\ldots,a_n,\{x\},
\{x\}\cup a_1,\ldots,\{x\}\cup a_{p-1}.
\]

Its length is

\[
n+1+(p-1)=2n-t+1.
\]

If `[i,j]` witnesses `S` and `j<p`, its transformed copy is present.  If
`j>=p`, then every later entry belongs to `a_j`, so

\[
\bigcup_{\ell=i}^na_\ell
=\bigcup_{\ell=i}^ja_\ell=S.
\]

The seam interval `a_i,...,a_n,{x}` therefore witnesses `S union {x}`.
No interval crosses an omitted transformed entry.

The reversed prefix construction is also correct.  Under

\[
a_1\subseteq\cdots\subseteq a_t,
\]

a witness with `i>t` is copied into the transformed suffix.  If `i<=t`,
then

\[
\bigcup_{\ell=1}^{i-1}a_\ell\subseteq a_i,
\]

so the seam interval `{x},a_1,...,a_j` has unchanged old projection.

The saving relative to the ordinary `2n` lift is exactly `t-1`.

Classification: **valid**.

## 4. Two-ended endpoint compression

Assume both

\[
a_1\subseteq\cdots\subseteq a_s
\]

and

\[
a_p\supseteq\cdots\supseteq a_n,
\qquad p=n-t+1.
\]

The proposed word is

\[
\{x\}\cup a_{s+1},\ldots,\{x\}\cup a_{p-1},
\{x\},a_1,\ldots,a_n,\{x\}.
\]

For an old witness `[i,j]`, exactly one of the following applies:

1. If `i<=s`, the interval `{x},a_1,...,a_j` works because the added old
   prefix is contained in `a_i`.
2. If `i>s` and `j>=p`, the interval `a_i,...,a_n,{x}` works because the
   added old suffix is contained in `a_j`.
3. If `i>s` and `j<p`, then

   \[
   s+1\le i\le j\le p-1,
   \]

   so the complete transformed interval is present.

These cases are exhaustive.  If the endpoint chains overlap so that the
transformed block is empty, case 3 is automatically impossible.

The exact length is

\[
n+2+\max(0,n-s-t).
\]

When `s+t<=n`, this becomes

\[
2n-s-t+2.
\]

Thus the saving is `s+t-2` only in the disjoint regime.  In the overlapping
regime the length is `n+2` and the saving is `n-2`.  The Section 8 finite
tables lie automatically in the disjoint regime because reduced chains have
`s+t<=2k` while the displayed base lengths are much larger than `2k`.

Classification: **valid**, with the disjoint-regime qualifier required when
the saving `s+t-2` is quoted.

## 5. Adjacent-equal reduction and endpoint ceilings

Deleting one of two adjacent equal entries preserves every interval union:
an interval using only the deleted copy may use the retained copy, an
interval crossing the pair remains contiguous after deletion, and all other
intervals merely reindex.  Hence a shortest word may be assumed to contain
no adjacent equality.

Every weak endpoint inclusion chain in a reduced word is then strict.  Its
entries are nonempty subsets of `[k]`, so cardinality changes at every step
and its length is at most `k`.

Therefore

\[
t-1\le k-1.
\]

For the two-ended formula, let `D` be the saving from `2n`.  Then

\[
D=n-2-\max(0,n-s-t).
\]

If `s+t<=n`, this is `s+t-2<=2k-2`.  If `s+t>n`, then

\[
D=n-2<s+t-2\le2k-2.
\]

Thus the universal endpoint ceilings `k-1` and `2k-2` are correct even in
the overlap case.

Classification: **valid**.

## 6. Product-chain seam lemma

Let

\[
P_1\subseteq\cdots\subseteq P_a,
\qquad
Q_1\subseteq\cdots\subseteq Q_b
\]

and fix `C`.  Choose one index pair `(u,v)` for every distinct fixed-rank
output

\[
P_u\cup C\cup Q_v.
\]

If two chosen pairs are comparable in the product order, their outputs are
comparable.  Distinct sets of the same cardinality cannot be properly
comparable.  Hence the chosen pairs form an antichain in `[a]x[b]`, whose
size is at most `min(a,b)`.

After repeated states are collapsed, an arbitrary chain of subsets of
`[k]` has at most `k+1` states.  This proves the source's `k+1` generic seam
bound.

### 6.1 Rank-sensitive strengthening

Suppose the outputs all have cardinality `r`.  Every chain state used by a
chosen output lies inside that output.  A strict used chain therefore has at
most `r+1` possible cardinalities `0,...,r`.

Moreover, the bound is at most `r` if either:

- one variable chain consists only of nonempty states; or
- `C` is nonempty.

In the first case the possible sizes are `1,...,r`.  In the second, replace
each state by its union with `C`; its possible sizes are

\[
|C|,|C|+1,\ldots,r,
\]

so there are at most `r-|C|+1<=r` states.

This strengthening requires no disjointness or independence of `P,Q,C`.

Classification: the source's generic `k+1` lemma and its one-unit `k`
sharpening are **valid**, but `k` is not the strongest constant in the
fixed-rank applications.

## 7. One-transition theorem

Assume the high-bit indicator has exactly one transition.  The zero and
high entries form two nonempty endpoint blocks `Z,H` in one of the two
orders.  Put

\[
M=\binom{k}{r},
\qquad 1\le r\le k.
\]

### 7.1 Zero-block bound

Every witness for an old rank-`r` target lies wholly in `Z`.  Chosen
intervals for distinct equal-rank targets are nonnested, since interval
containment implies containment of their unions.  An antichain of intervals
in a block of length `z` has size at most `z`: two antichain intervals
cannot share a left endpoint.  Therefore

\[
z\ge M.
\]

### 7.2 High-target classification

For each target `{x} union R`, choose one witness.  Witnesses wholly inside
`H` form an interval antichain and contribute at most `h` targets.  Every
other witness crosses the unique seam.

The old projection of a crossing witness is the union of a suffix-OR chain
and a prefix-OR chain.  On the zero side, every such state contains at least
one nonempty zero entry.  Hence that variable chain is nonempty, and the
rank-sensitive seam lemma bounds the crossing targets by `r`.

Thus the stronger theorem is

\[
\boxed{
z\ge M,
\qquad
h\ge M-r,
\qquad
|W|\ge2M-r.
}
\]

If `Z` is an intact base word of length `n`, then

\[
|W|\ge n+M-r.
\]

If `n=M+d`, the saving from `2n` is at most

\[
d+r.
\]

The live source states the same inequalities with `k`.  Since `r<=k`, those
inequalities are true but weaker.  Calling `d+k` the “exact constant” is
unsupported when `r<k`.

Classification: **structurally valid; constants corrected from `k` to
`r` for the strongest theorem proved by the argument**.

## 8. Many-high-run theorem

Write the tag pattern as

\[
Z_0,H_1,Z_1,H_2,\ldots,H_q,Z_q,
\]

where all internal zero runs are nonempty; an endpoint zero run may be
absent.  Let `h` be the total high length and `z` the total zero length.

### 8.1 Old targets

Every old rank-`r` witness lies in one zero run.  Summing the interval
antichain bounds over all zero runs gives

\[
z\ge M.
\]

### 8.2 Complete witness classification

Choose one witness for every `{x} union R`, `|R|=r`.

Witnesses internal to one `H_a` contribute at most `|H_a|`, hence at most
`h` in total.

For a noninternal witness, let `H_a,H_b` be the first and last high runs it
meets.

- If `a<b`, the start lies in `Z_{a-1}` or `H_a`, the end lies in `H_b` or
  `Z_b`, and all intervening material is forced.  Its old projection is

  \[
  P_u\cup C_{a,b}\cup Q_v,
  \]

  where `P_u` is a suffix state of the left wing and `Q_v` a prefix state of
  the right wing.  This includes witnesses spanning any number of
  intermediate high and zero runs.  Since `a<b`, the fixed middle contains
  at least one nonempty internal zero run, so `C_{a,b}` is nonempty.  The
  rank-sensitive seam bound is at most `r` for each of the `binom(q,2)`
  pairs.

- If `a=b`, excluding internal witnesses, exactly three endpoint types
  remain:

  \[
  Z_{a-1}\longrightarrow H_a,
  \qquad
  H_a\longrightarrow Z_a,
  \qquad
  Z_{a-1}\longrightarrow Z_a.
  \]

  In each type at least one variable chain consists of nonempty suffixes or
  prefixes of a zero run.  Hence each type contributes at most `r` targets.
  Missing endpoint zero runs only remove categories.

The categories are disjoint and exhaustive.  Therefore

\[
\boxed{
M\le h+r\left(\binom q2+3q\right)
}
\]

and, together with `z>=M`,

\[
\boxed{
|W|\ge2M-r\left(\binom q2+3q\right).
}
\]

The source's coefficient `k` remains a valid weaker bound.  The category
count `binom(q,2)+3q` is correct.  In particular, no witness spanning
intermediate runs has been omitted.

For `q=1`, Theorem 5 allows a high run in the interior and therefore allows
three noninternal endpoint types.  This does not conflict with Theorem 4,
where “exactly one transition” forces the high run to one endpoint.

Classification: **classification valid; constants corrected from `k` to
`r` for the strongest uniform fixed-rank theorem**.

## 9. Corrected finite hard-step consequences

Adopt the numerical `M`, `B(k)`, and target `L=B(k+1)` values printed in the
source as hypotheses.  Let

\[
F(q)=\binom q2+3q=\frac{q(q+5)}2,
\qquad
D=2M-L.
\]

At total length `L`, `z>=M` gives

\[
h\le L-M,
\]

while the rank-sensitive many-run theorem gives

\[
h\ge M-rF(q).
\]

Thus the corrected necessary condition is

\[
\boxed{rF(q)\ge D.}
\]

For the central rows `k=2r`, the exact arithmetic is:

\[
\begin{array}{c|r|r|r|r|r|r|c}
k&r&D&d=B(k)-M&2B(k)-L&d+r&q_{\min}&
\text{range at }q_{\min}\\ \hline
12&6&129&2&133&8&5&774\le h\le795\\
14&7&426&2&430&9&9&2991\le h\le3006\\
16&8&1427&3&1433&11&17&11374\le h\le11443\\
18&9&4859&3&4865&12&31&43598\le h\le43761.
\end{array}
\]

The predecessor and threshold checks are

\[
6F(4)=108<129\le150=6F(5),
\]

\[
7F(8)=364<426\le441=7F(9),
\]

\[
8F(16)=1344<1427\le1496=8F(17),
\]

and

\[
9F(30)=4725<4859\le5022=9F(31).
\]

The high-position lower endpoints are respectively

\[
924-6F(5)=774,
\]

\[
3432-7F(9)=2991,
\]

\[
12870-8F(17)=11374,
\]

and

\[
48620-9F(31)=43598.
\]

The upper endpoints are `L-M`, as printed.

The source's live coefficient-`k` table is internally arithmetically
correct: it proves the weaker necessary counts `3,6,12,21`.  Those numbers
are not the least counts allowed by the strongest seam estimate available
from the same proof.  Likewise its displayed high-position ranges are
ranges under the weaker inequalities at run counts that the stronger
inequality excludes.

The one-transition impossibility and the failure of the two-ended
`H-Z-H` architecture remain valid a fortiori.  The corrected one-transition
saving ceilings are `d+r=8,9,11,12`, all far below the required savings
`133,430,1433,4865`.

Classification: **printed implications valid but nonsharp; “required least
q” and “exact constants” corrected as above**.

## 10. Run-count/high-mass tradeoff

At `q=q_min`, the corrected intervals in Section 9 force a large total high
mass and hence long average high runs.  This conclusion cannot be made
uniformly over all larger `q`, because the lower bound

\[
h\ge M-rF(q)
\]

decreases quadratically with `q`.

Indeed, setting `h=q` shows that the inequalities themselves permit every
high run to be a singleton once

\[
M\le q+rF(q).
\]

The first such `q` values in the four rows are

\[
16,29,55,102.
\]

For example,

\[
15+6F(15)=915<924,
\qquad
16+6F(16)=1024\ge924,
\]

and similarly

\[
28+7F(28)=3262<3432\le3480=29+7F(29),
\]

\[
54+8F(54)=12798<12870\le13255=55+8F(55),
\]

\[
101+9F(101)=48278<48620\le49215=102+9F(102).
\]

These inequalities do not construct universal words with singleton high
runs.  They show only that Theorem 5 does not exclude them once `q` is
large.  The safe conclusion is:

> At the minimum permitted run count, the high mass must be large.  In
> general, the theorem gives a quantitative tradeoff between run count and
> high mass.

The source's unqualified statement that every viable theorem needs both
long high runs and many transitions, and that isolated separators are not
enough, is unsupported by the stated inequalities.

Classification: **corrected implication**.

## 11. Abstract double interval-cover criterion

Let

\[
w_i=
\begin{cases}
p_i,&\epsilon_i=0,\\
p_i\cup\{x\},&\epsilon_i=1,
\end{cases}
\]

with `p_i` nonempty whenever `epsilon_i=0`; empty `p_i` are allowed at high
positions.

If a target avoids `x`, every witnessing interval must have all tags zero,
and its projected union is that target.  If the target is `S union {x}`, its
witness must meet a tag-one position and its old projection is `S`, including
`S=empty` for the singleton target `{x}`.  The converse is immediate.

Therefore the two stated interval-cover conditions are necessary and
sufficient.  They are tautological but exact.

The rank arithmetic proves that a construction at the four printed hard
target lengths needs at least the corrected run counts in Section 9.  An
intact universal zero block supplies condition 1 but, from universality
alone, supplies no information about condition 2.  The two-ended endpoint
construction has tag pattern `H-Z-H` and hence only two high runs.

The source's sentence that “no claimed recursive improvement follows from
the base length or endpoint chains alone” is too broad if read literally:
Theorems 2.1 and 2.2 do give conditional recursive upper improvements from
quantified endpoint chains.  The justified statement is narrower:

> Base universality and length alone do not imply the high-tag interval
> cover, and one-/two-ended endpoint constructions cannot attain the four
> printed hard exact targets.  A hard-step multi-transition improvement
> requires additional structure.

Classification: **criterion valid; broad concluding implication corrected**.

## 12. Conditional endpoint-improvement arithmetic

All conclusions in this section are conditional on the existence of a word
of the printed base length with the stated endpoint chain.  No such endpoint
data are verified here.

### 12.1 Current-upper table

The one-ended bound is

\[
2U(k)-t+1.
\]

Substitution gives exactly

\[
1853-t,
3705-t,
7353-t,
14705-t,
29409-t,
58817-t,
117633-t.
\]

Strict comparison with the printed next-dimensional upper values requires
`t>=2` in every row except `13 -> 14`, where `t>=30`.  In a reduced word on
`[13]`, a strict nonempty endpoint chain has length at most `13`, so a
length-`1852` reduced base cannot meet `t>=30`.

With two endpoints and the printed base length `1852`, the disjoint formula
is

\[
3706-(s+t).
\]

Strict improvement over `3676` requires

\[
s+t\ge31.
\]

Reduction gives `s,t<=13`, hence `s+t<=26`.  This impossibility is tied to
the printed base length.  If a substantially shorter base were independently
available, the threshold would change.

### 12.2 Hypothetically exact odd bases

For an exact base length `n` and target length `L`, the one-ended sufficient
condition is

\[
t\ge2n+1-L,
\]

while in the disjoint two-ended regime it is

\[
s+t\ge2n+2-L.
\]

The printed pairs therefore give

\[
(t,s+t)=(5,6),(4,5),(4,5).
\]

These chain lengths are combinatorially possible, not proved to occur.

### 12.3 Hard even-to-odd one-ended requirements

The one-ended chain required to hit the printed hard target is

\[
t\ge2B(k)+1-B(k+1),
\]

which gives

\[
134,431,1434,4866.
\]

Each exceeds the strict-chain maximum `k=12,14,16,18`.  Thus endpoint
compression cannot hit those printed hard targets, conditional on the
printed base and target lengths.  The stronger many-run theorem gives the
corrected architecture counts from Section 9.

Classification: **all endpoint arithmetic valid with the stated conditional
and base-length scope**.

## 13. Evidence and presentation classifications

The following phrases cannot be independently certified in a math-only
audit because `B` and `U` are not intrinsically defined or proved in this
document:

- “certified rank-count values”;
- “currently certified nonzero upper length”;
- references to stored certificates.

Every algebraic implication remains valid when the printed numbers are
adopted as assumptions.

The live source also contains the bullet

```text
no one-transition lift can preserve B(k) in any hard row
```

twice consecutively.  This is a presentation duplication, not a
mathematical issue.

## Final classification

### Valid

- the ordinary trimmed lift;
- the terminal descending-tail lift and its reverse;
- the complete two-ended witness split, including overlap;
- adjacent-equal coalescing and strict endpoint-chain ceilings;
- the chain-product antichain lemma;
- the interval-antichain bound in each zero or high run;
- the first/last-high-run classification, including all intermediate runs;
- the `binom(q,2)+3q` seam-category count;
- the abstract double interval-cover criterion;
- all endpoint-improvement arithmetic, conditional on the printed inputs.

### Corrected

- add the formal ranges `1<=r<=k`, `1<=s,t<=n`;
- replace the fixed-rank seam coefficient `k` by `r` for the strongest
  theorem supplied by the proof;
- replace the hard-row least run counts `3,6,12,21` by `5,9,17,31` when the
  rank-sensitive lemma is used;
- replace the corresponding minimum-run high-position ranges by those in
  Section 9;
- restrict the saving `s+t-2` to the disjoint endpoint regime;
- replace the blanket long-run conclusion by a run-count/high-mass tradeoff;
- narrow the statement about absence of recursive improvement to the four
  hard exact targets and to what follows from base universality alone.

### Unsupported without external data or additional theorems

- that the coefficient `k` is exact or sharp;
- that every viable architecture must have long high runs even when `q` is
  allowed to exceed its minimum;
- the external certification status of the printed `B/U` values;
- existence of any endpoint chains appearing in the conditional tables;
- existence of a multi-transition double cover at any of the allowed run
  counts.

The stable finite-math conclusion is that endpoint compression is correct
but intrinsically `O(k)`, while a hard even-to-odd target requires a genuine
multi-run double interval cover.  The exact run classification is sound;
its fixed-rank constants are stronger than stated in the source.
