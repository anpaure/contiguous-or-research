# Correlated-row terminal absorption: nested-charge gain, exact barriers, and the literal constant-one escape

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

Audited sources:

- `MATH_THEOREM_CORRELATED_ROW_ORBIT_ABSORBER_AND_SHADOW_LOCK_20260726.md`;
- `MATH_THEOREM_N_OUTER_OWNER_FLAG_RUN_INVARIANT_20260726.md`.

Auxiliary proved inputs used for the exact escape ledger:

- `MATH_THEOREM_N_H_MEMORY_KERNEL_SHADOW_UNLOCKING_20260726.md`;
- `MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md`.

Independent audits of the decisive steps:

- `MATH_ATTACK_L_CORRELATED_ROW_NESTED_CHARGE_BARRIER_AND_LITERAL_ESCAPE_AUDIT_20260726.md`;
- `MATH_ATTACK_L_CORRELATED_ROW_SECTION7_KERNEL_AUDIT_20260726.md`.

## 0. Verdict

The two source reports are mathematically sound in their stated main
scopes.  The terminal exponent ledger is

\[
 \boxed{
 \text{bulk row slack: }H^3=o(m),\qquad
 \text{independent terminal collision: }H^4=o(m).}             \tag{0.1}
\]

Thus the exponent \(1/4\) is caused specifically by paying for \(q\)
crossing slots independently at every depth \(q\), not by the common run
vector.

There is a genuine conditional improvement.  If every shallow collision
can be charged to one of the \(H\) deepest crossing targets, then

\[
 \Pr(\text{bad shore})
 \le 2H(\lambda_H-1)
 =(2+o(1))\frac{H^3}{m},                            \tag{0.2}
\]

where \(\lambda_q=W/N_q\).  This gives exact terminal absorption through

\[
                         \boxed{H=o(m^{1/3})}.       \tag{0.3}
\]

An abstract SCD bank with the required nested cardinalities exists.
However, it is **not** yet a legal owner construction.  Three exact gates
remain:

1. a fixed proper SCD descendant map cannot commute with the full
   \(S_{2m}\)-orbit used to make deepest targets uniform;
2. the completed high-target families must lie on one common integral run
   line at every depth and both signs;
3. their flags must satisfy the semigroup law \(R_j=R_1^j\), equivalently
   the full \(H\)-memory circulation.

Consequently (0.3) is a theorem under an explicit nested-charge hypothesis,
not an unconditional exponent improvement for one exact successor.

There are two sharp barriers to the proposed local nested/hash/SCD route.

- At depth \(H\), the transitive collar hypergraph has fractional
  transversal number \(N_H/H\), while the cap-two duplicate budget is
  asymptotic to \(N_HH^2/m\).  Cardinality and uniform-marginal arguments
  therefore stop exactly when \(H^3\asymp m\).
- Short-core alternatives remain strongly correlated against star
  families: several alternatives which differ on only \(O(H)\) coordinates
  collide together with probability of first order in the bad density, not
  its square.

More decisively for the requested coefficient-one theorem, the exact
terminal quota absorber is not a necessary gate.  In the cap-two range,
a compiler-safe open Hamilton path satisfying the preload hypotheses
already has every target in its internal signed histograms; the seam is
needed only to restore exact multiplicities.  The finite delay-factor
compiler turns that path into a literal word of length at most \(W+H\).

More generally, cutting one cyclically compiler-safe owner cycle loses
at most \(q\) targets per sign and depth.  Every lost nonempty target can
be appended as one literal one-letter OR interval.  The singleton part of
the repair is at most

\[
                       2\sum_{q=1}^Hq=H(H+1)=o(W). \tag{0.4}
\]

and a universal one-cycle emitted-letter bound is

\[
                         W+H+H(H+1).               \tag{0.5}
\]

For \(K\) cycles, bare cuts plus singleton repair cost
\(W+HK+KH(H+1)\), while full collars cost \(W+2HK\).  Thus the respective
sufficient ledgers are \(KH^2=o(W)\) and \(KH=o(W)\).  These
literalization operations do not modify the underlying cyclic successor
or its common run vector; they merely choose a word representation and
append repair letters.  They bypass shadow-lock because a repaired target
is not inserted as a nested Johnson window.

For every \(1\le H\le m-1\), this makes terminal absorption unnecessary
*conditional on a cyclically compiler-safe full-support central cover*.
Combined with the proved product-SCD outer-tail estimate, it removes
exact terminal multiplicity closure as a separate constant-one gate.  It
does not construct the required central cover.  The surviving problem is
the internal central support/memory-circulation theorem at a depth
\(H/\sqrt m\to\infty\), with sufficiently few cycles.

For an exact owner-internal escape from a genuine lock, the right operation
is an integer **memory-kernel shadow-unlocking trade**.  Its complete
necessary-and-sufficient equations are proved in
`MATH_THEOREM_N_H_MEMORY_KERNEL_SHADOW_UNLOCKING_20260726.md` and summarized
in Section 7 below.

## 1. Audit of the terminal ledgers

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \lambda_q=\frac W{N_q}.                           \tag{1.1}
\]

In the cap-two range put

\[
 s_q=W-N_q=(\lambda_q-1)N_q.                       \tag{1.2}
\]

For an internal Hamilton path, the exact duplicate count forced by the
source's Lemma 4.1 is \(s_q-q\), not merely at most \(s_q\).  Hence the
sharp version of the orbit-seam expectation is

\[
\begin{aligned}
 \mathbb EC
 &=
 \sum_{q=1}^Hq
 \left(\frac{|D_q^-|}{N_q}+\frac{|D_q^+|}{N_q}\right)\\
 &=2\sum_{q=1}^Hq\frac{s_q-q}{N_q}\\
 &=2\sum_{q=1}^Hq(\lambda_q-1)
   -2\sum_{q=1}^H\frac{q^2}{N_q}.                  \tag{1.3}
\end{aligned}
\]

