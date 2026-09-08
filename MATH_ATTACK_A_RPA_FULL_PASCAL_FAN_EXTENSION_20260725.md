# RP_A: full-depth Pascal-fan fibre capacity and the parity-wrap audit

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
computation is used.

## 0. Result

Assume the audited tight-return Pascal fan of Theorem 5.1 in
`MATH_ATTACK_W_RPA_DYCK_PERIOD_FIBRE_PASCAL_FAN_20260725.md`.
Write

\[
 r_j=\frac12|\partial^jD|,
 \qquad
 \ell=\min\{j:r_j=h-j\},
\]

where the original zero-winding return has height (h).  The proposed
parity argument

\[
 \text{odd same-label gaps}
 \Longrightarrow
 \ell+1\text{ distinct terminal fan labels}
\]

is invalid.  Oddness holds for **consecutive** occurrences.  Two later
fan starts with the same label can be separated by two odd same-label
gaps and hence by an even time difference.

There is nevertheless an unconditional stronger counting statement.  At
inverse level (j), for every (1\le j\le\ell), the fan fixes

\[
 \boxed{t_j=\min\{j,2r_j\}}
\]

independent weak-composition degrees to prescribed nonnegative values.
Consequently, for every realizable rank profile, the complete inverse
tower has capacity factor at most

\[
 \boxed{
 \widehat Q_\ell(\mathbf r)
 =\prod_{j=1}^{\ell}
 \frac{
  \binom{r_{j-1}+r_{j+1}-t_j}{,2r_j-t_j,}
 }{
  \binom{r_{j-1}+r_{j+1}}{,2r_j,}
 } .}
 \tag{0.1}
\]

Thus Theorem 6.2 extends through the full mountain depth, but after a
cyclic wrap its correct assertion is not “(j) distinct slots.”  It is
“all available composition degrees are fixed.”

This does not prove \(\mathrm{RP}_A\).  In particular, when the residual
mountain rank (q=h-\ell) is bounded, the final saturated factor below
can remain a positive constant.

## 1. Exact audit of the terminal fan labels

At mountain depth put

\[
 q=h-\ell,
 \qquad
 p=2r_\ell+1=2q+1.
\]

The level-(\ell) fan consists of

\[
 I_{\ell,a}=[2a,2a+p],
 \qquad 0\le a\le\ell.
 \tag{1.1}
\]

Let \(\alpha_a\) be its equality-particle label.  Consecutive-fan-label
transport gives

\[
 \alpha_{a+1}=\alpha_a-1\pmod p,
\]

and hence

\[
 \boxed{\alpha_a=\alpha_0-a\pmod p.}
 \tag{1.2}
\]

It follows exactly that

\[
 \boxed{
 |\{\alpha_0,\ldots,\alpha_\ell\}|
 =\min\{\ell+1,p\}.}
 \tag{1.3}
\]

Suppose (a+p\le\ell).  Then \(\alpha_{a+p}=\alpha_a\), while the two
fan starts differ by (2p), an even number.  This does not contradict
the odd-gap theorem.  Indeed (1.1) already displays the intervening
occurrence of the same label at time (2a+p):

\[
 2a\longrightarrow 2a+p\longrightarrow 2a+2p,
\]

The first arrow is a consecutive gap equal to the odd number (p).
Between (2a+p) and (2a+2p) there may or may not be further occurrences;
their consecutive odd gaps have total (p), so their number is odd.  Thus
the complete separation (2p) is the sum of an even number of odd gaps,
exactly as parity permits.  The proposed inference confuses consecutive
with arbitrary same-label occurrences.

If one had an independent proof that the labels in (1.3) were distinct,
then the remaining algebra would be correct:

\[
 \ell+1\le2(h-\ell)+1
 \quad\Longleftrightarrow\quad
 3\ell\le2h.
 \tag{1.4}
\]

No such independent proof is supplied by oddness.  Accordingly, (1.4)
does not currently establish the universal bound

