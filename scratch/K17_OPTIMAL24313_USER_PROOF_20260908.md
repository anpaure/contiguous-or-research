## The exact case \(k=17\) is solved

$$
\boxed{\displaystyle \nu(17)=B(17)=24\,313.}
$$

I constructed an explicit **24,313-letter word covering all 131,071 nonempty subsets of \([17]\)** by ordinary, nonwrapping interval unions. Its length matches the rank-endpoint lower bound.

This removes the entire remaining **345-position gap** from the previous 24,658-letter construction. It closes the finite case that the handoff left unresolved. 

[Optimal 24,313-letter word](sandbox:/mnt/data/k17_exact_breakthrough/k17_optimal24313.word) · [Standalone verifier](sandbox:/mnt/data/k17_exact_breakthrough/verify.py) · [Full proof](sandbox:/mnt/data/k17_exact_breakthrough/EXACT_K17.md) · [Complete certificate package](sandbox:/mnt/data/k17_exact_breakthrough_complete.zip)

**The construction does not require merging everything into one cyclic component.** It produces two cycles with exactly \(W(17)\) total positions, then opens them with **one and two extra letters**. Their single join supplies the five targets absent from the separate linear blocks.

That is how it bypasses the previous cycle-fusion obstruction.

## 1. The lower bound: fewer than 24,313 positions are impossible

Put

$$
W=\binom{17}{9}=24\,310,
\qquad
\Lambda=\sum_{j=1}^{8}\binom{17}{j}=65\,535.
$$

Suppose a universal word has length \(W+t\). Choose one witness interval

$$
I_i=[\ell_i,r_i]
$$

for each of the \(W\) nine-element targets, ordered by left endpoint.

Two distinct equal-rank witnesses cannot contain one another: containment of intervals implies containment of their unions, and distinct nine-sets cannot contain one another. Thus both endpoint sequences are strictly increasing. Consequently,

$$
\ell_i=i+\alpha_i,\qquad r_i=i+\beta_i,
\qquad
0\le\alpha_i\le\beta_i\le t.
$$

Every interval \([a,a+t]\) contains \(I_a\). Therefore an interval representing a target of rank below nine must have length at most \(t\). There are only

$$
\sum_{j=1}^{t}(W+t-j+1)
=
tW+\binom{t+1}{2}
$$

such intervals.

For \(t\le2\), this is at most

$$
2W+3=48\,623<65\,535=\Lambda.
$$

So no word of length \(W+2\) or less is universal:

$$
\boxed{\nu(17)\ge W+3=24\,313.}
$$

This is the handoff’s rank-endpoint argument, reproduced here for the particular dimension. 

The new word attains it.

## 2. The construction starts with an exact-width two-cycle cover

The cyclic part consists of two genuine words of lengths

$$
\boxed{24\,225\quad\text{and}\quad85.}
$$

Their total length is

$$
24\,225+85=24\,310=W.
$$

Across these two cycles:

$$
\boxed{
\begin{aligned}
&\text{Every eight-set occurs exactly once as a three-letter union;}\\
&\text{every nine-set occurs exactly once as a four-letter union;}\\
&\text{every nonempty target at every rank occurs somewhere.}
\end{aligned}}
$$

The last assertion is checked separately; it is not inferred merely from middle-layer coverage.

### Construct the chronology before assigning the small targets

Let \(\rho\) rotate all seventeen coordinates. Each proper nonempty subset has seventeen distinct rotations, so each middle layer has

$$
\frac{24\,310}{17}=1\,430
$$

rotation classes.

The finite certificate supplies, for each index \(i\),

$$
L_i,\qquad b_i,\qquad (j_i,s_i),
$$

where \(L_i\) is an eight-set, \(b_i\notin L_i\) is one coordinate, and

$$
U_i=L_i\cup\{b_i\}.
$$

The certificate verifies that the \(L_i\)’s represent every eight-set rotation class and the \(U_i\)’s represent every nine-set rotation class. It also verifies that

$$
L_i\longmapsto \rho^{s_i}L_{j_i}
$$

is a bijective successor rule with

$$
\rho^{s_i}L_{j_i}\subset U_i,
\qquad
\rho^{s_i}L_{j_i}\ne L_i.
$$

Developing under all seventeen rotations gives an actual permutation of the entire eight-set layer. Its cycles—not a subsequently assumed ordering—supply the chronology.

The selected transitions also satisfy two temporal conditions: an inserted coordinate is not deleted on either of the next two transitions. All coordinate shifts are included in those checks.

