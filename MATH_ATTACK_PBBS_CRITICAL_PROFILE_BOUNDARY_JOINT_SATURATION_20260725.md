# RETRACTED: proposed critical PBBS profile--boundary joint saturation

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

> **Retraction (2026-07-25).** The advertised joint-saturation theorem is
> not proved. The proof audit in
> `PBBS_CRITICAL_PROFILE_BOUNDARY_AND_PORT_PROOF_AUDIT_20260725.md`
> identified three decisive gaps:
>
> 1. equation (3.5) is an upper bound on a fixed-word fibre, but
>    (3.9)--(3.11) incorrectly treat its right side as attained lower
>    capacity;
> 2. the set $\Omega_{m;s,p}$ enumerates the exact formal Pascal-fan
>    capacity envelope, not canonically realized PBBS inverse towers; and
> 3. the fresh cycles in Section 5 have no fibrewise compatible injection
>    into canonical parent clones.
>
> The valid result is only a **formal numerical load theorem**: the known
> orders of magnitude permit a balanced assignment of envelope tuples to
> word labels below a numerical allowance, followed by packing in a freely
> generated cycle model. This does not realize any joint PBBS capacity and
> does not obstruct a canonical cross-phase saving. Sections 3--5 and the
> conclusion must be read with the corrections inserted below.
>
> The replacement canonical attack is
> `MATH_ATTACK_PBBS_CANONICAL_SLIDING_DEFECT_AND_EXIT_INCIDENCE_20260725.md`.

## 0. Outcome

Write

\[
 Q_0(z)=Q_1(z)=1,\qquad Q_{j+1}(z)=Q_j(z)-zQ_{j-1}(z),
 \qquad C_j(z)=\frac{Q_j(z)}{Q_{j+1}(z)}.
\]

For a zero-winding return of height $s$, let $p$ be the first-mountain
pruning depth, put $q=s-p$, and set

\[
 b=2q-p+1=2s-3p+1.
\]

In the unsaturated sector $p<2q$, the exact full-depth Pascal-fan
capacity series is

\[
 \mathscr F^\star_{s,p}(z)
 =\frac{C_p(z)^b}{Q_p(z)^3}
 \left[1-\left(1-\frac{z^p}{Q_p(z)^2}\right)^b\right],
 \tag{0.1}
\]

and its coefficient is

\[
 \mathcal E_{m;s,p}=[z^{m-s}]\mathscr F^\star_{s,p}(z).
 \tag{0.2}
\]

The open question was whether coupling (0.1) to the positive endpoint
overlap, or to the exact triangular descendant intervals, forces

\[
 \sum_{s,p}\mathcal E^{\rm joint}_{m;s,p}
 =o(4^m/m^2)
 \tag{0.3}
\]

in the only remaining lane

\[
 p\asymp q\asymp\sqrt m.
 \tag{0.4}
\]

The original version claimed a negative saturation result here. That
claim is retracted for the reasons above.

### Retracted claim (not a theorem)

The original version claimed that there are constants $0<c<C<\infty$,
a fixed $A$, and infinitely many $m$ for which one can put every object
counted by a family of critical
coefficients (0.2) into a **single integral joint table** carrying all of
the following simultaneously:

1. its exact convex pruning profile and its exact zero-value full Pascal
   fan;
2. a positive balanced endpoint word $e$ of length $2p$, confined to
   the exact pruning strip $[-p,p]$;
3. the exact triangular descendant intervals

   \[
    I_{j,a}=[2a,2s+1-2(j-a)],\qquad 0\le a\le j\le p;
   \]

4. every currently proved $p$-refined boundary cap, including the
   fixed-word cap; and
5. an integral residue-locked packing of the parent intervals.

The joint mass and the packing both satisfy

\[
 \boxed{\mathcal J_m\ge c\,4^m/m^2.}
 \tag{0.5}
\]

The ambient number of parent edges used by the packing is

\[
 \Theta(\sqrt m\,\mathcal J_m)=\Theta(\operatorname{Cat}_m),
 \tag{0.6}
\]