The last term is negligible.  Uniformly for \(H=o(\sqrt m)\),

\[
 \lambda_q-1=(1+o(1))\frac{q^2}{m},               \tag{1.4}
\]

so, when also \(H\to\infty\),

\[
 \mathbb EC
 =\left(\frac12+o(1)\right)\frac{H^4}{m}.         \tag{1.5}
\]

Without the hypothesis \(H\to\infty\), the theorem-safe expression is

\[
 \mathbb EC
 \le(1+o(1))\frac{H^2(H+1)^2}{2m}.               \tag{1.6}
\]

Thus \(H=o(m^{1/4})\) gives a \(1-o(1)\) good fraction.  At
\(H=\alpha m^{1/4}\), Markov gives the lower bound

\[
 \Pr(\text{good})\ge1-\frac{\alpha^4}{2}-o(1);     \tag{1.7}
\]

existence for \(\alpha^4<2\) is correct, but the good fraction need not
tend to one.

The bulk row/column calculation is also correct:

\[
 \mathbb EZ
 \le2\sum_{q=1}^H(m-q+1)(\lambda_q-1)
 =(1+o(1))\frac{H(H+1)(2H+1)}3.                   \tag{1.8}
\]

For \(H\to\infty\), this is \((2/3+o(1))H^3\).  Obtaining
\(m-o(m)\) available rows and columns requires \(H^3=o(m)\), giving the
bulk exponent \(1/3\).

The only textual correction in the shadow-escape report is

\[
 \kappa^{2(H-q)}
 \left((m-q)_{\underline{H-q}}\right)^2,            \tag{1.9}
\]

not \(\kappa^{,2(H-q)}\), in its equation (7.4).

## 2. Exact terminal arithmetic beyond cap two

The cap-two language itself cannot survive the requested super-Gaussian
window.  The following exact lemma shows what replaces it and why pure
collision avoidance ceases to be enough.

Fix one depth and write

\[
                         W=cN+r,\qquad0\le r<N.     \tag{2.1}
\]

The completed balanced loads are \(c\) and \(c+1\), with exactly \(r\)
high targets.  An open Hamilton path has \(W-q\) occurrences at that
depth.

### Lemma 2.1 (floor/remainder seam dichotomy)

Suppose every internal target load belongs to
\(\{c-1,c,c+1\}\).  Put

\[
 D=\{T:\ell(T)=c+1\},\qquad
 E=\{T:\ell(T)=c-1\}.                              \tag{2.2}
\]

Then

\[
                         |D|-|E|=r-q.              \tag{2.3}
\]

If a seam supplies a set \(C\) of \(q\) distinct targets, its completed
histogram is balanced if and only if

\[
                         E\subseteq C,\qquad C\cap D=\varnothing.          \tag{2.4}
\]

In that event its completed high family is

\[
 \widehat{\mathcal H}
 =D\ \dot\cup\ (C\setminus E),\qquad
 |\widehat{\mathcal H}|=r.                         \tag{2.5}
\]

Consequently:

1. If \(r\ge q\) and \(|D|\le r-q\), then
   \[
                         E=\varnothing,\qquad |D|=r-q.           \tag{2.6}
   \]
   Exact seam closure must hit \(q\) distinct load-\(c\) targets and avoid
   every load-\((c+1)\) target.
2. If \(r<q\) and \(|E|\le q-r\), then
   \[
                         |E|=q-r,\qquad D=\varnothing.           \tag{2.7}
   \]
   Exact seam closure must hit all \(q-r\) prescribed load-\((c-1)\)
   deficits and exactly \(r\) further load-\(c\) targets.

#### Proof

Summing the internal loads gives

\[
 cN-|E|+|D|=W-q=cN+r-q,
\]

which is (2.3).  After adding one occurrence to every member of \(C\), a
load-\((c-1)\) target reaches the permitted floor precisely when it lies in
\(C\), while a load-\((c+1)\) target exceeds the ceiling precisely when it
lies in \(C\).  This proves (2.4); (2.3) then gives (2.5).

In the first case, (2.3) gives
\(|D|=r-q+|E|\ge r-q\), so the assumed upper bound forces
\(E=\varnothing\) and \(|D|=r-q\).  The second case is dual. \(\square\)

The no-deficit half does not require the three-value hypothesis.  If every
load is at most \(c+1\), put

\[
 \Delta=\sum_T(c-\ell(T))_+.
\]

The same mass identity is

\[
                         |D|-\Delta=r-q.           \tag{2.8}
\]

Therefore, when \(r\ge q\), the single inequality
\(|D|\le r-q\) forces \(\Delta=0\) and \(|D|=r-q\).  This is the exact
general form of the cap-two duplicate-budget argument.

In the source's cap-two regime, \(c=1\), \(r=s_q\), and
\(s_q\gg q\), so only case 1 occurs.  When \(H/\sqrt m\to\infty\),
\(W/N_H\) is no longer below two, and the remainder \(r_q=W\bmod N_q\)
has no proved uniform lower bound by \(q\).  An exact all-depth theorem
must therefore handle case 2 unless it first proves a new arithmetic
remainder bound.  That case is targeted absorption, and the shadow-lock
obstruction applies to it directly.

## 3. The nested-charge theorem

Return to the cap-two range.  Let a shore \(a\) have crossing targets

\[
 C_{q,k}^\epsilon(a),\qquad
 1\le k\le q,\quad \epsilon\in\{-,+\}.             \tag{3.1}
\]

The preload and all cap families \(D_q^\epsilon\) remain fixed while the
shore varies.

### Definition 3.1 (nested charge)

