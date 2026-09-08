# Independent audit of `FAN_CAPPED_AVOIDANCE.md`

## 1. Verdict

The central result is correct.

In particular, after independently rederiving the endpoint fans, the exact
identity at the selected right endpoints, the capped heterogeneous run
cover, and every displayed three-box count, I certify

\[
 |\mathcal F|
 \le \sum_{t=1}^N\min(A_t,h)
 \le \sum_{i=1}^M\min(w_i,h)+hD.
\]

There is no off-by-one error in `A_t`, `w_i`, or `lambda_i=v_i-u_i`.
The use of the slab height is valid, including the choice `h=2a` in the
nested-order application.  The exact nested-order consequence

\[
 D\ge {17\over30}a^2+{4\over5}a+{1\over30}
\]

is arithmetically and combinatorially correct.

The three-box consequences in Sections 5--7 also follow from the audited
lemmas, with their stated architectural hypotheses.  Two of them are genuine
new corollaries of combining the old geometric run assignments with the new
fan cap: the earlier source audits stated their conclusions only in the
surface-error regime because the old avoidance ledger contained `O(D^2)`.
The new proof legitimately removes that restriction; it should be described
as a new deduction from audited ingredients, rather than as a conclusion
already stated in the older audit.

No displayed inequality needs a numerical correction.  I recommend only the
scope and exposition repairs listed in Section 9 below.

## 2. Audit map

| Source portion | Verdict | Independent check |
|---|---|---|
| Section 1, (1.1) | Correct | Endpoint-chain capacity and the exact selected-fan identity give the two inequalities. |
| Section 1, (1.2) | Correct | Follows by applying `min(x+y,h)<=min(x,h)+y` to the audited heterogeneous run inequalities. |
| Section 1, (1.3) | Correct | The `h=2a` slab, nested run ledger, two congestion bounds, and one omitted index give exactly the displayed polynomial. |
| Section 2, formula for `A_t` | Correct | If `j=max{i:r_i<=t}`, avoidance is exactly `x>ell_j`, giving `A_t=t-ell_j`. |
| Section 2, (2.2)--(2.3) | Correct | At `t=r_i`, one has `j=i`, hence `A_(r_i)=r_i-ell_i=w_i`; there are exactly `D=N-M` unselected endpoints. |
| Section 2, sharpness | Correct but terse | An explicit height-`h` family is supplied in Section 3 of this audit. |
| Section 3, (3.2) | Correct | These are exactly the two audited one-sided run inequalities; internality of `[u_i,v_i]` is required. |
| Section 3, (3.3) | Correct | Congestion counts adjacent offset increments, whose total variations are at most `D`. |
| Section 4, (4.1) | Correct | The middle coefficient of `(1+x+...+x^(2a))^3` is `3a^2+3a+1`. |
| Section 4, (4.3) | Correct for its stated range `1<=h<=a` | Rank `3a-q` has size `M_a-q^2`; summing `q=1,...,h` gives the formula. |
| Section 4, (4.4) | Correct | It is the full nonzero lower half minus ranks `1,...,a-1`. |
| Section 4, (4.5) | Correct | It equals `((2a+1)^3-M_a)/2-1`. |
| Section 4, (4.6) | Correct | The slab has chain height at most `h`, and a below-middle witness cannot contain a selected middle witness. |
| Section 5, (5.1) | Correct | It uses the sharper estimate explicitly certified in `THREE_BOX_INTERLEAVING_OBSTRUCTION_AUDIT.md`. |
| Section 5, (5.2)--(5.3) | Correct | Adding the fan term `(3a-1)D` changes `2H+3a+3` to `2H+6a+2`. |
| Section 5, asymptotics | Correct with scope qualification | They concern the induced selected-middle order; the random-order assertion is high-probability conditional on that order being uniform. |
| Section 6, (6.1) | Correct | The audit certifies `|J|=M_a-1`, sum `lambda=a^3-a`, `C_alpha<=2a`, `C_beta<=a`, and `lambda<=a-1`. |
| Section 6, (6.2)--(6.3) | Correct | The omitted center costs `2a`; the fan costs `2aD`; the two congestion terms cost `3aD`. |
| Section 7, complete rings | Correct under the stated ring-order and `O(a)` auxiliary-occurrence hypotheses | The old geometric assignment is independent of the size of `D`; the new cap upgrades its conclusion to `D=Omega(a^2)`. |
| Section 7, side batches | Correct when `B` counts maximal intact side-homogeneous batches and the center is split off as in the audit | The constants `13` and `24` are valid safe roundings. |
| Section 7, reusable criterion | Correct | Assuming `D=o(a^2)` makes every term other than the clipped run budget `o(a^3)`, contradicting the fixed positive cubic gap. |
| Section 8 | Correct | It accurately states that this is not a general three-box impossibility theorem. |

