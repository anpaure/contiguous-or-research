# Actual stopped pair spread, coin fibres, and the pair-safe process

Date: 2026-07-27

Scope: the compensated repaired/ordinary promotion-frame process and the
finite top-strip pair-column cutoff.

## Superseding PSF status

`MATH_THEOREM_PROFILE_PAIR_SPREAD_CLOSES_STOPPED_WHOLE_ARM_PSF_20260727.md`
proves PSF and $o(W)$ whole-arm stopped incidence under the sharpened
profile pair-spread condition

\[
 {d_t(x,y)\over\Delta_t}
 \le A_2u_t^{-1}{d_0(x,y)\over D_0}.
\]

The maximum-only condition (PS) below is insufficient because it loses
the cyclic distance profile when endpoint pairs are summed.  The sole
remaining pair-safe gate is now propagation of this profile condition
itself; the factorial whole-arm estimate is no longer open.

## 0. Verdict

There are four separate conclusions.

1.  The pair-star residual in
    `MATH_AUDIT_PAIR_COLUMN_TAIL_BETA_AND_PAIR_STAR_OBSTRUCTION_20260727.md`
    is an arbitrary edge-deletion subhypergraph.  The actual process has
    a vertex-induced residual.  Therefore that construction does not
    prove that the stopped trajectory can reach a pair star.  Its
    maximum degree is also bounded, so it lies beyond the ordinary
    degree stop used in the Gaussian-density run.

2.  The time-zero scale $d_0(x,y)/D_0=O(m^{-2})$ is not dynamically
    neutral.  Even when all common-event corrections vanish,
    conditioning two endpoints to survive rather than one gives the
    baseline factor $u_t^{-1}$, where

    \[
                              u_t=e^{-t/r}.
    \]

    The smallest plausible stopped scale is therefore

    \[
       d_t(x,y)\le {L^{C}\over m^2u_t}\Delta_t.           \tag{PS}
    \]