For the resulting physical upper-owner sequence, form

$$
E_i=U_{i-3}\cap U_{i-2}\cap U_{i-1}\cap U_i.
$$

These envelope letters have size six. Their consecutive pair, triple, and four-letter unions have ranks seven, eight, and nine.

### Refine the letters without disturbing longer witnesses

Replace \(E_i\) by a nonempty subset \(A_i\subseteq E_i\), subject to

$$
\boxed{
A_i\cup A_{i+1}=E_i\cup E_{i+1}
\quad\text{at every cyclic adjacency}.
}
\tag{1}
$$

This preserves **every interval union of length at least two**. Indeed, any such interval is the union of its consecutive adjacent-pair unions.

The final assignment of the \(A_i\)’s contains every target of rank at most six as a literal letter. Their number is

$$
\sum_{r=1}^{6}\binom{17}{r}=21\,777,
$$

or 1,281 rotation classes.

Thus the lower-target assignment and the longer witnesses coexist in one actual word. There is no unresolved compatibility assumption between separately chosen witnesses.

The two cyclic target families have respectively

$$
130\,748\quad\text{and}\quad664
$$

members. Their union is exactly

$$
2^{[17]}\setminus\{\varnothing\}.
$$

The [construction certificate](sandbox:/mnt/data/k17_exact_breakthrough/construction_certificate.json.gz) records all 1,430 quotient rows, the refined letters, and the final opening choices.

## 3. The decisive join uses exactly three extra positions

Call the 85-letter cycle \(Q\) and the 24,225-letter cycle \(P\), using the canonical phases specified by the generator.

Rotate \(P\) so that its zero-based position \(15\,321\) comes first. Call that rotated word \(R\).

The final ordinary word is simply

$$
\boxed{
Q\;\Vert\;Q_0\;\Vert\;R\;\Vert\;R_0\;\Vert\;R_1.
}
\tag{2}
$$

Its length is

$$
\boxed{
85+1+24\,225+2=24\,313.
}
$$

There are no additional bridge letters or repair appendix.

Why are one and two copied letters sufficient, when opening the components separately would ordinarily require more? Because **the blocks are not required to preserve their cyclic target families separately**.

Let

$$
V=Q\Vert Q_0,\qquad
Z=R\Vert R_0\Vert R_1.
$$

The separate blocks have the following exact census:

| Block | Length | Targets covered internally |
| ----- | -----: | -------------------------: |
| \(V\) |     86 |                        639 |
| \(Z\) | 24,227 |                    130,747 |

Together, their internal witnesses cover **131,066 of the 131,071 targets**. The five missing masks are

$$
\boxed{
27299,\quad27303,\quad27315,\quad27319,\quad29363.
}
\tag{3}
$$

Their ranks are respectively

$$
8,\quad9,\quad9,\quad10,\quad9.
$$

All five are supplied by the single join.

### A six-letter certificate for the join

The last three letters of \(V\) and the first three of \(Z\) are

$$
\boxed{
(19076,\;19106,\;8834\mid25249,\;689,\;12849).
}
\tag{4}
$$

The vertical separator marks the block boundary. As throughout the certificate, bit \(j\) represents coordinate \(j+1\).

Number these six letters locally from 1 to 6. Then:

| Missing target | Rank | Witness among the six letters |
| -------------: | ---: | :---------------------------: |
|          27299 |    8 |           \([2,4]\)           |
|          27303 |    9 |           \([1,4]\)           |
|          27315 |    9 |           \([2,5]\)           |
|          27319 |   10 |           \([1,5]\)           |
|          29363 |    9 |           \([3,6]\)           |

For example,

$$
19106\mathbin{\mathrm{OR}}8834
\mathbin{\mathrm{OR}}25249
=
27299,
$$

and

$$
8834\mathbin{\mathrm{OR}}25249
\mathbin{\mathrm{OR}}689
\mathbin{\mathrm{OR}}12849
=
29363.
$$

Every listed interval crosses the join and is an ordinary contiguous interval. Every other target already has an internal witness in \(V\) or \(Z\), which concatenation cannot destroy.

Therefore

$$
\boxed{
\operatorname{Cov}(V\Vert Z)
=
2^{[17]}\setminus\{\varnothing\}.
}
$$

This is the exact upper-bound proof: the two finite internal censuses plus the five displayed cross-boundary identities.

[Five-target seam certificate](sandbox:/mnt/data/k17_exact_breakthrough/seam_certificate.json)