## 3. Independent proof of the fan identity

Let

\[
 I_i=[\ell_i,r_i],\qquad
 \ell_1<\cdots<\ell_M,\quad
 r_1<\cdots<r_M.
\]

The strict increase of both endpoint sequences follows from incomparability
of the selected antichain targets.  Equal left endpoints, equal right
endpoints, or an inversion of the right endpoints would make one selected
interval contain another, and hence make their two OR targets comparable.

Fix a physical right endpoint `t`.

If no `r_i` is at most `t`, then no interval ending at `t` can contain a
selected interval, so all `t` choices of its left endpoint are avoiding:

\[
 A_t=t.
\]

Otherwise let

\[
                         j=\max\{i:r_i\le t\}.
\]

An interval `[x,t]` contains at least one selected interval if and only if

\[
 x\le\max_{i\le j}\ell_i=\ell_j.
\]

Therefore the avoiding left endpoints are exactly

\[
                         x=\ell_j+1,\ldots,t,
\]

and

\[
                         A_t=t-\ell_j.                 \tag{3.1}
\]

This settles both possible off-by-one conventions.  In particular, the
nonavoiding interval beginning at `ell_j` is deliberately excluded.  At a
selected endpoint `t=r_i`, strict increase of the `r` sequence gives `j=i`,
so

\[
                         A_{r_i}=r_i-\ell_i=w_i.       \tag{3.2}
\]

There are exactly `M` selected right endpoints in `[N]`, hence exactly
`N-M=D` unselected ones.  Splitting the sum over these two kinds of endpoint
gives the exact identity

\[
 \sum_{t=1}^N\min(A_t,h)
 =\sum_{i=1}^M\min(w_i,h)
  +\sum_{t\notin\{r_1,\ldots,r_M\}}\min(A_t,h).       \tag{3.3}
\]

The last sum is at most `hD`.

At a fixed `t`, the ORs of `[x,t]` form a weak inclusion chain as `x`
moves left.  Thus they contain at most `h` distinct targets from a family of
chain height `h`.  They also use at most `A_t` avoiding physical intervals.
This proves the first inequality and completes the theorem.

The same argument proves the left-endpoint version.  At `x=ell_i`, the
avoiding right endpoints are precisely `ell_i,...,r_i-1`, again a set of
size `w_i`.

### Sharpness detail omitted from the source

The source's general-`h` sharpness sentence is correct, but an explicit
family makes it clearer.  Take distinct singleton word entries and select
only `I_1=[N,N]`.  Among the first `D=N-1` positions, let `mathcal F` consist
of all contiguous singleton sets of lengths at most `h`:

\[
 \{\{x,x+1,\ldots,t\}:1\le x\le t\le D,
                         \ t-x+1\le h\}.
\]

Its chain height is at most `h`, every member has its displayed avoiding
witness, and its size is

\[
 \sum_{t=1}^D\min(t,h)
 =hD-{h(h-1)\over2}\qquad(D\ge h).
\]

Thus no coefficient smaller than one can uniformly replace the coefficient
of `hD`.

## 4. Independent proof of the clipped run cover

For an assigned index before its run, the audited pin inequality gives

\[
 w_i\le \lambda_i+\alpha_{v_i+1}-\alpha_i,
 \qquad i<u_i.
\]

For an assigned index after its run, it gives

\[
 w_i\le \lambda_i+\beta_i-\beta_{u_i-1},
 \qquad i>v_i.
\]

Here an internal run has `2<=u_i<=v_i<=M-1`, and

\[
 \lambda_i=v_i-u_i
\]

is one less than the number of run positions.  This convention exactly
matches the pin inequality and the nested-order count; replacing it by the
number of vertices would introduce an erroneous `|J|` term, but the source
does not make that error.

For nonnegative `x,y`,

\[
                 \min(x+y,h)\le\min(x,h)+y.
\]

The offset differences above are nonnegative by monotonicity.  After
expanding them into adjacent increments, each `alpha` increment is used at
most `C_alpha` times and each `beta` increment at most `C_beta` times.  Since

\[
 \alpha_M-\alpha_1\le D,
 \qquad
 \beta_M-\beta_1\le D,
\]

their total charges are at most `C_alpha D` and `C_beta D`.  An unassigned
index costs at most `h`.  Hence