\[
 \ell\le\lfloor2h/3\rfloor.
\]

The present argument neither proves that bound nor constructs a genuine
zero-winding tower violating it; it removes the bound from the capacity
theorem altogether.

## 2. The full-depth slot theorem

### Theorem 2.1 (wrapped Pascal-fan inverse capacity)

Let (D) start a genuine zero-winding return of height (h), and retain
the notation above.  For every (1\le j\le\ell), put

\[
 p_j=2r_j+1,
 \qquad
 t_j=\min\{j,p_j-1\}=\min\{j,2r_j\}.
 \tag{2.1}
\]

At inverse level (j), the fan fixes (t_j) independent free child-slot
variables to prescribed nonnegative integral values.  For a fixed
realizable profile (r_0,\ldots,r_{\ell+1}) and a fixed bottom core, the
number of compatible inverse towers is at most the product of the
unrestricted conditional fibre capacities multiplied by (0.1).

#### Proof

The inverse expansion from (D^{(j)}) to (D^{(j-1)}) is a weak
composition of

\[
 y_j=r_{j-1}-2r_j+r_{j+1}\ge0
 \tag{2.2}
\]

into the (p_j=2r_j+1) cyclic child slots.  Its unrestricted cardinality
is

\[
 \binom{y_j+p_j-1}{p_j-1}
 =\binom{r_{j-1}+r_{j+1}}{2r_j}.
 \tag{2.3}
\]

The (j) fan intervals at level (j-1) yield, exactly as in the proof of
Theorem 6.2, the terminal-gap equations indexed by the consecutive cyclic
slot labels

\[
 i_0,i_0-1,\ldots,i_0-j+1\pmod {p_j}.
 \tag{2.4}
\]

There are \(\min\{j,p_j\}\) distinct labels in (2.4).  Select any

\[
 t_j=\min\{j,p_j-1\}
\]

of them.  Transport to a common phase has the exact form

\[
 \Delta_i(t)=1+\varepsilon_i+2z_i+n_i(t)-n_{i-1}(t).
 \tag{2.5}
\]

The reduced core determines \(\varepsilon_i,n_i(t),n_{i-1}(t)\).
Therefore each selected equation \(\Delta_i(t)=1\) fixes the corresponding
initial composition variable (z_i) to one integer.  Distinct slot labels
give distinct variables.  Since an outer fan is assumed to exist, every
prescribed value used by that tower is nonnegative.  If a slot label wraps
and occurs again, discard the repeated equation; it cannot increase the
number of compatible compositions.

If the (t_j) prescribed values have total (w\ge0), the number of
remaining compositions is

\[
 \binom{y_j-w+p_j-t_j-1}{p_j-t_j-1}
 \le
 \binom{y_j+p_j-t_j-1}{p_j-t_j-1}.
 \tag{2.6}
\]

Using (p_j-1=2r_j), the last member is

\[
 \binom{r_{j-1}+r_{j+1}-t_j}{2r_j-t_j}.
 \tag{2.7}
\]

This includes (t_j=p_j-1): after (p_j-1) coordinates of a weak
composition and its total are fixed, the last coordinate is determined,
and (2.7) equals (1).  Dividing (2.7) by (2.3), then conditioning and
multiplying from one inverse level to the next, proves (0.1). \(\square\)

Equivalently, every level factor is

\[
 \boxed{
 \frac{
  \binom{r_{j-1}+r_{j+1}-t_j}{2r_j-t_j}
 }{
  \binom{r_{j-1}+r_{j+1}}{2r_j}
 }
 =\prod_{i=0}^{t_j-1}
   \frac{2r_j-i}{r_{j-1}+r_{j+1}-i}.}
 \tag{2.8}
\]

## 3. Quantitative consequences

### 3.1 Unconditional extension to two-thirds depth

For every (j\le\lfloor2h/3\rfloor),

