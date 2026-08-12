# Independent adversarial audit of `K11_NONSATURATED_ONE_DEFECT_CORE_20260724.md`

## 1. Verdict

The principal one-defect theorem is correct.  In the guarded branch

```text
(delta_5,s)=(0,1),
```

the selected rank-five intervals force chain A, every core triple except
possibly one is either a selected rank-five triple or contains a selected
rank-five pair, and the possible uncovered triple is exactly

```text
H=[h3,h3+2]
```

when the `12` block is empty.  The collision injection is valid and gives,
with no off-by-one loss,

```text
y1+2*n5+Delta_lit <=368+v,
y2>=94+n5+Delta_lit-v,
y2>=93+n5+Delta_lit.
```

The duplicate-free two-component branch is also correct.  After reversal it
is chain B, its two low components have slacks two and one, no low triple
carrier exists, and its exact pair budget gives

```text
y1+2*n5+Delta_lit <=367,
y2>=95+n5+Delta_lit.
```

All headline constants, equality directions, and branch guards survive the
audit.  In particular, the difference between `368+v` and `367` is exactly
the difference between one contiguous core with `N-1` physical pairs and two
low components with only `N-2` internal physical pairs.

Three corrections or qualifications are required.

1. Section 2's claim that only its four listed inputs are used is not
   literally true.  The main application additionally needs the named-cell
   shortening theorem for every rank-at-most-four target.  Sections 5.7--5.9
   and 7.1--7.2 also invoke the rank-four surplus-component theorem, exact
   boundary--core rigidity, and the coordinate-transversal theorem.
2. The summed moment (5.40), and the corresponding summed moment following
   (7.14), require

   ```text
   0<=t<=10.
   ```

   At `t=11` their added `+1` run term makes the displayed inequality false.
   The pointwise rows (5.39) and (7.14) themselves remain valid for every
   `B`.  In Section 5.6, the statement that `L(t)-dB` is positive for every
   `t<=10` also has one edge exception: it may be zero at `t=10`.  The
   required fact `RB>=1` is nevertheless true because every rank-one value
   occurs literally in the low core.
3. Equations (5.35)--(5.40) and (7.11)--(7.14) are lossless necessary
   parameterizations of every hypothetical word.  They are not sufficient
   numerical classifications: integers satisfying the rows need not admit
   compatible OR labels or interval placements.  “Finite exact
   parameterization” should be read in that necessary, word-to-data sense.

These corrections do not weaken either new collision inequality or any
conclusion in the main verdict.  The report correctly makes no claim that
length 465 is impossible.

This audit is proof-only.  No search result, solver run, failed instance, or
enumeration is used as mathematical evidence.

## 2. Basic counts and hypotheses

The lower ideal through rank four has size

```text
C(11,1)+C(11,2)+C(11,3)+C(11,4)
=11+55+165+330
=561.
```

The rank-five layer has size `C(11,5)=462`.  In the one-component branch,

```text
N=465-n5,
q=462-n5=N-3,
y1+y2=q.
```

Here `y1` and `y2` count selected nonliteral rank-five pair and triple
witnesses.  A nonliteral rank-five witness cannot meet a literal rank-five
position: if it contained the literal value `R` and had OR `T`, then
`R subseteq T` and `|R|=|T|=5`, so `R=T`.  Thus every selected nonliteral
rank-five witness is wholly internal to the low component.

Likewise, every witness for a rank-at-most-four target is wholly internal to
a low component.  It cannot contain a literal rank-five entry.  To apply the
one-defect lemma, one also needs the established named-cell shortening fact:
each such target has a witness of physical length at most three.  This is an
additional input, not a consequence of the four items listed in Section 2
of the report.

Selected witnesses for distinct equal-rank targets are interval
incomparable.  Containment of two selected intervals would imply containment
of their OR values; equal cardinality would then force the values to be
equal.  This justifies every strict-endpoint argument used later.

## 3. The path lemma and its exact defect count

Let the `N-1` adjacent-pair cells of a segment be the vertices of a path.
Its `N-2` edges are the physical triples.  Suppose `a` selected rank-`r`
witnesses are pairs and `b` are triples.  Here