## 4. The middle-layer capacity is saturated exactly

The final word has a particularly clean structure:

| Window length | Ranks of all such unions | Distinct targets obtained |
| ------------: | ------------------------ | ------------------------: |
|             1 | 1 through 6              |                    21,777 |
|             2 | Always 7                 |                    19,448 |
|             3 | Always 8                 |                    24,310 |
|             4 | Always 9                 |                    24,310 |
|             5 | Always 10                |                    19,448 |

In particular, there are exactly

$$
24\,313-4+1=24\,310
$$

four-letter windows, and they enumerate **all nine-sets exactly once**.

The first three endpoints have no nine-set suffix union. Every subsequent endpoint introduces a fresh nine-set, reached at recency depth four.

So the three-position excess is not hiding wasted middle-layer occurrences:

$$
\boxed{
\text{three initial positions}
\;+\;
\text{one new nine-set at every remaining endpoint}.
}
$$

Higher ranks are included in the complete interval enumeration; their coverage is not assumed from the short-window table.

## 5. Verification was performed independently of the search

The optimality claim does **not** depend on a solver certifying its own objective.

The delivered word was checked in three ways.

**Exact suffix-union enumeration.** At each endpoint, the verifier applies

$$
\mathcal R_j
=
\{A_j\}\cup
\{A_j\cup S:S\in\mathcal R_{j-1}\}.
$$

Induction identifies this with every nonempty suffix union ending at \(j\). A nonwrapping interval is recorded for every target.

**Direct forward enumeration.** A separate scan starts at every left endpoint and accumulates ORs as the right endpoint advances. It stops only after obtaining the full set, because every subsequent extension has that same union. This independently checked **552,396 intervals** and found every nonempty target.

**Independent range-OR checks.** A segment tree built directly from the letters rechecked all **131,071 recorded witness intervals**.

The executed result is:

```text
Word length:                         24,313
Rank-endpoint lower bound:           24,313
Required nonempty targets:          131,071
Targets covered:                    131,071
Missing targets:                          0
Direct forward intervals checked:   552,396
Range-OR witnesses checked:          131,071
All letters nonempty:                   yes
All witnesses nonwrapping:              yes
```

[Executed verification log](sandbox:/mnt/data/k17_exact_breakthrough/verification.log) · [All target witnesses](sandbox:/mnt/data/k17_exact_breakthrough/all_target_witnesses.json.gz)

The word’s SHA-256 is:

```text
7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9
```

To verify the result after extracting the package:

```bash
python verify.py
```

To regenerate the word from the quotient certificate and check the structural construction:

```bash
python generate.py --output regenerated.word
python verify.py regenerated.word
python verify_structure.py
```

All three programs use only the Python standard library. The regenerated word was compared **byte for byte** with the delivered word.

## 6. What changed structurally

The previous searches tried to shorten an already completed word, or to fuse a fixed inventory of native states. Both approaches had stalled.

The successful construction changed the recurrent middle-layer matching itself. A global search reduced the missing target classes, and a finite feasibility model supplied fourteen successor changes that completed the required adjacent layers while retaining the temporal exclusions. The resulting data were then checked directly for **all** higher ranks, including those not explicitly constrained by that model.

The lower compiler subsequently filled every rank-one-through-six target class while preserving equation (1).

Finally, the opening search did **not** insist on making each component independently complete. It assigned the three extra positions across the two components and let the join take responsibility for the five remaining targets.

The resulting mechanism is

$$
\boxed{
\begin{gathered}
\text{an exact-width recurrent two-cycle cover}\\
+\ \text{pair-union-preserving lower assignment}\\
+\ \text{a jointly chosen three-position opening}\\
=\ \text{an optimal ordinary word}.
\end{gathered}}
$$

No theorem about universally fusing PBBS cycles was needed. Nor was a universal cyclic word of period \(W(17)\) needed.

## Scope of the breakthrough

This is an **exact finite result**, independent of the proposed asymptotic coefficient-one manuscript and its clock, renewal, and support arguments. That manuscript concerns a limiting ratio; the present proof consists of an explicit finite word, exhaustive integer checks, and a matching analytic lower bound. 

Combining this result with the handoff’s previously established values, the bound \(B(k)\) is now attained through **dimension 17**.  It does not yet prove \(\nu(k)=B(k)\) for every dimension.

But the finite gap we have been attacking is completely closed:

$$
\boxed{\displaystyle
24\,658
\quad\longrightarrow\quad
24\,313
=
B(17)
=
\nu(17).
}
$$