3.  This density loss is harmless for the **whole-arm** clock mass.  If

    \[
       \beta_t(F,F')\le {L^C\over m^2u_t},                \tag{HCE$_u$}
    \]

    for the equality-resolved arm pairs in a cutoff state with
    $p=O(L)$ arms, then

    \[
       \int_0^T\binom p2\beta_t\,dt
       \le {CL^{C+2}\over mz}=o(1),
       \qquad z=m^{-1/20}.                                \tag{0.1}
    \]

    Thus the finite backward tower closes under HCE$_u$; the stronger
    density-independent $m^{-2+o(1)}$ hypothesis is unnecessary.

4.  Compensation fibres have an exact solution at first moment: use the
    complete physical-resource union as the marginal reference.  Then
    every physical resource occurs once and the common-coin deficit is
    identically zero.  With armwise product normalization the deficit is
    nonzero and no hereditary $O(1/m)$ ratio follows from compensation.

The rigorous process available now is the **pair-safe stopped process**:
run the actual induced compensated process, use complete-union
normalization, and kill the monitored observable at the first failure of
the ordinary degree stop, (PS), or HCE$_u$.  Sections 2--5 give its exact
conditional inequalities.  They exclude every pair-star state before
the stop and make the top-strip drift summable.  What is not proved is
that the HCE$_u$ stop has $o(W)$ incidence.  The exact missing input is a
stopped factorial whole-arm link estimate, stated in Section 6.

## 1. The actual residual is induced

Let $A_t$ be the active physical resource set.  An edge clock selects an
active catalogue edge and deletes its resources; a compensation clock
deletes one active resource.  Neither operation deletes a catalogue edge
whose complete resource set remains active.  Hence, pathwise,

\[
               \boxed{\mathcal H_t=\mathcal H_0[A_t].}     \tag{1.1}
\]

In particular, retaining edges $f,f',g_1,\ldots,g_\ell$ and deleting
every other edge is not a reachability certificate.  One must exhibit an
active resource set $A$ such that the induced hypergraph
$\mathcal H_0[A]$ still has the claimed maximum degree and common-arm
fraction.  Neither of the two audited notes supplies such a set.

Moreover, their displayed residual has maximum degree at most three.
The actual top-strip argument is stopped while every monitored active
resource has degree at least a fixed fraction of the deterministic
current reference, which is enormous through $u\ge z$.  Thus that
particular residual is outside the stopped state space even if it is
viewed merely as a subhypergraph.

This observation retracts the claimed trajectory counterexample.  It
does not prove that a degree-scale induced pair star is impossible.

## 2. Exact conditional union inequalities

For an active resource set $S$, put

\[
 \mathcal E_t(S)=\bigcup_{x\in S}\mathcal E_t(x),\qquad
 J_t(S)=\sum_{x\in S}d_t(x)-|\mathcal E_t(S)|.
\tag{2.1}
\]

With

\[
 \nu_t={1\over r\Delta_t},\qquad
 \chi_t(x)={\Delta_t-d_t(x)\over r\Delta_t},
\tag{2.2}
\]

the exact union hazard is

\[
             \Lambda_t(S)={|S|\over r}-\nu_tJ_t(S).       \tag{2.3}
\]

For every finite $S$,

\[
 \begin{aligned}
 J_t(S)
 &=\sum_g\bigl(|g\cap S|-1\bigr)_+\\
 &\le\sum_{\{x,y\}\subseteq S}d_t(x,y).
 \end{aligned}                                           \tag{2.4}
\]

The first equality counts edge events only; compensation clocks are
already contained in (2.3).  Consequently, before the pair-spread stop

\[
 d_t(x,y)\le\delta_t\Delta_t\qquad(x\ne y),               \tag{2.5}
\]

one has the statewise conditional bounds

\[
 \boxed{
 { |S|\over r}-{\binom{|S|}{2}\delta_t\over r}
 \le\Lambda_t(S)\le {|S|\over r}.}                        \tag{2.6}
\]

If $P\cap R=\varnothing$, inclusion--exclusion gives the sharper
increment formula

\[
 \Lambda_t(P\cup R)-\Lambda_t(P)
 ={|R|\over r}
 -\nu_t\bigl[J_t(P\cup R)-J_t(P)\bigr],                  \tag{2.7}
\]

and

\[
 \boxed{
 { |R|\over r}
 -{\bigl(|P||R|+\binom{|R|}{2}\bigr)\delta_t\over r}
 \le\Lambda_t(P\cup R)-\Lambda_t(P)
 \le {|R|\over r}.}                                     \tag{2.8}
\]

These inequalities are conditional on the current stopped filtration;
they use no marginal-product approximation.

## 3. Why the neutral benchmark has a density loss

Fix active endpoints $x,y$.  Let

\[
                         X_{xy}(t)=d_t(x,y).
\]

For an active edge $e\supseteq\{x,y\}$, put
$R_e=V(e)\setminus\{x,y\}$.  Relative to survival of the two endpoints,
the exact loss rate of this edge is

\[
 \Lambda_t(V(e))-\Lambda_t(\{x,y\}).                     \tag{3.1}
\]

Equation (2.8) gives

\[
 \Lambda_t(V(e))-\Lambda_t(\{x,y\})
 \ge {r-2\over r}-{Cr\delta_t}.                          \tag{3.2}
\]

For a one-endpoint degree the corresponding zero-correlation rate is
$(r-1)/r$.  Therefore, even with $\delta_t=0$, the pair link decays
relative to its two-endpoint prefix like

\[
                         e^{-(r-2)t/r},
\]

whereas a degree relative to its one-endpoint prefix decays like
$e^{-(r-1)t/r}$.  Their ratio grows exactly by

\[
                         e^{t/r}=u_t^{-1}.                 \tag{3.3}
\]

Thus a density-independent hereditary $O(m^{-2})$ pair ratio cannot be
obtained from the compensated hazard equations alone.  Proving such a
ratio for the actual catalogue would require an additional negative-
dependence mechanism.  The neutral density-aware target is (PS).

There is also an exact obstruction to closing (PS) from its own first
moment.  If

\[
                         \delta_t={CL^C\over m^2u_t},
\]

then the accumulated error in (3.2) is

\[
 \int_0^T r\delta_t\,dt
 ={CL^Cr^2\over m^2}\left({1\over z}-1\right)
 =L^C\Theta(1/z),                                        \tag{3.4}
\]

because $dt=-r\,du/u$.  This is not $o(1)$.  Hence pair-spread does not
self-regenerate through a scalar first-moment Gronwall argument.  A
factorial link-energy or a sharper whole-arm incidence estimate is
genuinely necessary.

## 4. Pair-star certificate inequality

Let $P$ be the complete equality-resolved resource union of two active
arms.  Let $g_1,\ldots,g_h$ be common future edges, each meeting both
arms in genuinely new resources, and put

\[
              R=\left(\bigcup_{i=1}^hV(g_i)\right)\setminus P.
\tag{4.1}
\]

Before the pair-spread stop, (2.8) is the exact conditional estimate

\[
 \boxed{
 \Lambda_t(P\cup R)-\Lambda_t(P)
 \ge {|R|\over r}
 -{\bigl(|P||R|+\binom{|R|}{2}\bigr)\delta_t\over r}.}   \tag{4.2}
\]

For the pair-star certificate constructed in the audited note, the
$g_i$ are pairwise resource-disjoint outside their two displayed
endpoints.  Hence

\[
                         |P|\le2r,qquad |R|=h(r-2).       \tag{4.3}
\]

Combining (4.2)--(4.3), its conditional external killing rate is at
least

\[
                         h{r-2\over r}-C(h+2)^2r\delta_t. \tag{4.4}
\]

To state the consequence without dividing random indicators, let
$I_{P\cup R}(t)$ be the certificate-survival indicator and set

\[
 M_{P,R}(t)=I_{P\cup R}(t)\mathbf1_{t<\tau}
 \exp\!\left(\int_0^t\Lambda_s(P)\,ds\right),             \tag{4.4a}
\]

where $\tau$ is the pair-safe stop.  Stopping gives only a negative
jump, and before $\tau$

\[
 (\partial_t+\mathcal G_t)M_{P,R}
 =-[\Lambda_t(P\cup R)-\Lambda_t(P)]M_{P,R}.              \tag{4.4b}
\]

Thus (4.4) and Gronwall give, at $u=z$, the exact
prefix-compensated survival factor

\[
 \boxed{
 z^{h(r-2)}
 \exp\!\left[{CL^C(h+2)^2\over z}\right].}               \tag{4.5}
\]

For $h\le J=O(\log m)$, the logarithm of (4.5) is

\[
 -\Theta(hm\log m)+O(m^{1/20}L^C h^2)
 =-\Theta(hm\log m).                                     \tag{4.6}
\]

Thus the literal disjoint pair-star certificate is overwhelmingly
suppressed in the pair-safe stopped process.  What is still needed for
an aggregate trajectory theorem is to sum (4.5) over all certificates,
including their non-square equality/intersection shapes.

## 5. Whole-arm density-aware closure

For equality-resolved active arms $F,F'$, define

\[
 \beta_t(F,F')
 =\nu_t|\{g:g\cap(F\setminus F')\ne\varnothing,
             \ g\cap(F'\setminus F)\ne\varnothing\}|.    \tag{5.1}
\]

The pair-spread stop alone gives only the witness-sum estimate

\[
                         \beta_t(F,F')\le r\delta_t
                         ={L^C\over mu_t}.                 \tag{5.1a}
\]

Its integral is $L^C\Theta(1/z)$, so it does not close the cutoff.
The whole-arm geometry must save the additional factor $m^{-1}$.

Suppose the pair-safe process is stopped when

\[
                         \beta_t(F,F')>{CL^C\over m^2u_t}\tag{5.2}
\]

for any displayed arm pair.  At a cutoff state with $p$ nonprivate
arms, exact pair domination gives

\[
                         q(t)\le\binom p2{CL^C\over m^2u_t}.
\tag{5.3}
\]

Since $u_t=e^{-t/r}$ and $T=r\log(1/z)$,

\[
 \begin{aligned}
 Q:=\int_0^Tq(t)\,dt
 &\le {CL^Cp^2r\over m^2}
       \int_z^1{du\over u^2}\\
 &\le {CL^{C+2}\over mz}=m^{-19/20+o(1)}=o(1).           \tag{5.4}
 \end{aligned}
\]

Therefore the finite-cutoff potential remains valid with HCE$_u$ in
place of the stronger density-independent HCE.  This is a strict
improvement in the required dynamic statement.

## 6. The exact remaining factorial estimate

For one displayed arm pair define $C_t(F,F')$ to be the common-edge
family in (5.1).  For $1\le h\le J$, let
$\mathcal D_h(F,F';t)$ be the ordered $h$-tuples of distinct members of
$C_t(F,F')$ whose resources outside $F\cup F'$ are pairwise disjoint.
The disjoint pair-star is contained in this sector.

The sufficient stopped factorial estimate is

\[
 \boxed{
 \sum_{F,F'}w_t(F,F')|\mathcal D_h(F,F';t)|
 \le (Ch)^{Ch}
 \left({\Delta_t\over mu_t}\right)^h
 \sum_{F,F'}w_t(F,F')                                  }\tag{PSF}
\]

for the owner/root incidence weights $w_t$ occurring in the top-strip
observable.  The scale is forced by the time-zero whole-arm count
$O(D/m)$ and the $u_t^{-1}$ prefix-conditioning loss.  Markov at
$h=C_0\log m$, followed by (5.4), quarantines every disjoint pair-star
sector with superpolynomial margin.

For tuples with overlapping external resources, the exact analogue is
obtained by partitioning according to the equality/intersection shape
and replacing $h(r-2)$ in (4.3) by the actual number of new physical
resources.  Those are precisely the finite mixed diagrams that a
complete proof must regenerate dynamically.  The static higher
codegree table initializes them but does not prove (PSF) after
endogenous restriction.

## 7. Exact coin-fibre control

Let $A_1,\ldots,A_p$ be formal arms and

\[
                         \ell_y=|\{i:y\in A_i\}|.
\]

With armwise marginal normalization, the exact compensation deficit is

\[
 \boxed{
 C_\circ(t)=\sum_y\chi_t(y)(\ell_y-1)_+.}                 \tag{7.1}
\]

No small ratio follows merely from one-point compensation: the weights
$\chi_t(y)$ may be supported on resources common to several arms.  If
the degree stop additionally gives

\[
                         \Delta_t-d_t(y)\le\eta_t\Delta_t,
\]

then

\[
 C_\circ(t)
 \le {\eta_t\over r}\sum_y(\ell_y-1)_+
 \le\eta_t p.                                             \tag{7.2}
\]

This is the exact conditional armwise bound; it requires an integrated
degree-flatness estimate to be useful.

The cleaner choice is complete physical-union normalization.  Assign
each shared physical resource once in

\[
                         U=\bigcup_{i=1}^pA_i.
\]

Then its reference contains the single term
$\sum_{y\in U}\chi_t(y)$, exactly equal to the actual union coin
hazard.  Hence

\[
                         \boxed{C_\circ^{\rm union}(t)=0.}\tag{7.3}
\]

This removes the coin-fibre gate at first moment without any stochastic
assumption.  It does not remove the shared edge-event term (5.1).

## 8. Final boundary

Proved here:

1. the arbitrary edge-deletion pair star is not a trajectory
   counterexample to the induced stopped process;
2. exact conditional union bounds (2.6) and (2.8);
3. the exact $u^{-1}$ loss in the zero-correlation benchmark;
4. summability of the density-aware whole-arm condition HCE$_u$;
5. exponential suppression of every fixed disjoint pair-star
   certificate before the pair-spread stop; and
6. exact elimination of compensation fibres by full physical-union
   normalization.

Subsequently proved under profile pair spread:

\[
 \boxed{
 \text{PSF and }o(W)\text{ incidence for the HCE$_u$ whole-arm stop}.}
\]

Thus the actual trajectory is not refuted by the pair-star subgraph,
and HCE$_u$ now follows from profile pair spread.  The remaining dynamic
inequality is propagation of the profile pair-spread stop itself (with
the $u^{-2}$ triple-fibre threshold as the first auxiliary candidate).
