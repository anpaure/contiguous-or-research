# Independent audit: nonsaturated endpoint-fork stability

Date: 2026-07-24

Audited source: `NONSATURATED_ENDPOINT_FORK_STABILITY.md`.

No search result, certificate, or finite feasibility enumeration was used. All finite values below were recomputed from binomial coefficients and the defining closed rank-count inequality for `tau`.

## Overall verdict

The endpoint-fork, filtration, width-three, rainbow-run, and critical-flag theorems are mathematically valid. Every displayed finite number is correct. No inequality, sign, or numerical constant needs to be changed.

The source needs the following exact corrections or clarifications.

1. State the natural domains `m>=1`, `1<=s<=ell<=k`, and, in the critical-flag theorem, `d>=0` and `1<=a=r-d`.
2. All filtration statements use one fixed initial witness selection and its one fork forest; witnesses may not be reselected separately for different coordinate restrictions.
3. Section 4 inherits the exact-length, active-upper-middle-rank, and rank-cap hypotheses of Section 3. It should explicitly prove or cite both parts of the standard interval-band lemma: upper-middle witnesses have length at most four, and every lower target has a witness of length at most three.
4. “Fork runs” in the summed rainbow deduction means maximal consecutive runs of fork positions.
5. The inequalities in (5.1) are summed consequences of the pointwise subcube inequalities, not equivalent to them. The per-coordinate `199+h` conclusion comes from the pointwise ten-coordinate statement, not from the first aggregate inequality alone.
6. The `421` conclusion controls rank-five **base masks** omitting a coordinate. It does not show that the complete pair/triple labels of each corresponding diamond omit that coordinate.

These corrections do not weaken any structural theorem or any displayed scalar bound.

## 1. Endpoint injections and the double fork

### Equal-rank endpoint injection

Selected witnesses for distinct masks of one rank form a physical interval antichain. If two shared a left endpoint or a right endpoint, one interval would contain the other. OR monotonicity and equal target cardinality would then force equal masks, contradicting the fixed one-witness-per-mask selection.

Thus each selected rank layer has distinct left endpoints and distinct right endpoints.

For the two middle layers, all four endpoint sets have size

\[
M=\binom{2m+1}{m}=\binom{2m+1}{m+1}
\]

inside `n=M+d` positions. Hence

\[
|L_m\cap L_{m+1}|\ge2M-n=M-d,
\]

and similarly for right endpoints. A second inclusion--exclusion gives

\[
|C|\ge2(M-d)-(M+d)=M-3d.
\]

**Verdict on Lemma 2.1:** **VALID.** The constants `M-d,M-d,M-3d` are exact inclusion--exclusion bounds.

### Nesting and mixed-singleton exclusion

At a common left endpoint, the rank-`m` and rank-`m+1` intervals are nested. The higher-rank interval cannot be contained in or equal to the lower-rank interval, so

\[
I_p^+\subsetneq J_p^+.
\]

The same argument at a common right endpoint gives

\[
I_p^-\subsetneq J_p^-.
\]

If exactly one of `I_p^-,I_p^+` were `[p,p]`, its value `A_p` would be contained in the other rank-`m` OR. Equal cardinality would force equal masks, giving two different selected intervals for one mask. Thus the mixed case is impossible.

If both lower intervals are nonsingletons, they meet physically only at `p`, have distinct rank-`m` masks, and satisfy

\[
A_p\subseteq U(I_p^-)\cap U(I_p^+),
\qquad |A_p|\le m-1.
\]

No Johnson adjacency and no equality between `A_p` and the mask intersection is used.

**Verdict on Lemma 2.2:** **VALID.**

### Double-fork count

Every position of `C` that is not a double fork is the common singleton case and therefore carries an entry of rank exactly `m`. Consequently

\[
|F|\ge |C|-z_m\ge M-3d-z_m.
\]

Under the rank cap,

\[
n=p+z_m+h=M+d,
\]

so

\[
|F|\ge p+h-4d,
\qquad
p-|F|\le4d-h.
\]

Because `F` is contained in the low-position set, these inequalities also imply `h<=4d`; the exceptional bound `4d-h` is therefore automatically nonnegative whenever a word exists.

**Verdict on Theorem 2.3:** **VALID.** Here `p,z_m,h` count physical positions, not distinct values.

