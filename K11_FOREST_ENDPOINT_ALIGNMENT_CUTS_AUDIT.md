# Independent audit of the `k=11` endpoint-alignment cuts

## Verdict

The four proposed inequalities are **proved and globally WLOG** for the
current unrestricted nonzero `k=11,n=465` forest formula:

\[
\begin{aligned}
 \sum_{p=0}^{464} Z^{L}_{324}(p)&\ge324,&
 \sum_{p=0}^{464} Z^{R}_{324}(p)&\ge324,\\
 \sum_{p=0}^{464} Z^{L}_{24}(p)&\ge24,&
 \sum_{p=0}^{464} Z^{R}_{24}(p)&\ge24.
\end{aligned}
\]

Here `Z324` means that a selected rank-five witness of width one or two and a
selected rank-six witness of width two or three share the indicated endpoint;
`Z24` means that widths two and three, respectively, share it.

The numbers `324` and `24` are guaranteed lower bounds, not assertions that
the intersections have exactly those sizes.  They are sharp using only the
four endpoint-set cardinalities.  No full OR array attaining either bound is
claimed.

Two implementation qualifications are required:

1. the new option must either require the existing adjacent-shadow option or
   independently allocate its exact rank-six `B/E` endpoint summaries;
2. each population counter has **465 inputs**.  The audited nine-bit increment
   gadget for 462 inputs can be reused as a template, but it must be
   instantiated for 465 steps and separately for each counted predicate.

Subject to these qualifications, I found no counterexample or hidden
fixed-row, connected-path, or witness-selection assumption.

## 1. Endpoint injectivity

Choose one nonempty witnessing interval for every target in each rank under
discussion.  Within a fixed rank, selected left endpoints are distinct.
Indeed, two intervals with the same left endpoint are nested, so their OR
masks are comparable.  Distinct masks of equal rank are incomparable.  The
same argument applies to right endpoints.

Consequently the selected endpoint set in rank `s` has size

\[
 m_s={11\choose s}.
\]

For ranks three through six these sizes are

\[
 m_3=165,\qquad m_4=330,\qquad m_5=m_6=462.
\]

All endpoint sets are subsets of the same 465 physical positions.  This is
true at both ends; no cyclic endpoint or wraparound convention is present.

## 2. Independent reconstruction of the counts

For subsets `S_1,...,S_t` of a universe of size `n`, complement union-bound
gives

\[
 \left|\bigcap_{j=1}^{t}S_j\right|
 \ge n-\sum_{j=1}^{t}(n-|S_j|)
 =\sum_{j=1}^{t}|S_j|-(t-1)n.                 \tag{1}
\]

Apply (1) to the selected left-endpoint sets in ranks four, five, and six:

\[
 |L_4\cap L_5\cap L_6|
 \ge330+462+462-2\cdot465=324.                \tag{2}
\]

Adding rank three gives

\[
 |L_3\cap L_4\cap L_5\cap L_6|
 \ge165+330+462+462-3\cdot465=24.             \tag{3}
\]

Replacing every `L_s` by the corresponding `R_s` proves the identical two
right-endpoint bounds.  There is no correlation assumption between the
independently selected witness families.

The arithmetic can also be read through omitted positions.  Relative to the
465-position universe, the deficits of ranks `3,4,5,6` are

\[
 300,135,3,3.
\]

Thus the three-rank common set omits at most `135+3+3=141` positions, leaving
324, while the four-rank common set omits at most
`300+135+3+3=441`, leaving 24.

These set-theoretic bounds are sharp: disjoint omitted sets of sizes
`135,3,3` leave 324 common positions, and disjoint omitted sets of sizes
`300,135,3,3` leave 24.  This sharpness statement concerns only endpoint-set
cardinalities.

## 3. Nesting and the rank-six width cap

Write interval width as `right-left`, so a singleton has width zero.

If intervals of ranks `a<b` share a left endpoint, the rank-`a` interval must
be a proper prefix of the rank-`b` interval.  Equality would give one physical
interval two different OR values.  Reverse containment would make the
rank-`b` mask a subset of the rank-`a` mask, impossible because `b>a`.
Therefore their widths strictly increase with rank.  At a common right
endpoint the lower-rank interval is analogously a proper suffix, and widths
again strictly increase with rank.

It remains to verify the largest possible width.  Sort the 462 selected
rank-six intervals by left endpoint and index them `i=0,...,461`.  Equal-rank
incomparability makes both endpoint lists strictly increasing.  Each is a
462-element subset of 465 positions, hence

\[
 i\le \ell_i\le r_i\le i+3.
\]

Every selected rank-six witness therefore has width at most three.

At a common endpoint in (2), the integer widths obey

\[
 0\le w_4<w_5<w_6\le3.
\]

The four possible triples are

```text
(0,1,2), (0,1,3), (0,2,3), (1,2,3).
```

Thus every one of the at least 324 positions has

\[
 w_5\in\{1,2\},\qquad w_6\in\{2,3\}.           \tag{4}
\]

At a common endpoint in (3), four strictly increasing nonnegative integers
fit below three.  The unique possibility is

\[
 (w_3,w_4,w_5,w_6)=(0,1,2,3).                  \tag{5}
\]

This proves all proposed width implications at both endpoint colours.

For completeness, every selected rank-five witness has width at most two.
Any physical interval of length at least four contains one selected rank-six
interval: if it starts at `a`, then `a<=461` and the rank-six interval indexed
by `a` lies inside `[a,a+3]`.  Such a physical interval has OR rank at least
six, so it cannot witness a rank-five mask.  This justifies defining
`L5pos/R5pos` using precisely widths one and two.