A collar atlas has a nested charge through depth \(H\) if, for every
\((q,k,\epsilon)\), there is a deepest-slot index
\(\psi(q,k,\epsilon)\in[H]\) such that, for every shore \(a\),

\[
 C_{q,k}^\epsilon(a)\in D_q^\epsilon
 \quad\Longrightarrow\quad
 C_{H,\psi(q,k,\epsilon)}^\epsilon(a)\in D_H^\epsilon.          \tag{3.2}
\]

This is a shorewise implication.  It does not assert independence among
depths or slots.

### Theorem 3.2 (nested-charge terminal absorber)

Assume:

1. the internal path obeys the cap-two hypotheses of Lemma 4.1 in the
   audited absorber report;
2. the collar atlas satisfies (3.2);
3. each depth-\(H\) crossing target is uniform on its signed target layer
   under the relative shore distribution.

Then

\[
\begin{aligned}
 \Pr(\text{some signed collision at some depth})
 &\le H\frac{|D_H^-|+|D_H^+|}{N_H}\\
 &\le2H\frac{s_H-H}{N_H}\\
 &<2H(\lambda_H-1).                               \tag{3.3}
\end{aligned}
\]

Consequently, for \(H=o(m^{1/3})\), a \(1-o(1)\) fraction of shores close
all terminal quotas exactly.  If \(H=\alpha m^{1/3}\), one good shore is
guaranteed whenever

\[
                         2\alpha^3<1.              \tag{3.4}
\]

#### Proof

By (3.2), every shallow collision implies that at least one of the \(H\)
deepest lower or \(H\) deepest upper crossing targets is in the
corresponding depth-\(H\) cap family.  Take the union bound over those
\(2H\) deepest targets and use their uniform marginals.  This proves
(3.3).  Uniformly for \(H=o(\sqrt m)\),

\[
 2H(\lambda_H-1)=(2+o(1))\frac{H^3}{m}.            \tag{3.5}
\]

If the bound is below one, some shore is collision-free.  The exact seam
bookkeeping and distinct-crossing-target lemmas in the audited report then
give the completed balanced quotas. \(\square\)

If \(u_H\) signed crossing slots are not covered by (3.2), the same proof
gives the robust bound

\[
 \Pr(\text{bad})
 \le2H(\lambda_H-1)
    +u_H\max_{q\le H}(\lambda_q-1).                \tag{3.6}
\]

Thus

\[
                         u_H=o(m/H^2)              \tag{3.7}
\]

is sufficient at every \(H=o(m^{1/3})\).

The exact floor/remainder form of (3.3), in the no-deficit regime of
Lemma 2.1, is

\[
 \Pr(\text{bad})
 \le
 H\left(\frac{r_H-H}{N_H}
        +\frac{r_H-H}{N_H}\right)
 =\frac{2H(r_H-H)}{N_H}.                          \tag{3.8}
\]

This shows directly that nested charging does not reach a fixed Gaussian
window.  If \(H=\lfloor A\sqrt m\rfloor\) and \(e^{A^2}\notin\mathbb Z\),
then

\[
 \frac W{N_H}\longrightarrow e^{A^2},\qquad
 \frac{r_H}{N_H}\longrightarrow\{e^{A^2}\}>0,      \tag{3.9}
\]

so (3.8) is \(\Theta_A(\sqrt m)\), not \(o(1)\).  At the exceptional
values \(e^{A^2}\in\mathbb Z\), the remainder depends on the integer floor
and the rounding of \(H\); there is no uniform Gaussian conclusion.

## 4. What an abstract SCD bank does and does not provide

Put

\[
                         d_q=s_q-q.                \tag{4.1}
\]

### Lemma 4.1 (abstract nested SCD bank)

For \(H=o(\sqrt m)\) and all sufficiently large \(m\), there are lower and
upper families \(D_q^\pm\), \(q\le H\), with

\[
 |D_q^-|=|D_q^+|=d_q,                              \tag{4.2}
\]

and designated same-chain descendants from every selected shallow target
to a selected depth-\(H\) target.

#### Proof

First,

\[
 d_{q+1}-d_q
 =N_q-N_{q+1}-1
 =N_q\frac{2q+1}{m+q+1}-1>0                       \tag{4.3}
\]

for all sufficiently large \(m\).  Also \(d_H<N_H\), since cap two gives
\(s_H<N_H\).

Fix an SCD of \(2^{[2m]}\).  Exactly \(N_H\) of its chains meet rank
\(m-H\).  Choose nested index sets of those long chains,

\[
 J_1\subseteq J_2\subseteq\cdots\subseteq J_H,
 \qquad |J_q|=d_q.                                \tag{4.4}
\]

For each chain in \(J_q\), take its rank-\((m-q)\) and rank-\((m+q)\)
members.  These are distinct families of the claimed sizes.  Because
\(J_q\subseteq J_H\), continuing on the same chain gives the designated
depth-\(H\) descendants. \(\square\)

This is only a cardinal-and-nesting lemma.  To be the completed high-load
profile of one exact owner successor, after adjoining the \(q\) seam
targets the families \(\widehat D_q^\pm\), of size \(s_q\), must satisfy
one common run line:

\[
 \widehat h_{q,v}^-
 =\frac{(m-q)s_q}{2m}
  -q\left(R_v-\frac W{2m}\right),                 \tag{4.5}
\]

\[
 \widehat h_{q,v}^++\widehat h_{q,v}^-=s_q,
 \qquad R_v\in\mathbb Z_{\ge0},\quad\sum_vR_v=W.  \tag{4.6}
\]

An arbitrary choice of the chain sets \(J_q\) need not satisfy, and has
not been shown to satisfy, (4.5)--(4.6).  Even satisfying these point equations would not imply the
semigroup identities or the memory circulation.