so the construction saturates, rather than exceeds, the Catalan edge
budget.

This statement is retracted. The construction is not an exact integral
realization of the profile--boundary--descendant capacity relaxation: it
has neither actual fixed-word supply nor fibrewise parent-clone supply.
Accordingly, the former displayed consequence

\[
 \boxed{\text{RETRACTED: no joint PBBS realization was proved.}}
 \tag{0.7}
\]

does not follow. What remains true is only that the *numerical upper
allowances* are compatible with such a formal load. The actual canonical
cross-phase incidence problem remains open.

## 1. The exact finite profile objects behind the generating function

For fixed $s,p$, let $y_1,\ldots,y_p\ge0$ and define

\[
 r_j=s-j+\sum_{a=j+1}^p(a-j)y_a,
 \qquad 0\le j\le p.
 \tag{1.1}
\]

Then

\[
 m=s+\sum_{a=1}^p a y_a,
 \tag{1.2}
\]

and $p$ is the first mountain depth exactly when $y_p\ge1$. At inverse
level $j$, the fan fixes $j$ distinct child-slot variables. In the
zero-value capacity envelope the remaining free mass $y_j$ is a weak
composition into

\[
 2r_j-j+1
 \tag{1.3}
\]

boxes. Hence the exact set

\[
 \Omega_{m;s,p}
 =\left\{(\mathbf y,\mathbf n^{(1)},\ldots,\mathbf n^{(p)}):
 \begin{array}{l}
 y_p\ge1,\quad \sum_jj y_j=m-s,\\
 \mathbf n^{(j)}\in\mathbb Z_{\ge0}^{2r_j-j+1},\\
 \sum_i n_i^{(j)}=y_j
 \end{array}\right\}
 \tag{1.4}
\]

has cardinality

\[
 |\Omega_{m;s,p}|
 =\sum_{\substack{\mathbf y\ge0,\ y_p\ge1\\
                   \sum j y_j=m-s}}
   \prod_{j=1}^p\binom{y_j+2r_j-j}{y_j}
 =\mathcal E_{m;s,p}.
 \tag{1.5}
\]

Thus the objects used below are not fractional coefficient mass. They are
literal weak-composition tuples counted by the exact **capacity-envelope**
series. No realization map from these tuples to canonical PBBS inverse
towers is known.

The collapse of (1.5) to (0.1) follows from

\[
 t_j=\frac{z^j}{Q_j(z)^2},\qquad
 1-t_j=\frac{Q_{j-1}(z)Q_{j+1}(z)}{Q_j(z)^2},
 \tag{1.6}
\]

and the cancellation of the interior continuant powers. Restricting the
last negative-binomial sum to $y_p\ge1$ gives the bracket in (0.1).

## 2. Critical cells and their exact coefficient mass

Put

\[
 p\le b\le2p,
 \qquad s=\frac{b+3p-1}{2},
 \tag{2.1}
\]

with the required parity. Then

\[
 q=s-p=\frac{b+p-1}{2},
 \tag{2.2}
\]

so, uniformly in these cells,

\[
 p\asymp q\asymp s.
 \tag{2.3}
\]

At $z=1/4$,

\[
 Q_j(1/4)=\frac{j+1}{2^j},\qquad
 C_j(1/4)=\frac{2(j+1)}{j+2},
 \tag{2.4}
\]

and therefore

\[
 4^{-s}\mathscr F^\star_{s,p}(1/4)
 =\frac{2}{(p+1)^3}
 \left(\frac{p+1}{p+2}\right)^b
 \left[1-\left(1-\frac1{(p+1)^2}\right)^b\right]
 =\Theta(p^{-4}).
 \tag{2.5}
\]

The normalized coefficient law contains a $1/Q_{p-1}$ factor. Its mean
is $\Theta(p^2)$, its variance is $O(p^4)$, and the other positive
factors in (0.1) have total mean $O(p^2)$. Consequently there are
absolute $c_0,C_0,\eta>0$ such that a proportion at least $\eta$ of
the normalized mass in every cell (2.1) lies at coefficient indices