### Fork path forest

Each selected rank-`m` interval has one left and one right endpoint, so the directed fork graph has indegree and outdegree at most one. If an edge at junction `p` is followed by another edge, the common intermediate interval starts at `p`, is nonsingleton, and ends at a strictly larger junction `q`. Junction positions strictly increase along directed walks, excluding cycles.

Different fork centres give different edges because the right endpoint of the source interval recovers the centre. Hence the graph is a directed linear forest with exactly `|F|` edges and

\[
M-|F|
\]

components, isolated vertices included.

**Verdict on Theorem 2.4:** **VALID.**

## 2. Rank and coordinate filtrations

### Scope correction

The phrase “the upper middle rank attains the bound” must mean

\[
B(k)=b_{m+1}(k)
=\binom{k}{m+1}+\tau(k,m+1)
=M+d.
\]

Thus `d=tau(k,m+1)`, and exact rank truncation forces every entry to have rank at most `m+1`.

All restrictions below refer to the same preselected witnesses and the same resulting forest `F`. Reselecting witnesses for each `Y` would not prove simultaneous coordinate-sensitive stability.

### Coordinate restriction

The precise domain is

\[
1\le s\le\ell\le k,
\qquad Y\in\binom{[k]}\ell.
\]

For a target `T subseteq Y`, `|T|<=s`, every entry in any witness for `T` is a nonempty subset of `T`. Thus every position of that witness remains after deleting positions outside `P_s(Y)`. Since no position internal to the witness is deleted, its entries remain consecutive in the compressed word.

The retained word therefore covers the punctured ideal through rank `s` on `Y`. Applying the rank-count theorem at each `1<=t<=s` gives

\[
|P_s(Y)|\ge
\max_{1\le t\le s}
\left[\binom\ell t+\tau(\ell,t)\right]
=\beta_s(\ell).
\]

**Verdict on Lemma 3.1:** **VALID AFTER DOMAIN CLARIFICATION.**

### Lower fork incidence

Let

\[
E_{\rm low}=\{i:|A_i|\le m-1\}\setminus F.
\]

The double-fork theorem gives

\[
|E_{\rm low}|\le4d-h.
\]

Since `P_s(Y)` consists only of low positions,

\[
|F_s(Y)|
\ge\beta_s(\ell)-(4d-h).
\]

Taking `Y=[k]` gives the correct `+h` sign. Summing over all `ell`-sets counts a centre of entry rank `r` exactly

\[
\binom{k-r}{\ell-r}
\]

times and yields

\[
\sum_{\substack{i\in F\\|A_i|\le s}}
\binom{k-|A_i|}{\ell-|A_i|}
\ge
\binom{k}{\ell}
[\beta_s(\ell)-4d+h]_+.
\]

**Verdict on Theorem 3.2:** **VALID.** The prose “almost its full quota” can be vacuous when `beta_s(ell)<=4d-h`; the formula itself is exact.

### Upper incidence from acyclicity

For a fixed `q`-set `Q`, every fork centre with `Q subseteq A_i` gives an edge whose two endpoint rank-`m` masks contain `Q`. These edges lie in the induced subforest on

\[
\binom{k-q}{m-q}
\]

vertices, so there are at most one fewer edges:

\[
\#\{i\in F:Q\subseteq A_i\}
\le\binom{k-q}{m-q}-1.
\]

Summing over all `Q` counts centre `i` exactly `C(|A_i|,q)` times.

**Verdict on Theorem 3.3:** **VALID.** No connectivity assumption on the induced subforest is needed.

## 3. Width-three overlap law

Section 4 inherits `d=3`, exact upper-middle activity, and the rank cap.

### Lengths two or three

Order the `M` selected rank-`m+1` intervals by left endpoint:

\[
\ell_1<\cdots<\ell_M.
\]

Equal-rank noncontainment forces their right endpoints to have the same strict order. In `n=M+3` positions,

\[
\ell_i\ge i,
\qquad
r_i\le n-(M-i)=i+3.
\]

Thus every selected upper-middle witness has length at most four. A double-fork rank-`m` side is nonsingleton and is a proper same-endpoint subinterval of such a witness, so its length lies in `{2,3}`.

This derivation should be included or cited explicitly.

### Forbidden mixed widths