There is also an exact symmetry obstruction.

### Lemma 4.2 (no full-orbit proper descendant map)

Let \(0<\ell<k<n\).  There is no map

\[
 \sigma:\binom{[n]}k\longrightarrow\binom{[n]}\ell             \tag{4.7}
\]

such that

\[
 \sigma(T)\subset T,qquad
 \sigma(\pi T)=\pi\sigma(T)\quad
 (\pi\in S_n).                                    \tag{4.8}
\]

#### Proof

Fix \(T\).  Its stabilizer contains the full symmetric group on \(T\).
Equivariance makes \(\sigma(T)\) invariant under that group.  The only
invariant subsets of \(T\) are \(\varnothing\) and \(T\), contradicting
\(0<\ell<k\). \(\square\)

Thus a fixed SCD descendant cannot be combined with the full relative
coordinate orbit used in Theorem 3.2.  A positive construction needs a
smaller balanced hash group, an orbit of pairs \((\text{hash},\text{collar})\),
or a different exact operation.  Uniform deepest marginals, nested charge,
the common run line, and memory consistency must all be checked in that new
system.

For the full \(S_{2m}\)-orbit there is an equivalent set-family
formulation.  The orbit of one nested pair of ranks \(m-q\) and \(m-H\)
contains every pair \(S\subset T\) of those ranks.  Hence (3.2) for every
full-orbit shore forces

\[
 \partial^{\,H-q}D_q^-\subseteq D_H^-,
 \qquad
 \nabla^{\,H-q}D_q^+\subseteq D_H^+.               \tag{4.9}
\]

Choosing one SCD descendant of each shallow target proves neither
containment.  Conversely, (4.9) makes the nested-charge implication hold
for every possible full-orbit descendant.  This is the exact dichotomy:
keeping the SCD bank fixed destroys orbit compatibility, while transporting
the bank with the collar transports the collisions and ceases to be a
relative orbit.

### 4.3 Cap-two cost ledger

Uniformly for \(H=o(\sqrt m)\), with \(H\to\infty\),

\[
 s_q=(1+o(1))\frac{Wq^2}{m},\qquad
 \sum_{q=1}^Hd_q
 =\left(\frac13+o(1)\right)\frac{WH^3}{m}.          \tag{4.10}
\]

Without \(H\to\infty\), the uniform leading form is

\[
 \sum_{q=1}^Hd_q
 =(1+o(1))\frac Wm\frac{H(H+1)(2H+1)}6.             \tag{4.10a}
\]

Thus the entire nested duplicate bank has \(o(W)\) mass exactly in the
range \(H=o(m^{1/3})\).  At that same scale the remaining sufficient
ledgers are

\[
\begin{array}{c|c}
\text{resource or error}&\text{sufficient bound}\\ \hline
\text{bulk blocked row/column incidences}&H^3=o(m),\\
\text{nested terminal collision}&H^3=o(m),\\
\text{uncharged signed seam slots }u_H&u_HH^2=o(m),\\
\text{owner leave }\Lambda&\Lambda H=o(W),\\
\text{linear-path factor collars, }K\text{ paths}&KH=o(W),\\
\text{bare-cycle singleton repair, }K\text{ cuts}&KH^2=o(W),\\
\text{full cyclic collars, }K\text{ cycles}&KH=o(W),\\
\text{arbitrary changed successor tails }s&sH^2=o(W).
\end{array}                                                        \tag{4.11}
\]

The last row is the exact surgery estimate
\(sH(H+1)\) from the run-invariant report.  The leave row follows because
one missing owner contributes at most one missing target per sign and
depth.  A bare linearized cycle first pays the finite-factor overhead
\(H\), then can lose \(H(H+1)\) signed occurrences; a full collar pays
\(2H\) and loses none.  These constants are proved again in Section 8.
This table is complete only for the displayed cap-two terminal/preload
ledgers.  A constant-one endgame additionally needs compiler safety,
central length or overload \(W+o(W)\), aggregate physical defect \(o(W)\),
and the product-SCD tail condition; Section 8 records them explicitly.

This complete ledger also exposes the scale mismatch.  The product-SCD
outer tail is \(o(W)\) only when \(H/\sqrt m\to\infty\), whereas every
cap-two nested-bank term in (4.10)--(4.11) stops at or before
\(m^{1/3}\).  Hence the nested cap-two architecture cannot itself reach
the tail-killing regime.

## 5. Sharp barriers to local marginal arguments

### 5.1 Fractional depth-\(H\) barrier

Let \(\mathcal E\) be a shore orbit whose induced target hypergraph is
vertex-transitive at depth \(H\).  Regard its
sets of \(H\) deepest lower targets as the edges of an \(H\)-uniform regular
hypergraph on \(N_H\) vertices.

### Proposition 5.1

Its fractional transversal number is exactly

\[
                            \tau^*=\frac{N_H}{H}.   \tag{5.1}
\]

#### Proof

The constant vertex weight \(1/H\) is a fractional cover, so
\(\tau^*\le N_H/H\).  If the hypergraph has \(M\) edges and vertex degree
\(d\), regularity gives \(dN_H=MH\).  Summing all edge constraints of an
arbitrary fractional cover \(x\) gives

\[
 d\sum_vx_v\ge M,
\]

and hence \(\sum_vx_v\ge M/d=N_H/H\). \(\square\)

Since

\[
 d_H\sim s_H\sim N_H\frac{H^2}{m},
 \qquad
 \frac{d_H}{\tau^*}\sim\frac{H^3}{m},             \tag{5.2}
\]

the duplicate budget reaches fractional blocking capacity at exactly
\(H\asymp m^{1/3}\).  This is not an integral transversal construction;
it proves the sharp limit of arguments using only target cardinalities,
transitivity, and uniform marginals.