\[
 c_0p^2\le m-s\le C_0p^2.
 \tag{2.6}
\]

Take $p\in[R^{1/2},2R^{1/2}]$. There are $\Theta(R)$ pairs $(p,b)$
in (2.1), their total normalized mass in an interval $m\asymp R$ is
$\Omega(R^{-1})$, and that interval contains $O(R)$ integers. By
averaging, for arbitrarily large $m$, there is a critical cell family
$\mathscr C_m$ for which

\[
 \boxed{
 \sum_{(s,p)\in\mathscr C_m}|\Omega_{m;s,p}|
 \ge c\frac{4^m}{m^2}.}
 \tag{2.7}
\]

Every cell in $\mathscr C_m$ obeys

\[
 c\sqrt m\le p,q,s\le C\sqrt m.
 \tag{2.8}
\]

The tilted two-pole coefficient estimate also gives, uniformly in these
cells,

\[
 \boxed{|\Omega_{m;s,p}|\le C\frac{4^m}{m^3}.}
 \tag{2.9}
\]

Equations (2.7)--(2.9) are the lower and upper inputs for the joint load.

## 3. Positive endpoint word labels and the numerical upper allowance

For $p\ge2$, let

\[
 \mathcal W_p
 =\{e\in\{0,1\}^{2p}:\operatorname{net}(e)=0,
        \ e_1=e_{2p}=0\}.
 \tag{3.1}
\]

Every $e\in\mathcal W_p$ is confined to $[-p,p]$. Moreover

\[
 |\mathcal W_p|=\binom{2p-2}{p}
 \asymp\frac{4^p}{\sqrt p}.
 \tag{3.2}
\]

These are valid positive endpoint words with half-overlap

\[
 \lambda=p>0.
 \tag{3.3}
\]

For reference, the extremal word

\[
 e_p=0\,1^p0^{p-1}
 \tag{3.4}
\]

belongs to $\mathcal W_p$ and reaches height $p-1$. Thus the joint load
does not hide in a smaller strip.

The endpoint-array proof gives more than its final word-summed estimate.
For each fixed $e\in\mathcal W_p$, its two boundary occurrences have
joint critical weight at most $C16^{-p}$. Conditional on $e$, the
remaining semilength law has largest atom $O(s^{-2})$. The exact capped
array telescope contributes at most

\[
 C4^p\frac{(p+2)^2}{s^4}.
\]

After coefficient tilting, the resulting fixed-word capacity is

\[
 \boxed{
 \mathcal B_{m;s,p}(e)
 \le C4^{m-p}\frac{(p+2)^2}{s^6}.}
 \tag{3.5}
\]

Summing (3.5) over (3.2) recovers, up to constants, the known strip bound
at $\lambda=p$:

\[
 C4^m\frac{p^{3/2}}{s^6}.
 \tag{3.6}
\]

We can load the formal profile objects into **word labels**. This is not a
load into actual fixed-word PBBS fibres. For each cell choose a map

\[
 \beta_{s,p}:\Omega_{m;s,p}\longrightarrow\mathcal W_p
 \tag{3.7}
\]

whose fibres differ in size by at most one. This is an integral balanced
allocation. By (2.9) and (3.2),

\[
 |\beta_{s,p}^{-1}(e)|
 \le C\frac{4^{m-p}\sqrt p}{m^3}+1.
 \tag{3.8}
\]

Define the numerical allowance

\[
 U_{m;s,p}(e):=C4^{m-p}\frac{(p+2)^2}{s^6}.
 \tag{3.9}
\]

In a critical cell $U_{m;s,p}(e)\asymp_C4^{m-p}/m^2$, whereas the
nonconstant term in (3.8) is

\[
 O\!\left(\frac{4^{m-p}}{m^{11/4}}\right).
 \tag{3.10}
\]

