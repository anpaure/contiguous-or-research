# Pair-column tail: (O(1/m)) under pair spread, but (Theta(1)) in a reachable pair-star residual

Date: 2026-07-27

Scope: the ordered pair-column tower in the top-strip first-moment
hierarchy.

## Dynamic scope correction

The pair-star construction in Section 2 is an arbitrary edge-deletion
subhypergraph, not a residual proved reachable by the actual compensated
process.  The actual residual is vertex-induced:

\[
                         \mathcal H_t=\mathcal H_0[A_t].
\]

Moreover the displayed construction has bounded maximum degree and is
outside the ordinary degree-stopped Gaussian run.  It therefore refutes
deletion-hereditary pair spread, but it does **not** refute pair spread
along the actual stopped trajectory.  The trajectory claim (0.4) is
retracted.

The correct neutral dynamic scale also includes endpoint conditioning:
$m^{-2}u_t^{-1}$ rather than $m^{-2}$.  At the whole-arm level this loss
is harmless because

\[
 \int_0^T{dt\over m^2u_t}=O((mz)^{-1})=o(1).
\]

The maximum bound alone still loses a factor $m$ when all endpoint
pairs are summed.  The sufficient condition is preservation of the
full time-zero pair profile,

\[
 {d_t(x,y)\over\Delta_t}
 \le A_2u_t^{-1}{d_0(x,y)\over D_0}.
\]

Under this profile condition, the whole-arm PSF estimate and its
$o(W)$ stopped incidence are proved in
`MATH_THEOREM_PROFILE_PAIR_SPREAD_CLOSES_STOPPED_WHOLE_ARM_PSF_20260727.md`.

Exact conditional inequalities, the pair-safe stopped process, and the
remaining factorial link estimate are in
`MATH_AUDIT_ACTUAL_STOPPED_PAIR_SPREAD_COIN_FIBRE_AND_PAIR_SAFE_PROCESS_20260727.md`.

## 0. Verdict