For centres `p<q`, the facing intervals are

\[
[p,p+\lambda_p^+-1],
\qquad
[q-\lambda_q^-+1,q].
\]

If `q=p+1`, either mixed pair `(2,3)` or `(3,2)` gives proper containment. If `q=p+2`, either mixed pair again gives proper containment. Proper containment of two selected equal-rank intervals is impossible. Hence

\[
\lambda_p^+=\lambda_q^-
\]

at both distances.

The equal cases are consistent: at distance one the `(2,2)` intervals coincide and the `(3,3)` intervals cross; at distance two the `(3,3)` intervals coincide and the `(2,2)` intervals meet in one position.

Applying distances one, one, and two to three consecutive forks gives all four equalities in (4.2).

**Verdict on Theorem 4.1 and Corollary 4.2:** **VALID.** No boundary exception occurs because the fork intervals themselves certify that their endpoints lie in the word.

## 4. Short-band charge and rainbow runs

### Exact residual `sigma`

The standard interval-band lemma also says that every target below the active rank `m+1` has a witness of length at most `d=3`. Here is the needed derivation. If a physical interval `J` has length `d+1`, then there are only `M-1` positions outside it: its number of positions strictly to the left plus its number strictly to the right is `M-1`. If none of the `M` selected active-rank intervals were contained in `J`, each would have either its distinct left endpoint to the left of `J` or its distinct right endpoint to the right of `J`. Those endpoint injections would place `M` intervals into only `M-1` available outside positions, a contradiction. Thus every `(d+1)`-cell contains a selected active-rank witness. A witness for a strictly lower-rank target cannot contain such a witness, so it has length at most `d`.

This fact is used essentially in Theorem 4.3 and should be added to the final list of established inputs.

The length-one/two/three band contains

\[
n+(n-1)+(n-2)=3(M+3)-3=3M+6
\]

physical cells. The number of nonempty masks through rank `m` is

\[
\sum_{j=1}^{m}\binom{2m+1}{j}=2^{2m}-1.
\]

Choosing one distinct short cell for each such mask leaves exactly

\[
\sigma=3M+7-2^{2m}
\]

unused cells. Existence of the assumed word ensures `sigma>=0`.

### Type-`(2,2)` injection

At a type-`(2,2)` centre `p`, the two rank-`m` selected pair values on `[p-1,p]` and `[p,p+1]` are distinct. Their union, the OR of `[p-1,p+1]`, therefore has rank at least `m+1`. Its triple cell cannot be one of the selected lower-mask cells.

Different centres give different triple cells, so

\[
\#\{(2,2)\text{ centres}\}\le\sigma.
\]

It is irrelevant whether an unused cell has another lower witness elsewhere; only physical-cell capacity is being charged.

**Verdict on the first part of Theorem 4.3:** **VALID.**

### Three-fork windows

Let the maximal consecutive runs of `F` have lengths `t_j`, and let their number be `g`. Then

\[
T_3(F)=\sum_j(t_j-2)_+
\ge |F|-2g.
\]

Since a path with `n-|F|` nonfork positions has at most `n-|F|+1` nonempty fork runs,

\[
T_3(F)\ge[3|F|-2n-2]_+.
\]

Every such window has a distinct middle centre, which Corollary 4.2 makes type `(2,2)` or `(3,3)`. Globally at most `sigma` are type `(2,2)`, hence

\[
\#\{(3,3)\text{ run interiors}\}
\ge[3|F|-2n-2-\sigma]_+.
\]

The `-2` is the correct path-boundary term.

### Homogeneous runs and Johnson segments

For a consecutive fork run, distance-one equality gives

\[
\lambda_i^+=\lambda_{i+1}^-,
\]

while distance two, combined with the next distance-one equality, gives

\[
\lambda_i^+=\lambda_{i+2}^-=\lambda_{i+1}^+.
\]

Thus all used internal values share one `epsilon in {2,3}`; only the two unused outer-facing lengths may differ.

If `epsilon=3`, the outgoing lower interval at `i` is `[i,i+2]`. Its proper same-left upper witness has length exactly four and is `[i,i+3]`. Therefore

\[
T_i=U([i,i+2]),
\qquad
Q_i=U([i,i+3])
\]

are selected masks, with

