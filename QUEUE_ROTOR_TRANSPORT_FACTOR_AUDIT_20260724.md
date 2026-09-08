# Audit of the rotor-transport factor note (2026-07-24)

Audited file: `QUEUE_ROTOR_TRANSPORT_FACTOR_20260724.md`.

## Verdict

The positive rotor-transport theorem is valid after one wording correction:
the displayed arcs form a canonical biregular **subrelation** of all valid
one-step move-to-front transitions, rather than the exhaustive transition
relation.  This does not weaken any existence, uniform-marginal, or integral
path-factor conclusion.

The original block-barrier conclusion was quantitatively overstated.  It
silently substituted `R_q=(1-o(1))W` at the reservoir depth, whereas the
intended symmetric-chain quota is `R_q=N_q` and

\[
 \frac{N_q}{W}=(\log m)^{-1+o(1)}
 \quad\text{for }q=(1+o(1))\sqrt{m\log\log m}.
\]

The source note has been patched to retain this density factor and to limit
the barrier to direct one-update rotor packings with separate resets.

## Checks that pass

1. `|F_d|=W(m)_d^2`, and every signed depth-`q` mask has fibre
   `|F_d|/N_q`.
2. For the defined canonical arcs, the left degrees are `m-d` for `e<d`
   and `(m-d)^2` for `e=d` (including the separately defined `d=e=0`
   case).  Coordinate transitivity and arc double counting give
   
   \[
   r^-_{d,e}=r^+_{d,e}(m-e)_{d-e}^2.
   \]
3. The ordered last-occurrence partition
   
   \[
   (L_d,\{x_{d-1}\},\ldots,\{x_0\},
     \{y_1\},\ldots,\{y_d\},S^c\setminus\{y_1,\ldots,y_d\})
   \]
   exposes the advertised chain and can be initialized literally by writing
   its blocks in reverse order.  Appending the successor lower core produces
   exactly the leading blocks specified by the rotor formulas.
4. Choosing `M` divisible by all `|F_d|r^+_{d,e}` makes every arc coupling
   integral.  Pairing incoming and outgoing copies at each intermediate flag
   composes the layer couplings into exactly `M` full paths.
5. At every active time, fibre counting gives `M/N_q` copies of each signed
   depth-`q` mask, hence `a_qM/N_q` over the full path factor; the middle
   multiplicity is `HM/W`.

## Corrections made

### Canonical versus exhaustive arcs

Condition (2.1) excludes all old advertised upper coordinates.  A valid MTF
update can sometimes use an old upper coordinate that is discarded when the
radius falls (or the last discarded upper coordinate at equal radius).
Therefore the relation is not exhaustive.  It is nevertheless a valid,
biregular subrelation, which is all the path-factor proof needs.

### Density-sensitive block barrier

With `R_q` active centers in blocks of size at most `b`, the correct direct
packing conclusions are

\[
 \#\text{ high components}\ge(1-o(1))\frac{R_q}{b},
 \qquad
 \text{reset cost}\ge(2q+1)(1-o(1))\frac{R_q}{b}.
\]

Thus vanishing reset cost relative to `W` requires only

\[
 \frac{bW}{qR_q}\to\infty,
\]

not `b/q\to\infty` in general.  At the reservoir threshold this forces

\[
 b=\omega\!\left(
 \sqrt{m\log\log m}(\log m)^{-1+o(1)}
 \right),
\]

so bounded blocks are excluded, but `Theta(q)`-local correlation is not.

The previously stated estimate
`b m/((m)_(q-1)(m)_q) <= (1+o(1))b m^(2-2q)` was also nonuniform in growing
`q`.  The uniform argument is instead

\[
 \frac{bm}{(m)_{q-1}(m)_q}
 \le \frac{bm}{(m)_1(m)_2}
 =\frac{b}{m(m-1)}\le\frac1{m-1}.
\]

Finally, the component proof applies to direct packings using one rotor
update between advertised centers.  Extra connector states might change the
ledger, and the note now explicitly declines to lower-bound their cost.

## Resulting status

The exact integral flag-space transport and mask-marginal conclusions stand.
The negative result is a useful but density-sensitive direct-reset barrier;
it is not an `omega(q)` correlation lower bound at all depths and is not a
general obstruction to connector-based rebraiding.