```text
a+b=q=N-3.
```

The selected pair set omits at least two of the `N-1` path vertices.  Break
it into runs.  A selected run of length `ell` touching a path endpoint is
incident with `ell` triple cells; an internal run is incident with
`ell+1`.  Incident-edge sets of distinct runs are disjoint.  Hence at least
`a` distinct physical triples contain a selected pair.

A selected rank-`r` triple cannot contain a selected rank-`r` pair belonging
to a different target.  The two OR values would be comparable rank-`r`
sets and hence equal.  Therefore the `b` selected triples are disjoint from
the triples incident with selected pairs.  At least

```text
a+b=q
```

of the `N-2=q+1` triples are covered, leaving at most one.

Every covered triple has OR-rank at least `r`: it either has rank exactly
`r` as a selected triple or contains a pair of rank `r`.  Consequently at
most one physical triple can have OR-rank below `r`.  A lower target whose
short witness is not a singleton or pair must use that triple.  Since one
physical cell has only one OR value, at most one lower target can do so.

There is no collision or multiplicity gap in this argument.  In particular,
two selected pair runs separated by one unselected pair cell contribute two
different boundary triples, not one doubly counted triple.

## 4. Chain A and the named carrier

Order the 462 selected rank-five intervals by left endpoint and write

```text
alpha_j=ell_j-j,
beta_j =r_j-j.
```

There are 462 distinct left endpoints and 462 distinct right endpoints in
465 positions, so

```text
0<=alpha_j<=beta_j<=3.
```

Both sequences are nondecreasing, and the length-three cap gives
`beta_j-alpha_j<=2`.

Under `(delta_5,s)=(0,1)`, literal rank-five singleton positions form only
the two outer boundary blocks.  Hence the internal diagonal states `11` and
`22` are absent.  The remaining states form the unique chain

```text
00 < 01 < 02 < 12 < 13 < 23 < 33.
```

With the report's boundaries, direct endpoint substitution gives

```text
C=[h1,h6+2],
N=h6-h1+3=465-n5,
n5=462+h1-h6,
y1=(h2-h1)+(h4-h3)+(h6-h5),
y2=(h3-h2)+(h5-h4).
```

The pair starts are

```text
[h1,h2-1], [h3+1,h4], [h5+2,h6+1],
```

and the selected triple starts are

```text
[h2,h3-1], [h4+1,h5].
```

If `h3<h4`, the middle pair block covers triple starts from `h3` through
`h4`; together with the outer pair and triple blocks this covers every core
triple.  If `h3=h4`, the blocks cover every triple start except `h3`.
Thus the unique uncovered cell is exactly

```text
H=[h3,h3+2].
```

This remains true when any surrounding state block is empty, including when
`H` touches an endpoint of `C`.  Therefore the carrier variable is correctly
guarded by

```text
e=1 iff h3=h4 and |OR(H)|<=4.
```

Only when this physical cell is assigned a nonliteral lower target does it
save a lower pair cell; that sharper condition is the report's `v=1`.

## 5. Chain-A Hall and collision rows

### 5.1 Unweighted Hall count

There are `N` singleton cells and `N-1-y1` pair cells not selected at rank
five.  At most `H` contributes one more lower cell.  Hence

```text
561<=N+(N-1-y1)+e.
```

Substituting `y1=N-3-y2` gives

```text
y2>=94+n5-e,
y2>=93+n5.
```

If

```text
F=sum_(r=1)^4 max(nr-C(11,r),0),
```

then at most `N-F` singleton positions can provide distinct lower values.
The same count gives

```text
y2>=94+n5+F-e
   >=93+n5+F.
```

Substitution of the chain-A boundaries yields exactly

```text
h3+h5+h6 >=h1+h2+h4+555+F,
```

or constant `556-e` in the carrier-resolved version.  The displayed example
`n5=134,y2=221` is therefore correctly cut by the unconditional lower bound
`227`.

### 5.2 The full collision injection

Let `zr` be the number of distinct rank-`r` entry values in `C`, and put

```text
Delta_lit=N-(z1+z2+z3+z4).
```