\[
Q_i=T_i\cup T_{i+1},
\qquad
|T_i\cap T_{i+1}|=m-1.
\]

Selected same-rank uniqueness makes all `T_i` and all `Q_i` globally distinct. A maximal epsilon-three run of length `t` contributes exactly `t-2` Johnson edges, one per type-`(3,3)` interior. There is no double counting across maximal runs.

**Verdict on Theorems 4.3--4.4 and the rainbow deduction:** **VALID**, with “runs” clarified as maximal in the summed statement.

## 5. Formula-only audit of the odd finite consequences

The defining arithmetic is

\[
\tau(k,s)=\min\left\{t\ge0:
\sum_{j=1}^{s-1}\binom{k}{j}
\le t\binom{k}{s}+\binom{t+1}{2}\right\},
\]

and

\[
\beta_s(k)=\max_{1\le t\le s}
\left[\binom{k}{t}+\tau(k,t)\right].
\]

Direct evaluation gives

\[
\begin{array}{c|c|c}
k&\beta_{m-1}(k)&\beta_{m-1}(k)-12\\ \hline
11&331&319\\
13&1288&1276\\
15&5006&4994\\
17&19450&19438\\
19&75584&75572.
\end{array}
\]

Thus the fork lower bounds `319+h,1276+h,4994+h,19438+h,75572+h` are correct.

At `k=11`,

\[
\beta_2(11)=56,
\quad
\beta_3(11)=166,
\quad
\beta_4(11)=331,
\]

giving exactly `44+h,154+h,319+h` after subtracting `12-h`.

For the coordinate restrictions,

\[
\beta_4(10)=211,
\quad
\beta_4(9)=128,
\quad
\beta_4(8)=72,
\quad
\beta_4(7)=37,
\]

so every corresponding subcube contains at least

\[
199+h,quad116+h,quad60+h,quad25+h
\]

fork centres of the specified kind.

Summing these pointwise inequalities gives

\[
\begin{aligned}
\sum_{i\in F}(11-|A_i|)&\ge2189+11h,\\
\sum_{i\in F}\binom{11-|A_i|}{2}&\ge6380+55h,\\
\sum_{i\in F}\binom{11-|A_i|}{3}&\ge9900+165h,\\
\sum_{i\in F}\binom{11-|A_i|}{4}&\ge8250+330h.
\end{aligned}
\]

These are consequences, not equivalents: summation loses the individual subcube inequalities. In particular, the statement that at least `199+h` centres omit each prescribed coordinate follows from (3.2) with \(Y=[11]\setminus\{x\}\), not from the first aggregate inequality alone.

For the five odd dimensions, the exact residuals and consequences are

\[
\begin{array}{c|r|r|r}
k&\sigma&[|F|-\sigma]_+&[3|F|-2n-2-\sigma]_+\\ \hline
11&369&0&0\\
13&1059&217+h&0\\
15&2928&2066+h&0\\
17&7401&12037+h&2285+3h\\
19&14997&60575+h&26955+3h.
\end{array}
\]

Every entry agrees with the source.

For each `k=11,13,15,17,19`, the upper-middle rank has `B(k)=M+3`, while the lower-middle record is `M+2`. Exact rank truncation therefore gives

\[
h\le1.
\]

No external finite data is used in these calculations.

## 6. Critical flags

### Domain and intersection theorem

State the natural domain

\[
d\ge0,
\qquad
1\le a=r-d\le r\le k.
\]

For each selected rank `j`, the endpoint set has size `M_j=C(k,j)` in an `n`-position universe. The complement union bound gives

\[
\left|\bigcap_{j=a}^{r}L_j\right|
\ge
\sum_{j=a}^{r}M_j-dn
=\Lambda,
\]

and identically for right endpoints.

At a common endpoint, increasing target rank forces strict physical nesting. The selected rank-`r` interval has length at most

\[
n-M_r+1=d+1.
\]

There are `d+1` distinct positive integer lengths, so they are exactly

\[
1,2,\ldots,d+1.
\]

Both flag endpoint sets lie in the same set of at most `M_a` selected rank-`a` singleton positions. Hence their intersection has size at least

\[
[2\Lambda-M_a]_+.
\]

**Verdict on Theorem 6.1:** **VALID AFTER DOMAIN CLARIFICATION.**