\[
 2r_j\ge2(h-j)\ge j.
\]

Hence (t_j=j).  The original formula (6.2) is therefore valid
unconditionally with

\[
 k=\min\{\ell,\lfloor2h/3\rfloor\},
 \tag{3.1}
\]

not merely (k\le\lfloor h/2\rfloor).  This improvement needs no claim
about distinct terminal labels at level \(\ell\).

If a separate theorem did prove \(\ell\le2h/3\), then (0.1) would reduce
to the proposed factor

\[
 Q_\ell(\mathbf r)
 =\prod_{j=1}^{\ell}
 \frac{
  \binom{r_{j-1}+r_{j+1}-j}{2r_j-j}
 }{
  \binom{r_{j-1}+r_{j+1}}{2r_j}
 }.
 \tag{3.2}
\]

On the same formal harmonic profile used in Proposition 6.3, with rank
scale tending to infinity for fixed \(\ell\),

\[
 Q_\ell\longrightarrow
 \frac{(\ell+2)^\ell}{(\ell+1)^{\ell+1}}
 \sim\frac e\ell.
 \tag{3.3}
\]

Thus moving the cutoff from (h/2) to its largest proposed value
(2h/3) improves the critical harmonic constant by a factor (3/4); it
does not change the (1/h) order.

### 3.2 The wrapped final fibre is saturated

At the mountain level put (q=h-\ell), and assume (\ell\ge1) (as is
automatic in the saturated regime considered below).  Since

\[
 r_\ell=q,
 \qquad
 r_{\ell+1}=q-1,
\]

and \(\ell\) is the first mountain level,

\[
 r_{\ell-1}\ge q+2.
\]

Therefore

\[
 y_\ell
 =r_{\ell-1}-2q+(q-1)
 =r_{\ell-1}-q-1
 \ge1.
 \tag{3.4}
\]

If

\[
 \ell\ge2q
 \quad\Longleftrightarrow\quad
 \ell\ge2h/3,
\]

then (t_\ell=2q), so all weak-composition degrees in the last inverse
fibre are fixed.  Its exact capacity ratio is at most

\[
 \boxed{
 \frac1{\binom{2q+y_\ell}{2q}}
 \le\frac1{2q+1}.}
 \tag{3.5}
\]

Thus the range in which the proposed distinctness argument could fail is
not a loss of fibre information: cyclic wrapping saturates the final
fibre.  This gives an additional vanishing factor whenever

\[
 q=h-\ell\longrightarrow\infty.
\]

It does not give a vanishing factor when (q=O(1)), and hence does not by
itself close the Catalan packing estimate.

## 4. Adversarial audit and exact boundary

1. Oddness is used only for consecutive same-label occurrences.  No
   statement about arbitrary pairwise time differences is made.

2. The label circle at inverse level (j) has (p_j=2r_j+1) slots.  The
   fan supplies (j) equations, not (j+1); the latter is the number of
   descendant return labels delimiting those equations.

3. A weak composition into (p_j) parts has only (p_j-1) independent
   degrees after the total is fixed.  This is why (t_j) is capped at
   (2r_j=p_j-1), not at (p_j).

4. Repeated phase equations may impose additional compatibility, but
   discarding them is legitimate for an upper bound.  Their possible
   dependence cannot invalidate (0.1).

5. The nonnegativity of prescribed values is not asserted for an arbitrary
   core.  It follows conditionally for every compatible outer tower being
   counted; incompatible cores contribute zero.

6. Formula (3.3) has the same fixed-depth-then-large-rank interpretation as
   the original harmonic audit.  It is not a uniform growing-depth
   asymptotic for all realizable profiles.

The remaining problem after this correction is therefore not a parity
extension of the fan product.  The full-depth product is already available.
It must still be summed with exact profile weights and trace conflicts.
In particular, the bounded-residual-rank regime (h-\ell=O(1)) receives
no vanishing gain from (3.5), and is not closed by this theorem.