Universality forces all eleven rank-one values to occur literally, so
`z1=11`.  Also

```text
Delta_lit>=F.
```

The exact number of lower masks which are not literal values in `C` is

```text
561-(z1+z2+z3+z4)
=561-(N-Delta_lit)
=96+n5+Delta_lit.
```

All but the possible target assigned to `H` require adjacent-pair witnesses.
Map those

```text
96+n5+Delta_lit-v
```

targets to their chosen pair cells.  Map the `y1` selected rank-five pair
targets to their own pair cells.  The combined map is injective:

* targets within one rank have distinct OR values;
* targets of different ranks cannot have the same OR value; and
* one physical pair cell has one fixed OR value.

No containment or endpoint assumption beyond the already proved
localization is used here.  The one-component core has exactly

```text
N-1=464-n5
```

physical pair cells.  Therefore

```text
(96+n5+Delta_lit-v)+y1 <=464-n5,
```

which rearranges to the advertised exact constant

```text
y1+2*n5+Delta_lit <=368+v.               (A)
```

Using `y1+y2=462-n5`, (A) is equivalent to

```text
y2>=94+n5+Delta_lit-v.
```

Since `v<=1`,

```text
y2>=93+n5+Delta_lit.
```

Thus the sign, factor `2*n5`, constants `368,94,93`, and implication
directions are all correct.

### 5.3 Equality

Set

```text
D=y2-(93+n5+Delta_lit).
```

If `D=0`, the carrier-resolved inequality forces `v=1` and equality in the
pair injection.  Hence every one of the `N-1` pair cells is used either by a
nonliteral lower target or by a selected rank-five pair target.

The selected rank-five pair cells are then only the two endpoint-touching
runs, because `v=1` forces `h3=h4`.  They contaminate exactly `y1` triples,
the selected rank-five triples occupy `y2` further triples, and

```text
y1+y2+1=N-2.
```

The remaining triple is `H`.  The middle lower-pair zone has

```text
p=N-1-y1=96+n5+Delta_lit-1
```

edges, and therefore `p-1` internal triples.  One is `H`; the other

```text
p-2=93+n5+Delta_lit=y2
```

are exactly the selected rank-five triples.  The equality skeleton and all
of its constants are correct.

At `n5=134`, the nested rank-four structure removes the effective carrier,
so `D=0` is impossible.  At `n5=133`, the only inner branch with a genuine
carrier is

```text
x4=0, s3=1, v4=1, rho=4.
```

Then

```text
y2=226+Delta_lit,
y1=103-Delta_lit,
Delta_lit>=101-n4,
n4<=103.
```

These follow respectively from `D=0`, `y1+y2=329`, the bound of 231
distinct rank-at-most-three literal values, and the slack-two lower capacity.

## 6. Audit of the remaining constants

### 6.1 Weighted incidence

The total rank of the lower ideal is

```text
11+2*55+3*165+4*330=1936.
```

After using a low carrier of rank `rho`, lower targets assigned to
singleton/pair cells have total rank `1936-rho`.  Distinct useful singleton
values contribute at most `S-E`.  The pair OR-rank sum is at most

```text
2*S-r_first-r_last <=2*S-2,
```

because the word is zero-free.  The selected rank-five pairs consume
`5*y1` of this pair capacity.  Thus

```text
1936-rho+5*y1 <=3*S-E-2,
3*S-E-5*y1    >=1938-rho.
```

Since a low carrier has `rho<=4`,

```text
3*S-E-5*y1>=1934.
```

The constants `1936,1938,1934` are exact.  When there is no low carrier,
`rho=0` and the stronger constant is `1938`.

### 6.2 Coordinate ledgers

For one coordinate `b`, the numbers of lower masks containing and omitting
it are

```text
1+10+45+120=176,
10+45+120+210=385.
```

At most one target uses `H`.  A marked position belongs to at most three
singleton/pair cells, so `3*ob>=175` and

```text
ob>=59.
```

If the `Zb` unmarked positions form `Rb` runs, their singleton/pair cells
number `2*Zb-Rb`.  Since at least 384 omitting targets use them and
`Rb>=1`,

```text
Zb>=193.
```