## 4. Why projecting away ranks three and four is WLOG

Fix any actual universal array and any rank-five and rank-six witness families
represented by the two exact central schedules.  Independently choose one
witness for every rank-three and rank-four mask.  Equations (2)--(5) then
force the four inequalities using only the already fixed rank-five/rank-six
physical endpoints and widths.

Therefore the rank-three and rank-four schedules need not be variables in the
CNF.  Their existence in the underlying universal array implies a necessary
property of every possible pair of selected central schedules.  The argument
does not choose a specially favourable central row and does not require either
central endpoint forest to be connected.

This projection remains valid when ranks three and four are represented by
the audited shadow compressions rather than by direct target blocks.  It would
cease to be justified only if a future central relaxation stopped representing
an exact one-witness-per-mask rank-five/rank-six family.

## 5. Exact implementation-safe definitions

Use physical positions `p=0,...,464`.  Let the ten central states have offsets
`(alpha_u,beta_u)`, and write `S5[i,u]` for the exact-one rank-five state at
slot `i`.

Define the following support sets of existing state literals:

\[
\begin{aligned}
 \mathcal L_{5,+}(p)
  &=\{S5[i,u]:i+\alpha_u=p,
                    \ \beta_u-\alpha_u\in\{1,2\}\},\\
 \mathcal R_{5,+}(p)
  &=\{S5[i,u]:i+\beta_u=p,
                    \ \beta_u-\alpha_u\in\{1,2\}\},\\
 \mathcal L_{5,2}(p)
  &=\{S5[i,u]:i+\alpha_u=p,
                    \ \beta_u-\alpha_u=2\},\\
 \mathcal R_{5,2}(p)
  &=\{S5[i,u]:i+\beta_u=p,
                    \ \beta_u-\alpha_u=2\}.
\end{aligned}
\]

For a summary `V <-> OR(z in S) z`, emit

```text
(-z OR V)                    for every support literal z,
(-V OR z_1 OR ... OR z_t).
```

If the support is empty, the second clause is the unit `-V`.  Instantiate
this for `L5pos,R5pos,L52,R52` with the four support sets above.  The current
rank-five width-three prohibition makes this exhaustive.

Reuse the already exact rank-six summaries

```text
B6[p,d] iff the selected rank-six interval starting at p has width d,
E6[p,d] iff the selected rank-six interval ending   at p has width d,
```

for `0<=d<=3`.  In the current source these exist only under the adjacent-
shadow option, so the endpoint-alignment option must depend on that option or
allocate the same bidirectional summaries itself.

Now define, exactly,

```text
ZL324[p] <-> L5pos[p] AND (B6[p,2] OR B6[p,3]),
ZR324[p] <-> R5pos[p] AND (E6[p,2] OR E6[p,3]),
ZL24[p]  <-> L52[p]   AND B6[p,3],
ZR24[p]  <-> R52[p]   AND E6[p,3].
```

For example, `Z <-> L AND (B2 OR B3)` is encoded exactly by

```text
(-Z OR L)
(-Z OR B2 OR B3)
(-L OR -B2 OR Z)
(-L OR -B3 OR Z).
```

The two-input `Z <-> L AND B3` uses the usual three clauses.  These reverse
implications are essential: one-sided flags would let the counter undercount
real alignments and would not prove the lower bounds.

## 6. Counters and boundary conventions

Each sum ranges over all 465 ordinary linear positions.  There is no sentinel
position and no identification of positions zero and 464.  Existing central
state supports automatically make geometrically impossible endpoint/width
summaries false near the boundary.

Use four separate exact 465-step counters, or another independently audited
exact cardinality encoding.  Nine output bits suffice because

\[
 0\le\sum_{p=0}^{464}Z(p)\le465<512=2^9.
\]

With the XOR/carry increment template, initialize all nine bits to zero,
process every Boolean input once, and compare the final unsigned value with
324 or 24 as appropriate.  There is no modular overflow.  Calling these
“exact cardinality cuts” should mean exact encodings of `sum>=threshold`, not
equalities `sum=threshold`.

## 7. Soundness and completeness of the proposed option

* **Completeness relative to genuine arrays.**  Sections 1--4 prove that every
  universal length-465 array, for every choice of its exact central witness
  schedules, satisfies all four comparisons.  Enabling them removes no
  genuine optimum.
* **Soundness relative to the base formula.**  The new clauses only restrict
  existing exact schedule states and functionally determined auxiliaries.
  They cannot create a spurious array model.  The base formula's existing
  soundness proof is unchanged.

Hence the guarded extension is satisfiable if and only if the unrestricted
base formula is satisfiable, provided the exact definitions and guard
dependency in Section 5 are followed.

## 8. Independent arithmetic checker

`scratch/verify_k11_endpoint_alignment.cpp` independently checks:

* all four binomial coefficients;
* both inclusion-exclusion bounds and their set-theoretic sharpness;
* all possible strict width triples and quadruples below the width-three cap;
* the truth table of the four-clause `Z324` equivalence;
* nine-bit nonoverflow for 465 inputs.

Compiled with `-O3 -std=c++20`, it reports:

```text
m3=165 m4=330 m5=462 m6=462
triple_endpoint_lower_bound=324 four_endpoint_lower_bound=24
triple_width_patterns=4 quadruple_width_patterns=1
k11_endpoint_alignment=PASS
```

This checker is a regression aid; the proof above is independent of it.
