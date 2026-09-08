# Audit of the corrected terminal-sector fusion boundary

Date: 2026-07-25

Pure mathematics only. No computation, finite search, or external input is
used.

Audited file:
`MATH_ATTACK_K_RPA_RETRACTED_SECTOR_FUSION_BOUNDARY_20260725.md`.

## Verdict

**Pass after one substantive scope correction and minor notation patches.**

The protected-spine iff criterion, the protected return theorem, the exact
product enumeration, the stretched-exponential estimate, the deck
normalization, and the primitive endpoint counterexample are correct.

The initial version of Section 7 treated the zero-winding family
\(\mathcal Z_{r,s}\) as if it exhausted all short returns. That implication
was too strong: an actual short return may satisfy

\[
 \sum_{j<s}d_j=\delta_s+aN
\]

with \(a>0\). The report has been patched to use the full congruence family
\(\mathcal R_{r,s}\), including all earlier odd and even nonreturn
conditions, and the exact residence cutoff \(s\le H-1\). With that patch,
the implication to \((\mathrm{RP}_A)\) is correct.

## 1. Protected-spine criterion

At formal time \(j\), the transported arrays are

\[
 \widehat A_i^{(j)}=
 \begin{cases}
 B_{j-1-i},&i<j,\\
 A_{i-j},&i\ge j,
 \end{cases}
 \qquad
 \widehat B_i^{(j)}=B_{i+j}
\]

when the displayed index exists. The necessity argument is exact:

- at \(j=h-1-k\), an original \(A_k\) occupies the last pre-spine slot,
  so full canonicality forces \(A_k=\varnothing\);
- at \(j=h\), an original \(B_t\) occupies pre-spine depth \(h-1-t\),
  so strict first-deepest canonicity forces
  \(\operatorname{ht}(B_t)\le t\).

Conversely, these inequalities imply that every transported pre-spine
forest has total height at most

\[
 i+\operatorname{ht}(B_{j-1-i})\le j-1<h,
\]

while the original attachment bound controls every post-spine forest.
Thus the criterion is genuinely necessary and sufficient for the stated
full formal itinerary. It is not asserted to classify all actual returns.

The audit added the convention that the empty forest has height zero and
fixed one malformed attachment-depth parenthesis.

## 2. Return calculation

On the protected class, with forest size measured in edges,

\[
 C_j=j+2\sum_{t<j}|B_t|,
 \qquad
 \delta(D_j)=h+2\sum_{t<j}|B_t|.
\]

Hence \(\delta(D_j)-C_j=h-j\), and

\[
 C_h=h+2\sum_t|B_t|=2r-h<2r+1=N.
\]

Both sides of every proper odd comparison lie in \([0,N)\), so the strict
literal difference excludes a congruence. Also
\(0<C_j<C_h<N\) excludes every proper positive even return. Equality at
\(j=h\) gives the first zero-winding return at gap \(2h+1\). No modulus,
factor-two, or endpoint-index error remains.

## 3. Enumeration and constants

The exact protected-root form is

\[
 1^h0B_{h-1}0B_{h-2}\cdots0B_1 0,
 \qquad
 \operatorname{ht}(B_k)\le\min(k,h-k),
\]

which gives

\[
 p_{r,h}=[z^{r-h}]
 \prod_{k=1}^{h-1}C_{\min(k,h-k)}(z).
\]

For the aggregate bound, the two independent relaxations are valid:

\[
 p_{r,h}\le
 4^r\exp\!\left(-{\pi^2r\over(h+2)^2}\right)
\]

and

\[
 {p_{r,h}\over B_r}
 \le(r+1)2^{-h}.
\]

Splitting at \(h=\lfloor r^{1/3}\rfloor\) yields

\[
 |\mathcal P_r|\le C B_r e^{-c r^{1/3}}
\]

after absorbing polynomial factors into a smaller absolute exponential
constant. The displayed product ratio in the prefix estimate has the
correct orientation; every factor \((r-a)/(2r-a)\) is at most \(1/2\).

## 4. Physical deck and repair normalization

Each quotient root has at most \(N\) spatial lifts. Therefore even charging
every protected lift separately gives

\[
 {O(H^2)N|\mathcal P_r|\over W}
 =O(H^2){|\mathcal P_r|\over B_r}.
\]

For \(H=O(\sqrt r)\), this is

\[
 O\!\left(r e^{-c r^{1/3}}\right)=o(1).
\]

The factors \(N\), \(B_r\), and \(W=NB_r\) therefore cancel exactly as
claimed. The report's wording was narrowed: the conclusion applies to
repairs or modifications confined to the protected occurrences; it does
not rule out a nonlocal braid which merely uses a protected root as an
anchor and changes macroscopic support elsewhere.

## 5. Counterexample and implication boundary

For \(D_0=1110011000\), the exact orbit data are

\[
 (\delta,d)=(3,1),(3,5),(7,1),
 \qquad \tau^3D_0=D_0.
\]

Thus the alleged gap-seven endpoint label is

\[
 u-(1+5+1)+3=u-4\not\equiv u\pmod {11}.
\]

The report also correctly checks that the first actual return is at gap
thirteen. Coordinate conjugation preserves the inequality of the two
failed ports, so this is a literal obstruction to the proposed
all-primitive static-sector identification.

After the Section 7 patch, the exact remaining target is all actual return
solutions \(\mathcal R_{r,s}\), not merely zero-winding solutions. For a
residence cutoff \(H\), the correct index range is \(0\le s\le H-1\),
because gap \(2s+1\) has projected residence \(s+1\). The long-cycle
packing target \(o_A(B_r/N)\), together with the already proved negligible
short-cycle term, is exactly the quotient form needed for \((RP_A)\).

No claim that \((RP_A)\) is true or false remains. No global dynamic-spine
braid is ruled out. The report proves only the exact static-sector boundary,
its negligible protected mass, and the failed literal ports outside it.