Summing over the eleven coordinates gives

```text
S>=11*59=649,
11*N-S>=11*193=2123,
S<=11*(465-n5)-2123=2992-11*n5.
```

For the exact endpoint-pair exclusion, let `ab` and `cb` count selected
rank-five pair values omitting and containing `b`.  Then

```text
sum_b ab=6*y1,
sum_b cb=5*y1.
```

The report's rows

```text
2*Zb-Rb-ab       >=385-db,
2*ob+Rb-1-cb     >=176-fb
```

are exact one-component cell counts.  Using `Rb>=1` and `Rb<=ob+1` gives

```text
Zb>=193+ceil((ab-db)/2),
ob>=ceil((176-fb+cb)/3).
```

Summing the integer excesses correctly yields

```text
Komit=max(0,ceil((6*y1-e*(11-rho))/2)),
Khit =max(0,ceil((5*y1-11-e*rho)/3)).
```

The `-11` in `Khit` is correct: the baseline value 59 absorbs one unit of
`cb` in each coordinate.  The additional `-e*rho` records the second unit
absorbed in coordinates contained in `H`.  The aggregate row

```text
649+Khit <=S<=11*N-2123-Komit
```

therefore follows.  For `e=0`, `Komit=3*y1`, giving the stated upper row

```text
S+3*y1<=11*N-2123.
```

### 6.3 All-codimension moments

For a proper coordinate set `B`, the `B`-free singleton/pair cells number
`2*ZB-RB`; removing selected rank-five pairs disjoint from `B` gives

```text
2*ZB-RB-aB>=L(t)-dB.
```

Summing over all `t`-sets gives, for `0<=t<=10`,

```text
2*sum_i C(11-|A_i|,t)
 >=C(11,t)*(L(t)+1)+C(6,t)*y1
    -e*C(11-rho,t).
```

The `+1` comes from `RB>=1`.  At `t=10`, `L(t)-dB` can be zero, contrary to
one sentence in the report, but `RB>=1` still follows from the literal
rank-one value outside `B`.  Thus the summed formula remains correct.

For `t=6`,

```text
C(11,6)*(L(6)+1)=462*(30+1)=14322,
```

and the displayed coefficients

```text
210,84,28,7
```

are `C(10,6),C(9,6),C(8,6),C(7,6)`.  Equation (5.23) is correct.

At `n5=134`, substituting

```text
(n1,n2,n3,n4)=(11,55,165+F,100-F),
y1<=100-F
```

gives the exact residual lower bounds

```text
t=1: 404+8F
t=2: 2810+29F
t=3: 8465+62F
t=4: 14410+85F
t=5: 15150+76F
t=6: 10078+43F.
```

All six constants independently expand correctly.  Moving a surplus entry
from rank three to rank one or two increases every relevant binomial moment,
so the minimization direction is also correct.

## 7. Rank-four recursion

The nested rank-four sections require the previously established rank-four
surplus and boundary--core theorems.  Conditional on those inputs, their
accounting is correct.

Put

```text
e4=134-n5,
z4=n4-x4.
```

After deleting the rank-four entries, the total length of the
rank-at-most-three components is `N-n4`, while the number of selected
nonliteral rank-four targets is `330-z4`.  Hence total interval slack is

```text
(N-n4)-(330-z4)=1+e4-x4.
```

Every nonempty component has positive slack.  Therefore

```text
0<=x4<=e4,
s3<=1+e4-x4.
```

The outer one-defect theorem permits only one physical triple of rank below
five.  Consequently a selected rank-four triple and a rank-at-most-three
triple carrier compete for one token:

```text
v4+w3<=1.
```

The number of nonliteral rank-at-most-three targets still needing pairs is

```text
231-[(N-n4)-Delta3]-w3.
```

The number of rank-four pair targets is

```text
330-z4-v4.
```

They inject into the `N-n4-s3` internal pairs of the lower components.
Expanding this inequality gives exactly

```text
Delta3+n4 <=369-2*n5-s3-x4+v4+w3.
```

Similarly, rank-four pair targets and outer rank-five pair targets inject
into the `N-1` pairs of the one-component core:

```text
y1+(330-z4-v4)<=N-1,
y1<=134-n5+z4+v4.
```

Thus the constants `369` and `134` are correct.

For the pointwise recursive omission row (5.39), the summed version (5.40)
is valid only for `0<=t<=10`.  At `t=11`, its left side is zero while its
unsubtracted `+1` term makes the right side positive.  This is a domain
correction, not an error in the collision row.

### 7.1 Top slices

At `n5=134`, total rank-four slack is one.  Hence `x4=0,s3=1`, and exact
rank-four rigidity gives

```text
C=P4 || D3 || Q4,
|D3|=331-n4,
n4<=100.
```

The nonliteral rank-four family has size `|D3|-1`.  In a segment of length
one more than the number of non-singleton incomparable witnesses, all
adjacent pairs must be selected: if `b` selected triples replaced pairs,
their two pair endpoints would lie in only `b` unselected pair vertices,
which cannot support `b` edges of a path.  Hence all pairs of `D3` are
distinct rank-four targets and every rank-at-most-three target is literal.
It follows that

```text
F=|D3|-231=100-n4.
```

Those `330-n4` rank-four pairs are disjoint from the `y1` rank-five pairs
among the 330 physical pairs of `C`, so

```text
y1<=n4.
```

The report's effective-carrier argument is also correct.  If `H` lies in
`D3`, it contains two distinct rank-four pair values, so its OR has rank at
least five.  If it meets `P4` or `Q4` and has rank at most four, its OR is
the literal rank-four value it contains and supplies no new target.
Therefore

```text
y2>=228+F=328-n4.
```

At `n5=133`, the three cases in Section 5.7 have the stated slacks:

```text
x4=1,s3=1: two-level slack 1,
x4=0,s3=2: each component has slack 1,
x4=0,s3=1: the component has slack 2.
```

In the first two cases every internal lower-component pair is selected at
rank four, which gives

```text
F=101-n4,
y1<=n4                 in the first case,
y1<=n4+1               in the second.
```

In the slack-two case, `v4` rank-four triples leave

```text
1+v4
```

internal pairs available for rank-at-most-three targets.  All internal
triples are selected at rank four or contain a selected rank-four pair, so
there is no additional lower-triple allowance.  Hence

```text
(332-n4)+(1+v4)>=231,
n4<=102+v4,
y1<=n4+1+v4.
```

The branch constants and the claim `v4<=1` are correct.

## 8. Chain B and the constant 367

In the duplicate-free two-component mode

```text
(delta_5,s)=(0,2),
```

there is exactly one nonempty internal diagonal singleton block.  Physical
reversal exchanges `11` and `22`, so one may orient it as a positive `22`
block.  The endpoint chain is then

```text
00,01,02,12,22,23,33.
```

The low component left of the `22` block has

```text
length   h4-h1+2,
witnesses h4-h1,
slack 2.
```

The right component has

```text
length   h6-h5+1,
witnesses h6-h5,
slack 1.
```

Thus the decomposition

```text
P5 || C2 || R5 || C1 || Q5
```

and the stated slack orientation are exact.  The left component's `01` and
`12` pair blocks together with its `02` triple block cover every internal
triple.  Every pair of the right component is a selected rank-five pair.
A triple crossing a component boundary contains a literal rank-five entry.
Therefore no rank-at-most-four target can use a triple anywhere in this
branch.

There are `N` low singleton cells but only

```text
(|C2|-1)+(|C1|-1)=N-2
```

internal low pair cells.  The number of nonliteral lower targets remains

```text
96+n5+Delta_lit.
```

Inject these targets and the `y1` selected rank-five pair targets into the
same physical pair pool:

```text
(96+n5+Delta_lit)+y1<=N-2=463-n5.
```

Rearranging gives

```text
y1+2*n5+Delta_lit<=367.                  (B)
```

Using `y1+y2=462-n5`, (B) is exactly

```text
y2>=95+n5+Delta_lit.
```

The constant is `367`, not `368`, because the separator removes one
additional low pair edge and there is no compensating carrier.

If equality holds, every internal pair not selected at rank five is used by
one nonliteral lower target.  This proves the equality statement following
(7.6a).