Let (f,f') be two equality-resolved physical row arms and remove their
known common resources from the cross-prefix calculation.  Define the
genuinely new common edge-event fraction

\[
 \beta_t(f,f')=
 {|{g:\ g\cap(f\setminus f')\ne\varnothing,
          \ g\cap(f'\setminus f)\ne\varnothing}|
  \over K\Delta_t}.
\tag{0.1}
\]

There are two sharp statements.

1. Under the stopped current pair-spread condition

   \[
       d_t(y,z)\le\delta_t\Delta_t
       \qquad(y\ne z),
   \tag{0.2}
   \]

   one has

   \[
                  \boxed{\beta_t(f,f')\le K\delta_t.}
   \tag{0.3}
   \]

   In particular, \(\delta_t=O(m^{-2}\operatorname{polylog}m)\)
   gives \(\beta=O(\operatorname{polylog}m/m)\).

2. Without (0.2), even after full row/resource equality resolution,
   arbitrary edge deletion admits pair-star subhypergraphs with

   \[
                         \boxed{\beta_t(f,f')=\Theta(1).}
   \tag{0.4}
   \]

Therefore no deletion-hereditary polylogarithmic cutoff closes the
ordered tower.  This does not decide the actual induced stopped process.
Conditional on a suitable density-aware trajectory version of (0.2),
the finite hybrid remains valid.

## 1. The upper bound under pair spread

Every genuinely new common event (g) contains some ordered pair

\[
              y\in f\setminus f',qquad
              z\in f'\setminus f.
\tag{1.1}
\]

Consequently

\[
\begin{aligned}
 |{g:g\sim f, g\sim f'\}_{\rm new}|
 &\le
 \sum_{y\in f\setminus f'}
 \sum_{z\in f'\setminus f}d_t(y,z)\\
 &\le K^2\delta_t\Delta_t.
\end{aligned}
\tag{1.2}
\]

Division by (K\Delta_t) proves (0.3).  The estimate is insensitive to
long common segments, because resources in (f\cap f') have already
been quotient-resolved and their marginal hazards belong to the physical
reference rather than to a future pair column.

A common compensation clock cannot be genuinely new: one compensation
resource kills both rows only when it belongs to (f\cap f'), hence it
is removed by the same equality resolution.  Thus (0.3) is the complete
tail parameter after physical quotienting.

## 2. Pair-star residual with \(\beta=\Theta(1)\)

Take a repaired row (f) and a relabelling transposition whose two labels
are separated by a linear cyclic distance, and put (f'=\tau f).  On a
linear fraction of the retained phases, exactly one transposed label
belongs to the middle owner.  After deleting the phases fixed by (\tau),
this gives (cK) distinct paired owners

\[
             f\setminus f'\supseteq\{y_1,\ldots,y_{cK}\},
 \qquad
             f'\setminus f\supseteq\{z_1,\ldots,z_{cK}\}.
\tag{2.1}
\]

Each pair satisfies (d_J(y_i,z_i)=1).  Choose one repaired edge

\[
                         g_i\ni y_i,z_i
\tag{2.2}
\]

for each of (cK) indices, with the (g_i)'s pairwise resource-disjoint
outside their displayed endpoints and avoiding every other displayed
endpoint.  This greedy choice is available from the exact distance-one
pair link: it has (\Theta(D/m^2)) candidates, while prescribing one
further forbidden owner costs an additional (O(m^{-2})) factor by the
same path-mesh endpoint count.  At step (i), only (O(K^2)) owners have
been used; after reducing (c>0) if necessary, fewer than half the pair
link candidates are forbidden.

Keep (f,f') and the edges (g_i), and delete every other catalogue edge.

The resulting residual is obtained solely by edge deletion.  Its maximum
degree is

\[
                         \Delta_t\le3,
\tag{2.3}
\]

whereas every (g_i) conflicts with both (f) and (f').  Hence

\[
 |{g:g\sim f, g\sim f'}_{\rm new}|
 =cK=\Theta(K\Delta_t),
\tag{2.4}
\]

which proves (0.4).

No resource equality has been hidden: the two endpoints of each pair
((y_i,z_i)) are distinct, and the common event is the future edge (g),
not a shared vertex.  Thus physical equality resolution does not remove
the obstruction.

This construction is an edge-deletion subhypergraph, not a
vertex-induced residual of the random slow-bite trajectory.  It proves
only that a pointwise \(o(1)\) value of \(\beta\) cannot be
deletion-hereditary.

## 3. Hybrid cutoff when pair spread is available

Let

\[
                  \beta=K\delta_t,
 \qquad
                  B=C_2(\log m)^2.
\tag{3.1}
\]

Choose the certified endpoint range with enough constant slack that the
base excess (s\le L) and the first (B) ordered pair columns satisfy

\[
                         s+B\le L_{\rm pm}.
\tag{3.2}
\]

The endpoint proof is unchanged for
\(L_{\rm pm}=O((\log m)^2)\) after increasing its constant.  It gives the
correct \(\alpha^j\) scale for \(j\le B\), with the envelope evaluated at
the total order \(s+j\), not at \(s\).

For (j>B), expose only the chronology.  Conditional on the current
pair-spread stop, every additional genuinely new common column has
conditional mass at most \(\beta\).  The ordered-time simplex therefore
gives

\[
 \sum_{j>B}{(CT\beta)^j\over j!}
 \le
 \left({eCT\beta\over B}\right)^B
 \quad\text{when }B\ge2eCT\beta.
\tag{3.3}
\]

If \(\delta_t=O(m^{-2}\operatorname{polylog}m)\) with a sufficiently
small fixed polylogarithmic power, then

\[
                  T\beta
 =O(\operatorname{polylog}m\cdot\log m),
\tag{3.4}
\]

and (B) can be enlarged within the polylogarithmic endpoint range so
that (3.3) is

\[
                         \exp[-\Omega(B\log\log m)].
\tag{3.5}
\]

At the sharp scale \(\delta_t=O(m^{-2})\), one has
\(T\beta=O(\log m)\), and \(B=C_2(\log m)^2\) gives

\[
                         \exp[-\Omega((\log m)^2\log\log m)].
\tag{3.6}
\]

This is far below every polynomial leave budget.

By contrast, the pair-star residual has \(\beta=\Theta(1)\), so

\[
                         T\beta=\Theta(m\log m).
\tag{3.7}
\]

No \(B=\operatorname{polylog}m\) can satisfy the condition in (3.3).

## 4. Exact remaining gate

The ordered tower does not require an all-order endpoint theorem if one
can prove the trajectory-specific pair-spread condition

\[
 \boxed{
 d_t(y,z)\le {\operatorname{polylog}m\over m^2}\Delta_t
 }
\tag{4.1}
\]

outside owner/root incidence (o(E_t)), uniformly to density (z).
Under (4.1), the static-prefix plus chronological-tail hybrid closes.
Without a condition of this kind, (0.4) shows that the best universal
tail parameter is one, and the hybrid cannot close.