### 5.2 Short-core correlation barrier

Let \(1\le q\le H\le m^{1/3}\), let \(k=m\pm q\), and let
\(S_1,\ldots,S_L\) be \(k\)-targets with

\[
 \left|\bigcap_{j=1}^LS_j\right|\ge k-b.           \tag{5.3}
\]

For a fixed \(r\)-set \(R\), put

\[
 \mathcal D_R=\{T\in\tbinom{[2m]}k:R\subseteq T\}.             \tag{5.4}
\]

Under a uniform coordinate permutation \(\pi\),

\[
 p:=\Pr(\pi S_j\in\mathcal D_R)
 =\frac{\binom kr}{\binom{2m}r},                  \tag{5.5}
\]

whereas

\[
\begin{aligned}
 \Pr(\pi S_j\in\mathcal D_R\text{ for every }j)
 &\ge\frac{\binom{k-b}r}{\binom{2m}r}\\
 &=p\prod_{i=0}^{r-1}\left(1-\frac b{k-i}\right)\\
 &\ge p\left(1-\frac{br}{k-r+1}\right).          \tag{5.6}
\end{aligned}
\]

The last inequality is \(\prod_i(1-x_i)\ge1-\sum_i x_i\).
Choosing an integer \(r\) with

\[
 r=\log_2\frac{m}{q^2}+O(1)                                  \tag{5.7}
\]

makes \(p=\Theta(q^2/m)\).  If \(b=O(H)\) and
\(H\le m^{1/3}\), then \(br/m=o(1)\).  All alternatives therefore
collide together with probability \((1-o(1))p\), not \(p^L\).

This proposition is a budget-level obstruction.  The star family need not
satisfy the common run line or arise from an actual Hamilton preload.  It
therefore rules out a universal proof from cardinality plus short-core
alternatives, not every run-compatible hash construction.  The latter must
be certified through (4.5)--(4.6) and the memory circulation.

## 6. The common-run invariant: exact audit and consequence

### 6.1 Semigroup and fractional-circulation audit

For independently prescribed nested lower and upper flags, put
\(\mathcal M=\binom{[2m]}m\) and define the induced middle maps

\[
 R_j(X)=\bigl(X\setminus A_j^*(X)\bigr)\cup B_j^*(X).
\]

The power-consistency theorem in the run-invariant report is exact: one
owner permutation realizes all prescribed flags through depth \(H\) if
and only if

\[
 R_1\in\operatorname{Sym}(\mathcal M),
 \qquad R_j=R_1^j\quad(0\le j\le H).               \tag{6.0a}
\]

Necessity is immediate from \(R_j(X)=P^jX\).  Conversely, (6.0a), together
with the prescribed one-step nested deletions and additions, makes
\(P=R_1\) follow exactly those flags; geodesicity then identifies their
intersections and unions.  Thus separate depthwise integral SCD flows do
not compose unless (6.0a) is proved.

The root and \((H-1)\)-memory overlap equations are likewise an exact
integral formulation: root mass one makes every selected safe-path column
binary, and balanced prefix/suffix degrees decompose the selected memory
edges into directed cycles, defining one successor permutation.  On the
other hand, averaging every coordinate conjugate of one wreath cycle gives
a feasible *fractional* circulation with the uniform signed target load

\[
                         \mu_j^\pm=\frac W{N_j}.    \tag{6.0b}
\]

Coordinate transitivity and total target mass \(W\) prove (6.0b).  Hence
there is no fractional Hall obstruction; the obstruction under discussion
is integral chronology.

### 6.2 Common run line

For an \(H\)-safe owner successor, let \(R_v\) be the number of cyclic
membership runs of coordinate \(v\).  The audited identities are

\[
 B_{m-j}\mu_j^-=\frac W2\mathbf1-jR,\qquad
 B_{m+j}\mu_j^+=\frac W2\mathbf1+jR,               \tag{6.1}
\]

and

\[
                         \sum_vR_v=W.              \tag{6.2}
\]

If two exact \(H\)-safe factors on the same owner support have histogram
difference \(g_j^\pm\) and run-vector difference \(\Delta R\), subtraction
gives the strongest universal all-depth point law

\[
 \boxed{
 B_{m-j}g_j^-=-j\Delta R,\qquad
 B_{m+j}g_j^+=j\Delta R.}                          \tag{6.3}
\]

Thus point effects at separate depths cannot be selected independently.
A run-neutral trade has

\[
 B_{m-j}g_j^-=B_{m+j}g_j^+=0                       \tag{6.4}
\]

for every \(j\), but it may still move full target histograms inside these
point-incidence kernels.  The run invariant and shadow-lock are therefore
independent: (6.4) does not prevent a fibre from being completely locked.

The audited \(H\)-safe condition forces cyclic coordinate runs of length
at least \(H\), not \(H+1\).  This is precisely why the compiler condition
\(P_H\) introduced in Section 8 is an additional hypothesis.

### 6.3 Exact arithmetic obstructions and their scope

At \(m=3,H=2\), one has

\[
 W=20,\qquad N_2=6,qquad c_2=3,qquad r_2=2.
\]

Every depth-two lower target is a singleton, and (6.1) gives

\[
                         \mu_2^-(\{v\})=10-2R_v.    \tag{6.5}
\]

Every such load is even.  Exact balance would allow only \(3\) or \(4\),
so all six loads would have to equal \(4\), contradicting their total
mass \(W=20\).  Thus the report's finite exact-balance counterexample is
valid.  It refutes a universal exact recursion, not asymptotic near-balance.