### 8.1 Two-component coordinate rows

Counting zero runs separately in two components gives

```text
2*Zb-Rb-ab   >=385,
2*ob+Rb-2-cb >=176.
```

Here `Rb>=1` and `Rb<=ob+2`.  Thus

```text
Zb>=193+ceil(ab/2),
ob>=ceil((176+cb)/3).
```

Summing gives exactly

```text
649+max(0,ceil((5*y1-11)/3))
 <=S
 <=11*N-2123-3*y1.
```

In the slack-one component of length `m`, every adjacent pair has rank five.
For one coordinate, its number of pair occurrences is
`o_b+R_b-1`; summing over coordinates yields

```text
5*(m-1)=S1+R1-11,
S1+R1=5*m+6.
```

The constant `6` is correct.  If this component is coordinate-complete then
`m>=4`: two positions have union rank five, and with three positions the
two adjacent rank-five unions share the nonempty middle entry, so their
total union has size at most nine.

### 8.2 Top chain-B slice

At `n5=134`, concatenate `C2` and `C1` across the deleted literal separator.
All original lower witnesses remain internal to one of the two pieces, so
the concatenated word still covers every mask through rank four.  Rank-four
rigidity gives

```text
Cstar=P4 || D3 || Q4,
|D3|=331-n4>=231.
```

The artificial seam cannot lie inside `D3`.  The `|D3|-1` original
nonliteral rank-four witnesses are forced to be every adjacent pair of
`D3`; a seam inside `D3` would require the nonexistent cross-component
pair.  Since every pair of `C1` is selected at rank five, `D3` cannot be
contained in `C1`.  Hence

```text
D3 subseteq C2.
```

It follows that `C2` is coordinate-complete and every entry of `C1` is a
distinct literal rank-four boundary entry.  Among the `N-2=329` original
internal low pairs, `330-n4` are selected at rank four.  Therefore

```text
m-1<=y1<=329-(330-n4)=n4-1<=99.
```

Also

```text
F=100-n4,
y2>=95+134+F=329-n4,
y1+y2=328.
```

Every constant in (7.7)--(7.10) is correct.

For smaller chain-B slices, the same slack calculation gives

```text
0<=x4<=134-n5,
1<=s3<=135-n5-x4.
```

There is no carrier, so the rank-four/lower collision row becomes

```text
Delta3+n4<=369-2*n5-s3-x4,
```

and outer rank-four/rank-five pair packing into `N-2` cells gives

```text
y1+(330-z4)<=N-2,
y1<=133-n5+z4.
```

The constants `369` and `133` are correct.  The summed moment associated
with (7.14), like (5.40), must be stated only for `0<=t<=10`.

## 9. Final theorem ledger

- **One-defect path lemma:** accepted.
- **Chain-A normalization:** accepted exactly under
  `(delta_5,s)=(0,1)`.
- **Named carrier `H`:** accepted, including all empty-block endpoints.
- **Chain-A collision row:** accepted with exact constant `368+v`.
- **Unconditional lower row:** accepted:
  `y2>=93+n5+Delta_lit`.
- **Weighted incidence row:** accepted with exact unconditional constant
  `1934`.
- **Coordinate occurrence and omission:** accepted with thresholds `59`
  and `193`.
- **Aggregate and all-codimension rows:** accepted, with the summed moments
  restricted to `t<=10`.
- **Nested rank-four rows:** accepted conditional on the cited earlier
  rigidity, surplus, shortening, and transversal theorems.
- **Equality skeleton:** accepted as a necessary labelled path template,
  not as an existence construction.
- **Chain-B orientation:** accepted exactly under
  `(delta_5,s)=(0,2)` and reversal.
- **Chain-B collision row:** accepted with exact constant `367`.
- **Duplicate branch:** correctly excluded; none of these chain-A/B
  normalizations is asserted for `(delta_5,s)=(1,1)`.
- **Recursive classifications:** accepted as lossless necessary data
  attached to every word, not as sufficient scalar characterizations.
- **Global scope:** no contradiction to a length-465 word is proved or
  claimed.