### The `k=14` values

Formula-only evaluation gives the complete rank-count list

\[
14,92,365,1002,2003,3005,3434,3007,2009,1016,406,202,182,181,
\]

so `B(14)=3434` is uniquely attained at rank seven.

With

\[
M_5=2002,
\quad M_6=3003,
\quad M_7=3432,
\]

one obtains

\[
\Lambda=2002+3003+3432-2(3434)=1569
\]

and

\[
2\Lambda-M_5=1136.
\]

At such a two-sided centre, the two rank-six pair labels are `S union {x}` and `S union {y}`. The physical pair intervals are distinct members of one fixed selected rank-six family, so their masks are distinct and `x!=y`. Their centered triple has rank seven. The rank-five bases are distinct.

The coordinate calculation is

\[
\#\{\text{bases contained in }Y\}
\ge
[\binom{|Y|}{5}-866]_+.
\]

For `|Y|=13`, this is

\[
\binom{13}{5}-866=1287-866=421.
\]

This proves that at least `421` double-diamond **bases** omit each prescribed coordinate. It does not prove that the added pair/triple coordinates also omit it. The unqualified phrase “421 double diamonds omit each coordinate” should be replaced by the base-mask statement.

For a consecutive run of double-diamond centres, the shared pair interval gives

\[
B_i=S_i\cup S_{i+1}=U([i,i+1]),
\]

and overlapping pairs give

\[
Q_i=B_i\cup B_{i+1}=U([i,i+2]).
\]

Selected same-rank uniqueness makes the `B_i,Q_i` distinct, and consecutive bases are Johnson adjacent. The count `1136` alone does not force adjacency because a path on `3434` positions has an independent set of size `1717`.

**Verdict on Corollary 6.2 and its run deductions:** **VALID**, with the base-mask wording correction.

### Odd full-flag values

Applying the same formula to ranks `m-2,m-1,m,m+1` gives

\[
\begin{array}{c|r|r}
k&\Lambda&[2\Lambda-M_{m-2}]_+\\ \hline
15&1564&125\\
17&7505&2634\\
19&33583&16778.
\end{array}
\]

The corresponding values at `k=11,13` are nonpositive, so “positive from `k=15` onward” is exact.

## 7. Unsupported overreadings

The audit confirms that the source does not prove, and should not be read as proving, any of the following:

- that a generic fork entry equals the entire intersection of its endpoint masks;
- that adjacent generic fork masks are Johnson adjacent outside the homogeneous length-three runs;
- that the fork forest itself covers all lower masks or that its hulls cover all upper masks;
- that the incidence inequalities are sufficient for factorization by one OR word;
- that the displayed finite necessary conditions are infeasible;
- that `1136` diamonds force a collision or even an adjacent pair;
- that a base omitting a coordinate forces the complete diamond to omit it.

The OPEN statements in Section 7 remain open and are not used by any proved consequence.

## Final ledger

### Valid

- Endpoint injections and the `M-d,M-d,M-3d` intersection counts.
- Nesting, mixed-singleton exclusion, and double-fork bounds.
- The directed fork path forest and its exact component count.
- Pointwise and summed lower filtration inequalities.
- Upper rank/coordinate incidence from forest acyclicity.
- The forbidden mixed `2/3` overlap theorem.
- The `sigma` short-band injection and all run-window bounds.
- Homogeneous fork runs and rainbow Johnson segments.
- The two-sided critical-flag intersection theorem.
- Every displayed finite scalar and table entry.

### Corrected or clarified

- Add the positive parameter domains and active-rank meaning.
- Keep one fixed witness selection throughout all restrictions.
- Supply the upper-witness and lower-short-witness interval-band derivations.
- Interpret summed fork runs as maximal runs.
- Replace “equivalently” before (5.1) by “summing these pointwise inequalities gives.”
- Attribute the per-coordinate `199+h` claim to the pointwise theorem.
- Replace “421 diamonds omit a coordinate” by “421 diamond bases omit a coordinate.”
- Add the lower-mask short-witness lemma to the final list of established inputs.

### Unsupported

Only the stronger readings listed in Section 7 are unsupported. No stated theorem or finite numeric bound is false.

With these corrections, the source is a sound finite-math stability theorem and changes no equality or nonexistence result by itself.