More generally, exact balance at the full depth \(j=m-1\) forces
\(2m\mid\binom{2m}{m}\), and therefore fails when \(m\) is an odd prime.
Indeed, all singleton loads are congruent to \(W/2\pmod{m-1}\); the two
consecutive balanced values cannot both have that residue when \(m\ge3\).
If the division by \(2m\) has nonzero remainder, both values must occur,
a contradiction, so every singleton load is equal and \(2m\mid W\).
For an odd prime \(m=p\),

\[
 \binom{2p}{p}
 =2\prod_{i=1}^{p-1}\frac{p+i}{i}
 \equiv2\pmod p,
\]

so the divisibility fails.  This is a full-depth obstruction and has no
force against the desired Gaussian regime \(H=o(m)\).

### 6.4 Exact shadow lock

Let a lower depth-\(q\) target \(T\) still need an occurrence, while every
child \(S\in\partial T\) is already at its depth-\((q+1)\) cap.  Any new
nested safe flag containing \(T\) at depth \(q\) contains some such
\(S\) at depth \(q+1\), so an addition-only collar necessarily violates a
child cap.  The upper statement is dual, with every
\(V\in\nabla U\) saturated.  This proves the source shadow-lock lemma
exactly.  It blocks addition-only extension, not a simultaneous signed
replacement; Section 7 identifies the exact replacement equations.

## 7. Exact owner-internal escape: a memory-kernel unlocking trade

Let \(\Gamma_H\) be the safe \(H\)-path columns.  Let \(A\) be the
root-owner matrix, \(M\) the prefix-minus-suffix memory matrix, \(D\) the
first-deletion matrix, and \(S_j^\pm\) the signed target matrices.  Fix an
integral base circulation \(z\), so

\[
 z\ge0,\qquad Az=\mathbf1,\qquad Mz=0.             \tag{7.1}
\]

### Theorem 7.1 (exact memory-kernel trade criterion)

An integer vector \(\delta\) produces another integral, \(H\)-safe,
run-neutral successor satisfying prescribed target intervals
\(\ell_j^\pm\le\mu_j^\pm\le u_j^\pm\) if and only if

\[
\boxed{
\begin{aligned}
 z+\delta&\ge0,\\
 A\delta&=0,\\
 M\delta&=0,\\
 D\delta&=0,\\
 \ell_j^\pm-S_j^\pm z
 \le S_j^\pm\delta
 &\le u_j^\pm-S_j^\pm z
 \qquad(1\le j\le H).
\end{aligned}}                                                     \tag{7.2}
\]

#### Proof

Necessity follows by subtracting the two owner, memory, run, and cap
systems.  Conversely, the first three lines make \(z+\delta\) an integral
safe-path circulation, hence an \(H\)-safe owner permutation.  The fourth
line preserves its common run vector, and the last line is exactly target
cap/floor feasibility. \(\square\)

If the owner factor must retain an additional fixed fibre or
\(D_r\)-transversal system encoded by rows \(Cz=b\), one must also impose
\(C\delta=0\), or restrict \(\Gamma_H\) from the outset to fibre-legal
columns.  The unrestricted equations (7.2) do not silently encode that
extra structure.

For adjacent lower depths \(1\le q<H\), define the projected signed flow

\[
 p_{q,T,S}(\delta)
 =\sum_{\gamma:L_q(\gamma)=T,\ L_{q+1}(\gamma)=S}\delta_\gamma,
 \qquad S\in\partial T.                           \tag{7.3}
\]

Its two marginals are the depth-\(q\) and depth-\((q+1)\) histogram
effects.  If \(T\) is fully locked, every \(S\in\partial T\) is saturated.
If a cap-safe trade has \((S_q^-\delta)_T>0\), then for some
\(S\in\partial T\)