The additive one in (3.8) is negligible because $4^{m-p}/m^2\to\infty$.
Therefore, for all sufficiently large critical $m$,

\[
 \boxed{
 |\beta_{s,p}^{-1}(e)|\le U_{m;s,p}(e)
 \qquad(e\in\mathcal W_p).}
 \tag{3.11}
\]

Equation (3.11) is only a formal numerical compatibility statement.
Equation (3.5) says that the actual fixed-word fibre is **at most** this
allowance; it supplies no lower capacity and may be empty. The original
inference from (3.5) to a genuine joint coefficient statement is retracted.

## 4. Formal descendant patterns on the envelope tuples

For $\omega\in\Omega_{m;s,p}$, inverse level $j$ has $j$ omitted
composition coordinates and $2r_j-j+1$ displayed free coordinates.
Adjoin to $\omega$ the formal return labels

\[
 \alpha_{j,0},\ldots,\alpha_{j,j},
 \qquad \alpha_{j,a+1}=\alpha_{j,a}-1,
 \tag{4.1}
\]

and the exact tight-return intervals

\[
 I_{j,a}=[2a,2s+1-2(j-a)].
 \tag{4.2}
\]

They obey

\[
 |I_{j,a}|=2(s-j)+1
 \tag{4.3}
\]

and the child identities

\[
 I_{j+1,a}=[L,R-2],\qquad
 I_{j+1,a+1}=[L+2,R]
 \tag{4.4}
\]

whenever $I_{j,a}=[L,R]$. The $j$ gaps between the consecutive labels
in (4.1) reproduce the $j$ zero coordinates removed in (1.3). This is the
formal combinatorial pattern behind the binomial factors in (1.5); it does
not prove that the tuple is a canonical PBBS inverse tower carrying these
descendants.

The endpoint word $\beta_{s,p}(\omega)$ and all descendant labels are
stored on the same object $\omega$. Consequently the resulting joint
table is

\[
 \mathcal T_{m;s,p}
 =\{(\omega,\beta_{s,p}(\omega),
          (I_{j,a})_{a\le j\le p}):
      \omega\in\Omega_{m;s,p}\},
 \tag{4.5}
\]

and

\[
 |\mathcal T_{m;s,p}|=\mathcal E_{m;s,p}.
 \tag{4.6}
\]

Define the total joint coefficient on the critical subsequence by

\[
 \mathcal J_m
 :=\sum_{(s,p)\in\mathscr C_m}|\mathcal T_{m;s,p}|.
 \tag{4.7}
\]

Then (2.7) gives $\mathcal J_m\ge c4^m/m^2$.

Equations (3.11) and (4.6) construct only a formally decorated envelope
table. They do not impose endpoint and descendant data jointly on actual
PBBS fibres.

## 5. Freely generated cycle model (not a fibre-capacity packing)

The following construction is retained only as a freely generated ambient
cycle model. It is not a packing in canonical inverse fibres.

For each $\tau=(\omega,e,(I_{j,a}))\in\mathcal T_{m;s,p}$, take one
directed parent cycle

\[
 \Gamma_\tau=\mathbb Z_{3g},\qquad g=2s+1.
 \tag{5.1}
\]

Give every vertex of this cycle the invariant profile tag of $\omega$.
Declare the three phases

\[
 0,\quad g,\quad2g
 \tag{5.2}
\]

eligible. At each eligible phase place the boundary word $e$, the same
common-base composition tower $\omega$, and the translated descendant
fan (4.2). Select the three parent intervals

\[
 [0,g),\qquad[g,2g),\qquad[2g,3g).
 \tag{5.3}
\]

They partition the edge set of $\Gamma_\tau$. Cycles belonging to
different $\tau$'s are disjoint. Hence all selected parent intervals are
pairwise edge-disjoint.

The original note asserted that these artificial edges could be assigned
to parent clones in every reduced-edge fibre. That assertion is retracted.
One tuple supplies no reason for the existence of the required $3g$
phase-compatible parent clones, and the global Catalan-order mass in
(5.6) cannot be redistributed between fibres. No compatible injections
of the form required by equation (3.1) of the proof audit are known.