\[
 \sum_i\min(w_i,h)
 \le
 \sum_{i\in J}\min(\lambda_i,h)
 +(C_\alpha+C_\beta)D+(M-|J|)h.
\]

Adding the endpoint-fan term `hD` proves (1.2).  There is no hidden fixed-row
assumption: the only band input is the unrestricted endpoint normal form for
the selected antichain witnesses.

## 5. Three-box rank arithmetic

For `P_a=[0,2a]^3`, the rank-generating polynomial is

\[
                         (1+x+\cdots+x^{2a})^3.
\]

For `0<=q<=a`, inclusion-exclusion gives

\[
\begin{aligned}
 [x^{3a-q}](1+x+\cdots+x^{2a})^3
 &= {3a-q+2\choose2}-3{a-q+1\choose2}\\
 &=3a^2+3a+1-q^2\\
 &=M_a-q^2.
\end{aligned}
\]

The slab `3a-h<=rho<=3a-1` corresponds to `q=1,...,h`, so for `h<=a`,

\[
 L_h(a)=hM_a-\sum_{q=1}^h q^2
       =hM_a-{h(h+1)(2h+1)\over6}.
\]

The full nonzero lower half is

\[
\begin{aligned}
 V_a
 &=\frac{(2a+1)^3-M_a}{2}-1\\
 &=4a^3+\frac92a^2+\frac32a-1.
\end{aligned}
\]

The `h=2a` slab contains ranks `a,...,3a-1`.  The discarded nonzero ranks
`1,...,a-1` have total size

\[
                         {a+2\choose3}-1,
\]

because the coordinate upper bounds are inactive there.  Therefore

\[
\begin{aligned}
 L_{2a}(a)
 &=V_a-\left({a+2\choose3}-1\right)\\
 &=\frac{23}{6}a^3+4a^2+\frac76a.
\end{aligned}
\]

This calculation does not misuse (4.3), whose stated range ends at `h=a`.
Also `2a<=3a-1` for every `a>=1`, so the slab itself is valid.  Its chain
height is at most `2a`, since it occupies exactly `2a` consecutive ranks.

## 6. The anti-mixing constants

The sharper estimate proved in
`THREE_BOX_INTERLEAVING_OBSTRUCTION_AUDIT.md` is

\[
 \sum_iw_i\le aM_a+2HD+3(a+1)D.                    \tag{6.1}
\]

Using the full lower family with height `3a-1` gives

\[
\begin{aligned}
 V_a
 &\le\sum_i\min(w_i,3a-1)+(3a-1)D\\
 &\le aM_a+2HD+3(a+1)D+(3a-1)D\\
 &=aM_a+(2H+6a+2)D.
\end{aligned}
\]

The potentially suspicious constant `+2` is therefore correct: the audited
sharper width estimate has `2HD`, not the older relaxed `2(H+1)D`.
Subtracting

\[
 aM_a=3a^3+3a^2+a
\]

from `V_a` gives

\[
 V_a-aM_a=a^3+\frac32a^2+\frac12a-1,
\]

which proves (5.3).  The three asymptotic consequences follow immediately.

For the random-order statement, the cited audit proves
`H=O(a log a)` with high probability for a uniformly random permutation of
the selected middle targets.  Substitution now gives
`D=Omega(a^2/log a)`.  This is not a statement that an arbitrary universal
word induces a uniformly random order.

## 7. The nested-order calculation

The phase-separation audit certifies

\[
 |J|=M_a-1,
 \qquad
 \sum_{i\in J}\lambda_i=a^3-a,
 \qquad
 C_\alpha+C_\beta\le3a,
 \qquad
 \lambda_i\le a-1.
\]

At cap `h=2a`, clipping changes none of the assigned run costs.  The one
unassigned index costs `2a`; the two congestion charges cost `3aD`; and the
endpoint fan costs another `2aD`.  Thus

\[
\begin{aligned}
 L_{2a}(a)
 &\le(a^3-a)+3aD+2a+2aD\\
 &=a^3+a+5aD.
\end{aligned}
\]

Consequently

\[
\begin{aligned}
 5aD
 &\ge {17\over6}a^3+4a^2+{1\over6}a,\\
 D
 &\ge {17\over30}a^2+{4\over5}a+{1\over30}.
\end{aligned}
\]

Every term, including the constant `1/30`, is correct.

## 8. Audit of the remaining three-box corollaries

### 8.1 Contiguous complete rings

The spiral-band audit supplies, for the complete-ring selected-witness
order with at most `O(a)` auxiliary occurrences:

* an internal run assignment for all but `O(a)` selected indices;
* assigned `lambda_i<=a+O(1)` after charging any inserted run extensions;
* total assigned run cost at most `3a^3+O(a^2)`; and
* one-sided span, hence charge congestion, `O(a)`.

These geometric facts do not require `D=O(a)`.  The old paper imposed that
condition only when combining them with its `O(D^2)` avoidance estimate.
Applying the new capped theorem with `h=3a-1` instead gives

\[
 V_a\le3a^3+O(a^2+aD).
\]

Since `V_a=4a^3+O(a^2)`, this implies `D=Omega(a^2)`.

This extension is sound, but its scope must remain exactly that of the
geometric run certificate: contiguous complete ring blocks (arbitrary ring
permutation, reversal, and corner cut are allowed), at most `O(a)` auxiliary
occurrences, and the selected middle-witness order inherited from that row.
It says nothing about genuine interleaving of arcs from different radii.

### 8.2 Side-batched orders

The repaired phase-separation audit gives

\[
 \sum_{i\in J}\lambda_i\le3a^3+O(a^2),
 \qquad C_\alpha+C_\beta\le10a,
 \qquad M_a-|J|\le8aB+O(a).
\]

The congestion constant uses the audited one-sided span `5a`; each of the
two offset sequences then has congestion at most `5a`.

At height `3a-1`, (1.2) gives

\[
\begin{aligned}
 V_a
 &\le3a^3+O(a^2)+10aD\\
 &\quad +(8aB+O(a))(3a-1)+(3a-1)D\\
 &\le3a^3+13aD+24a^2B+O(a^2).
\end{aligned}
\]

After subtracting the leading `3a^3`, this is exactly

\[
                         13D+24aB\ge a^2-O(a).
\]

Here `B` must count maximal side-homogeneous batches of intact half-open side
blocks after deleting the center.  If the center splits a batch, the two
pieces are treated as separate local batches, changing the ledger by only
the audited `O(a)` margin.  Without these definitions, the claimed
interpretation in terms of genuine side changes would not follow; with them,
it does.

### 8.3 General criterion

Let `h=Theta(a)` and assume the hypotheses in (7.4).  If, toward a
contradiction, `D=o(a^2)`, then

\[
 (C_\alpha+C_\beta)D+hD=o(a^3)
\]

and

\[
                         (M_a-|J|)h=o(a^3).
\]

The right side of (1.2) is therefore at most
`(c+o(1))a^3`, whereas the chosen slab has at least
`(c+epsilon)a^3` targets.  Quantitatively, for all sufficiently large `a`,
half of this fixed cubic gap must be supplied by `O(aD)`, yielding
`D=Omega(a^2)`.  The conclusion is valid as written.

## 9. Required and recommended source edits

No formula needs replacement.  The following wording changes would make the
paper fully self-contained and prevent overreading.

1. In Theorem 1, state `h>=1` when `mathcal F` is nonempty, and say explicitly
   that targets are distinct elements of the ambient inclusion-ordered join
   semilattice.  The empty-family case is vacuous.
2. Expand the general-`h` sharpness sentence using the length-at-most-`h`
   interval family in Section 3 of this audit.
3. In Lemma 2, repeat the internality condition
   `2<=u_i<=v_i<=M-1`; it is currently inherited through the citation.
4. In Section 5, qualify “random-order consequence” as a statement about a
   uniformly random induced selected-middle permutation.
5. In the complete-ring corollary, say that the `D=Omega(a^2)` statement is a
   new application of the old audited geometric run assignment.  The older
   theorem itself assumed surface error because it used the uncapped ledger.
6. Retain explicitly all complete-ring scope conditions: contiguous complete
   rings, the inherited witness order, and only `O(a)` auxiliary occurrences.
7. In the side-batch corollary, repeat that `B` counts maximal batches of
   intact designated half-open blocks after the center repair.  This is needed
   only for the “genuine switches” interpretation, not for the algebra once
   the repaired run ledger is assumed.

## 10. Final certified statement

Subject only to those clarifications, `FAN_CAPPED_AVOIDANCE.md` is
mathematically sound.  Its genuinely new proved contribution is the removal
of the quadratic endpoint-gap correction for bounded-height target families:

\[
 \boxed{
 |\mathcal F|
 \le\sum_i\min(w_i,h)+hD.}
\]

Together with the already audited heterogeneous run assignments, this
correctly upgrades the nested phase, contiguous-ring, and side-batched
three-box obstructions from surface-error statements to the stronger
quadratic-slack conclusions recorded in the source.  It remains an
architectural obstruction, not a proof of the general Boolean-array
conjecture or of a general three-box lower bound.