\[
 p_{q,T,S}>0
 \quad\text{and}\quad
 p_{q,T',S}<0                                      \tag{7.4}
\]

for another \(T'\supset S\), necessarily with \(T'\ne T\).  Thus every
legal unlocking contains the
alternating shadow pivot

\[
                         T\longrightarrow S\longleftarrow T'. \tag{7.5}
\]

The upper analogue is \(U\to V\leftarrow U'\), with \(V\in\nabla U\).
The projected pivot is necessary, not sufficient: it may fail to lift
through the root and memory kernels or may violate another depth or sign.

Equations (7.2)--(7.5) identify the exact escape operation without invoking
an independently switchable component atlas.  What remains unproved is an
abundance theorem giving signed kernel trades with
\(\delta^-\le z\), an integral memory lift, simultaneous other-depth and
opposite-sign slack, short support, bounded overlap, fibre legality,
controlled cycle toll, and a literal word implementation.

## 8. Literal support-only escape for coefficient one

Exact target multiplicities are stronger than literal contiguous-OR
coverage.  There is an essential off-by-one chronology distinction.  In
this section a path is called **compiler-safe through depth \(H\)** when
every block of at most \(H\) transitions is Johnson-geodesic (condition
\(G_H\)) and every internal positive coordinate run has at least \(H+1\)
states (condition \(P_H\)).  These are the two hypotheses needed by the
finite delay-factor lemma.  The audited owner condition \(G_H\) alone
certifies the rank-correct trace windows but forces only \(P_{H-1}\), not
\(P_H\).

### Theorem 8.1 (cap-two support and literal path conversion)

Let \(1\le H\le m-1\), and let

\[
                         X_1,\ldots,X_W             \tag{8.1}
\]

be an \(H\)-geodesic Hamilton path through all middle owners, meaning that
every block of at most \(H\) transitions is a Johnson geodesic.  Assume the
cap-two regime and, at every signed depth \(q\le H\), pointwise internal
load at most two and

\[
                         |D_q^\pm|\le s_q-q,        \tag{8.2}
\]

where \(D_q^\pm\) is the family of targets of internal load two.  Then
every target at every protected signed depth has positive internal load.
If, in addition, the path is compiler-safe through depth \(H\), all these
internal targets have a literal contiguous-OR word of length at most
\(W+H\).

#### Proof

Let \(z_q\) and \(d_q\) be the numbers of zero and double loads for one
sign and depth.  Rank-correctness follows from geodesicity.  The internal
total-load identity is

\[
 W-q=N_q-z_q+d_q=N_q+s_q-q.
\]

Thus \(d_q-z_q=s_q-q\).  Since \(d_q\le s_q-q\), one has
\(z_q=0\).  Apply this separately to both signs and every depth.

This proves trace support under the geodesic hypothesis.  Under the
additional compiler-safety hypothesis, define

\[
 A_j=\bigcap_{i=\max(1,j-H)}^{\min(W,j)}X_i,
 \qquad 1\le j\le W+H.                              \tag{8.3}
\]

Coordinatewise condition \(P_H\) gives

\[
 X_i=\bigcup_{j=i}^{i+H}A_j,
\quad
 \bigcap_{i=a}^{b}X_i=\bigcup_{j=b}^{a+H}A_j
 \quad(b-a\le H),                                  \tag{8.4}
\]

and, without a restriction on \(b-a\),

\[
                         \bigcup_{i=a}^{b}X_i
                         =\bigcup_{j=a}^{b+H}A_j.   \tag{8.5}
\]

Indeed, a coordinate which is present at a given state lies in a positive
run reaching a boundary or containing at least \(H+1\) states, hence lies
in a defining intersection \(A_j\) with the required endpoint; the
reverse inclusions are immediate.  Taking the union over \(i\) proves
(8.5).  Therefore \((A_1,\ldots,A_{W+H})\) is the desired factor word.
Empty entries may be deleted. \(\square\)

Theorem 8.1 is a shallow cap-two statement.  In particular, it does not by
itself reach \(H/\sqrt m\to\infty\), and an arbitrary Hamilton path has no
cyclic run vector whose preservation could be asserted.

### Theorem 8.2 (exact partial-collar/singleton ledger)

Let an even-dimensional central owner factor consist of \(K\)
cyclically compiler-safe cycles \(C\) through depth \(H\), meaning cyclic
\(G_H+P_H\), of lengths \(v_C\) summing to
\(W\).  Assume their cyclic lower and upper flag support covers every
target in ranks \(m-H,\ldots,m+H\).  For each cycle choose an integer

\[
                         0\le\sigma_C\le H.         \tag{8.6}
\]

Cut it, copy \(\sigma_C\) initial owner states, apply the finite
delay-factor compiler, and append once every physical central target which
is still missing.  This gives a literal central word of length at most

\[
\boxed{
 W+HK+\sum_C\sigma_C
 +2\sum_C\sum_{q=1}^H(q-\sigma_C)_+ .}             \tag{8.7}
\]

Equivalently, since

\[
 2\sum_{q=1}^H(q-\sigma)_+
 =(H-\sigma)(H-\sigma+1),                           \tag{8.8}
\]

the last two terms per cycle are

\[
                         \sigma_C+
 (H-\sigma_C)(H-\sigma_C+1).                       \tag{8.9}
\]

In particular, bare cuts and full collars give respectively

\[
 \boxed{W+HK+KH(H+1)},\qquad
 \boxed{W+2HK}.                                    \tag{8.10}
\]

#### Proof

The extended linear owner row for \(C\) has \(v_C+\sigma_C\) states, and
the factor compiler contributes exactly \(H\) further positions before
empty entries are deleted.  At signed depth \(q\), precisely
\((q-\sigma_C)_+\) cyclic starts on each sign are unavailable.  Thus the
number of physical targets which become missing is no larger than the
two-sided occurrence count in (8.7).  Appending a missing nonempty target
as one letter realizes it as a length-one OR interval and cannot destroy
an old witness.  Summing over cycles proves (8.7), and (8.8)--(8.10) are
arithmetic. \(\square\)

The operations in Theorem 8.2 do not alter the underlying cyclic owner
successor or its common run vector; they choose a literal representation
and append external repair letters.  Singleton repair also bypasses the
shadow-lock premise: it does not request a nested return-free
\((q+1)\)-window containing the repaired target.

### Corollary 8.3 (even composition with the proved product-SCD tail)

Let \(H=H_m\le m-1\) satisfy

\[
                         H/\sqrt m\longrightarrow\infty.       \tag{8.11}
\]

Under the hypotheses of Theorem 8.2, let \(L_m(m-H-1)\) be the proved
even product-SCD exterior length.  Then

\[
\boxed{
 \nu(2m)\le
 W+HK+\sum_C\sigma_C
 +2\sum_C\sum_{q=1}^H(q-\sigma_C)_+
 +L_m(m-H-1).}                                      \tag{8.12}
\]

Since \(L_m(m-H-1)=o(W)\), either of the following is sufficient for
\(\nu(2m)=(1+o(1))W\):

\[
 \begin{array}{c|c}
 \text{literalization choice}&\text{sufficient cycle ledger}\\ \hline
 \sigma_C=0\text{ for every }C&KH^2=o(W),\\
 \sigma_C=H\text{ for every }C&KH=o(W).
 \end{array}                                         \tag{8.13}
\]

If Stage A is already a literal central word of length \(W+o(W)\), no
owner-cycle hypothesis is needed: concatenate it directly with the
factor-blind product-SCD tail.

Thus the exact terminal multiplicity absorber is not a separate
coefficient-one gate.  The corollary remains conditional on a
compiler-safe full-support central construction; neither Theorem 8.1
nor the two audited source reports construct it at super-Gaussian depth.

There is a sharper near-factor form.  Suppose compiled cyclic rows contain
\(\mathsf P=W-M_0+E_0\) middle-owner occurrences, where \(M_0\) distinct middle
owners are missing and \(E_0\) is the middle overload.  Let

\[
                         \Delta_H=
 \sum_{q=1}^H(M_q^-+M_q^+)                         \tag{8.14}
\]

be the actual physical signed defect after full cyclic support is
measured.  Full atom-prefix linearization and literal completion give the
exact factor-blind inequality

\[
 \boxed{\nu(2m)\le
 W+E_0+2HK+\Delta_H+L_m(m-H-1).}                   \tag{8.15}
\]

Indeed, the compiled rows cost \(\mathsf P+2HK\), appending the \(M_0\) missing
middle owners changes \(\mathsf P\) to \(W+E_0\), and every remaining physical
hole costs one literal.  Consequently the quantitatively smallest
central hypothesis isolated here is

\[
                         E_0+HK+\Delta_H=o(W),      \tag{8.16}
\]

together with compiler safety and \(H/\sqrt m\to\infty\).  The middle
leave \(M_0\) itself need not be \(o(W)\); it cancels exactly in the mass
identity.

### 8.4 Parity ledger

The correlated-row theorem audited above is even-dimensional.  To avoid
silently exporting its floor identities to odd dimension, here is the
exact odd compiler ledger.  Put

\[
 W_o=\binom{2m+1}{m},\qquad
 N_q^o=\binom{2m+1}{m-q}=\binom{2m+1}{m+1+q}.       \tag{8.17}
\]

For this odd paragraph, **odd compiler-safe through depth \(H\)** means
\(G_{H+1}\): every block of at most \(H+1\) transitions in the cyclic
\(X\)-sequence is Johnson-geodesic.  This implies the positive-dwell
condition \(P_H\) needed by the delay-\(H\) factor compiler.  The stronger
geodesic index is necessary because an upper depth-\(H\) target uses
\(H+2\) states.

Let \(K\) odd-compiler-safe alternating \(X/Y\) cycles have total
\(X\)-length \(W_o\), partition both middle shores, and have full cyclic
signed support on \([m-H,m+H+1]\).  A lower depth-\(q\) target uses \(q+1\)
consecutive \(X\)-states and an upper target uses \(q+2\).  For partial
collars \(0\le\sigma_C\le H+1\), with \(z_0\) the number having
\(\sigma_C=0\), the same proof gives

\[
\boxed{\begin{aligned}
 L_{\rm odd}\le{}&W_o+HK+\sum_C\sigma_C+z_0\\
 &+\sum_C\sum_{q=1}^H
 \bigl((q-\sigma_C)_++(q+1-\sigma_C)_+\bigr).
\end{aligned}}                                       \tag{8.18}
\]

Thus a bare cut costs at most \(W_o+H+(H+1)^2\) for one cycle, while
full collars on \(K\) cycles cost

\[
                         W_o+(2H+1)K.               \tag{8.19}
\]

The protected odd band is \([m-H,m+H+1]\), and the exterior word costs
\(2L_m(m-H-1)\).  Hence the full-collar odd analogue of (8.12) is

\[
 \nu(2m+1)\le W_o+(2H+1)K+2L_m(m-H-1).             \tag{8.20}
\]

Finally, if \(W_o=c_qN_q^o+r_q\) and one bare Hamilton path has only the three loads
\(c_q-1,c_q,c_q+1\), then its exact floor/remainder identities are

\[
 |D_q^-|-|E_q^-|=r_q-q,\qquad
 |D_q^+|-|E_q^+|=r_q-(q+1).                         \tag{8.21}
\]

Accordingly, in the odd no-deficit regime \(r_H\ge H+1\), and under
uniform deepest-slot marginals, the deepest collision union bound is

\[
 H\frac{r_H-H}{N_H^o}
 +(H+1)\frac{r_H-(H+1)}{N_H^o},                    \tag{8.22}
\]

not the even expression (3.8).  No odd nested-charge construction is
claimed here.

## 9. Precise proved/conditional boundary

### Proved

1. The two audited source ledgers and the common run-vector theorem are
   correct, with the minor corrections in Section 1.
2. Nested collision charging improves the terminal exponent from \(1/4\)
   to \(1/3\) under the explicit shorewise condition (3.2).
3. An abstract nested SCD bank realizes all required cardinalities.
4. Full coordinate-orbit equivariance is incompatible with a fixed proper
   descendant map.
5. Uniform-marginal/cardinality reasoning has a sharp fractional barrier at
   exponent \(1/3\), and short-core alternatives do not generically square
   bad densities.
6. The exact owner-internal shadow escape is the memory-kernel trade
   (7.2), with forced alternating pivot (7.5).
7. The finite delay-factor compiler plus either full collars or literal
   singleton repair bypasses exact terminal multiplicity closure whenever
   a compiler-safe full-support central factor is already available.  The
   exact even ledgers are (8.12)--(8.16), and the parity correction under
   \(G_{H+1}\) is (8.18)--(8.22).

### Not proved

1. No nested/hash/SCD bank is shown to satisfy simultaneously the common
   run line, semigroup consistency, integral memory circulation, and a
   relative balanced shore action.
2. No abundance theorem for memory-kernel unlocking trades is proved.
3. No internal central-band owner successor/path cover is constructed at
   \(H/\sqrt m\to\infty\).  In particular, shallow cap-two support from
   Theorem 8.1 cannot be combined directly with the super-Gaussian tail.

The smallest remaining constant-one hypothesis isolated by this lane is
therefore a compiler-safe internal central construction with full support
(or aggregate literal defect \(o(W)\)) and the mass/defect ledger (8.16),
together with its odd \(G_{H+1}\) analogue.  Exact
terminal quota balancing and independent coordinate-orbit collision
avoidance are not required.  No claim is made about the already closed
component-switch or fixed-atlas lanes.