The packing cardinality is

\[
 |\mathcal P_m^{\rm free}|
 =3\sum_{(s,p)\in\mathscr C_m}
     |\mathcal T_{m;s,p}|.
 \tag{5.4}
\]

By (2.7),

\[
 \boxed{|\mathcal P_m^{\rm free}|\ge3c\,4^m/m^2.}
 \tag{5.5}
\]

Its total parent-edge mass is

\[
 \begin{aligned}
 |E(\Gamma)|
 &=\sum_{(s,p)\in\mathscr C_m}
     3(2s+1)|\mathcal T_{m;s,p}|\\
 &=\Theta(\sqrt m)\,
   O(4^m/m^2)
 =O(4^m/m^{3/2})
 =O(\operatorname{Cat}_m).
 \end{aligned}
 \tag{5.6}
\]

The lower bound (2.7) and $s\asymp\sqrt m$ also give a matching lower
order after harmless constant thinning. Thus the **freely generated
cycle model** has Catalan-order global mass and critical density. This is
only an order-of-magnitude compatibility check, not a packing in the
profile--descendant fibre-capacity relaxation.

Theorem A is not proved.

## 6. What the formal table actually shows

The earlier load-table observation said only that the separate numerical
bounds

\[
 \sum_{s,p}\mathcal E_{m;s,p}=O(4^m/m^2)
 \tag{6.1}
\]

and

\[
 z_{m,s,2\lambda,p}
 \le C4^m\frac{(\lambda+2)^2}{s^6\sqrt{\lambda+1}}
       e^{-c\lambda/(p+1)^2}
 \tag{6.2}
\]

are numerically compatible with critical mass.

The formal label assignment is explicit:

\[
 \omega\longmapsto\beta_{s,p}(\omega).
 \tag{6.3}
\]

It is integral, word-valued, and balanced on every **label** fibre.
Equation (3.11) checks only the numerical allowance $U$, and Section 5
checks only freely generated cycles. Hence this is not an actual
profile--boundary correlation and not an actual fibrewise packing.

Numerically, the right side of the fixed-word upper bound exceeds the
evenly allocated formal load by a factor of order

\[
 m^{3/4}.
 \tag{6.4}
\]

This shows slack in the known upper allowances, but it says nothing about
lower supply in actual fixed-word fibres.

### 6.1 A genuine PBBS atom realizes the same joint local geometry

The relaxation is not based on a locally impossible combination. For
$n\ge3$ and $M\ge0$, put $F=(10)^M$ and

\[
 D_{n,M}=1^{3n+1}0^n1^{2n-1}0^{4n-1}F0.
 \tag{6.5}
\]

The exact canonical quotient trace of this word gives a genuine first
zero-winding return of duration $s=4n$. Its endpoint half-overlap, first
mountain depth, and residual mountain rank are

\[
 \lambda=n,\qquad p=n,\qquad q=3n,
 \tag{6.6}
\]

and its literal common boundary is precisely

\[
 e_n=0\,1^n0^{n-1}.
 \tag{6.7}
\]

Its only nonzero inverse curvatures are

\[
 y_1=M,\qquad y_n=1.
 \tag{6.8}
\]

Every one of the $n$ terminal fan equations at level $n$ prescribes a
distinct zero coordinate. The exact joint fan fraction is

\[
 Q_{n,M}
 =\frac{10n-4}{M+10n-4}\frac{5n+1}{6n+1}.
 \tag{6.9}
\]

Choosing $M=\lceil c(4n)^2\rceil$ with fixed $c>0$ puts the word in a
Gaussian window and gives

\[
 \sqrt{M+5n}\,Q_{n,M}\longrightarrow
 \frac{25}{12\sqrt c}>0.
 \tag{6.10}
\]

Thus a genuine PBBS return simultaneously realizes positive overlap
$\lambda=p$, the near-extremal word (3.4), an unsaturated
$p\asymp q\asymp\sqrt m$ profile, and the zero-value triangular fan at
the critical pointwise scale. This family is only sub-Catalan in
aggregate and supplies no packing lower bound. Its role is narrower: a
PBBS proof cannot exclude the joint load by declaring its local atoms
unrealizable. It must prove that harmonic-scale mass cannot organize
these atoms with the residue recurrence of Section 5.

## 7. Exact implication boundary for the actual PBBS

The obstruction is not a PBBS counterexample for one precise reason. The
maps $\beta_{s,p}$ and the residue placement (5.2) were chosen freely.
In the actual PBBS both are determined by the same first-maximum
chronology:

* the endpoint word is cut from the literal common carrier;
* the common-phase weak-composition vector is transported by the actual
  reduced PBBS itinerary; and
* the next eligible phase is not freely assignable modulo $2s+1$.

Therefore a strict theorem must control that single joint transport. A
sufficient statement can be isolated without any marginal product.

Fix one actual critical cell $(s,p)$, put $g=2s+1$, and let $\Omega$ be
an invariant profile fibre. Define

\[
 \mathcal A_i(e)\subseteq\Omega
 \tag{7.1}
\]

to be the vectors which, at quotient phase $i$, satisfy every fan equation
and have literal positive endpoint word $e$. The missing assertion is a
uniform no-residue-locking estimate of the form

\[
 \boxed{
 \sum_i\sum_{e,e'}
 |\mathcal A_i(e)\cap
   \tau^{-g}\mathcal A_{i+g}(e')|
 =o\!\left(\frac1{\sqrt m}
             \sum_i|\Omega|\right),
 \tag{7.2}
\]

followed by summation over the critical cells; a variable-gap version is
needed when cells are mixed in one packing. Equivalently, one may prove
directly that every actual
edge-disjoint critical family obeys

\[
 \sum_{I\in\mathcal P}|I|
 =o\!\left(
   \sum_{\text{profile base edges }x}F(x)\right).
 \tag{7.3}
\]

Since $|I|\asymp\sqrt m$, (7.3) gives

\[
 |\mathcal P|=o(4^m/m^2).
\]

The free-cycle model in Section 5 has no bearing on (7.2) or (7.3), because
it is not embedded in actual PBBS fibres. These remain open canonical
incidence statements.

## 8. Adversarial audit

1. **Formal label map only.** The map (3.7) is integral, but (3.11) checks
   a numerical allowance, not actual word-fibre supply.

2. **Exact coefficient objects.** The set (1.4) is integral, and its
   cardinality is exactly the coefficient (0.2).

3. **Positive overlap.** Every assigned word has length $2p>0$, so
   $\lambda=p\asymp\sqrt m$. The solved zero-overlap sector is not used.

4. **Correct critical lane.** Equations (2.2) and (2.8) give
   $p\asymp q\asymp\sqrt m$ and $p<2q$ with fixed room.

5. **Formal descendant information.** The $j$ zero coordinates and the
   interval labels are present in the envelope tuple; canonical PBBS
   realization is not proved.

6. **Free-cycle packing only.** The intervals (5.3) partition newly
   generated cycles, but no fibrewise parent-clone injection is proved.

7. **Global scale is insufficient.** Equation (5.6) is Catalan order, but
   global mass does not imply local fibre capacity.

8. **Scope.** Only the formal numerical load theorem stated in the
   retraction survives. No saturation of the exact capacitated relaxation
   is proved.

## 9. Final conclusion

The advertised joint saturation is retracted. What survives is an exact
critical profile-envelope coefficient, a balanced formal word-label table,
a freely generated cycle model of the same global order, and one genuine
PBBS local atom. None supplies actual fixed-word abundance or fibrewise
phase-compatible parent clones.

The critical $p\asymp q\asymp\sqrt m$ lane therefore remains open. Its
correct target is an actual common-base cross-phase theorem such as (7.2)
or (7.3), derived from the canonical first-maximum transport with no free
word assignment and no free cycles.
