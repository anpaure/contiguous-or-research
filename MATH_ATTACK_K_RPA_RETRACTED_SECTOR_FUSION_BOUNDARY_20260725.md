# Lane K: the retracted terminal-sector reservoir and the exact protected-spine boundary

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Outcome

Put

\[
 N=2r+1,\qquad B_r=\operatorname{Cat}_r,\qquad W=NB_r,
 \qquad \tau=\phi^2.
\]

The requested primitive/terminal-max fusion cannot be founded on
`PBBS_ZERO_WINDING_CONVERSE_AND_RPA_COUNTEREXAMPLE_20260725.md`.
That file is explicitly retracted, and its failure occurs before any seam
or literal-fusion question: a primitive terminal-max root need not have the
claimed return port.

This report gives the exact correction.

1. The formal first-deepest-spine sector shift from the retracted report is
   canonically valid for a full height cycle if and only if every pre-spine
   forest is empty and every post-spine forest \(B_t\) has height at most
   \(t\).

2. On this corrected protected-spine class the claimed zero-winding return
   at gap \(2h+1\) is valid, with the exact strict pre-return difference
   \(h-j\) after \(j<h\) two-step moves.

3. The protected class has size

   \[
    \boxed{
    |\mathcal P_r|\le C B_r e^{-c r^{1/3}} }
    \tag{0.1}
   \]

   for absolute constants \(c,C>0\). Thus at Gaussian depth
   \(H=O(\sqrt r)\), even an \(O(H^2)\) literal repair for every physical
   occurrence has total cost

   \[
    O(H^2N|\mathcal P_r|)=o(W).
    \tag{0.2}
   \]

4. The primitive terminal-max word

   \[
    D_0=1110011000
   \]

   lies outside the protected class and has no claimed gap-seven return.
   The alleged two ports omit distinct coordinates. A coordinate
   conjugation preserves their inequality, so no literal fusion which
   identifies those alleged ports can include all primitive roots.

Consequently there is no Catalan-positive packet reservoir, and hence no
positive-density global braid, supplied by the named sector argument. The
status of \((\mathrm{RP}_A)\) reverts to **open**, exactly as stated in
Section 23 of `PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`. This report
does not prove \((\mathrm{RP}_A)\); it proves that its asserted disproof and
the requested terminal-sector fusion premise are invalid.

The corrected global target is the set of actual solutions of the
accumulated sector equation, with dynamic changes of the first deepest
spine. A braid for that set remains open.

## 1. Exact one-step sector transport

Let \(D\) be a Dyck word of semilength \(r\) and height \(h\). Along the
path to the first deepest leaf, let \(A_i\) and \(B_i\) be the ordered
forests before and after the spine child at depth \(i\), respectively.
Then

\[
 D=A_0\,1A_1\,1\cdots1A_{h-1}\,1\,
   0B_{h-1}0\cdots0B_1\,0B_0,
 \tag{1.1}
\]

and \(A_{h-1}=\varnothing\). If forest height is measured relative to
its attachment vertex, canonicity also gives

\[
 \operatorname{ht}(A_i)\le h-i-1,
 \qquad
 \operatorname{ht}(B_i)\le h-i.
 \tag{1.2}
\]

The empty forest has height zero; every nonempty forest has height at least
one. The strict loss of one in the first inequality is essential: an
\(A_i\)-forest reaching total depth \(h\) would encounter a deepest leaf
before the displayed spine.

For the canonical first-maximum factorization

\[
 D=P1R0S,
\]

one has

\[
 \tau D=S1P0R,
 \qquad d(D)=|S|+1,
 \qquad \delta(D)=|P|+1.
 \tag{1.3}
\]

Substitution of (1.1) into (1.3) gives the always-valid one-step word
identity

\[
 \tau D
 =B_0\,1A_0\,1A_1\cdots1A_{h-1}\,0\,
   0B_{h-1}0\cdots0B_1.
 \tag{1.4}
\]

It does **not** say that the displayed height-\(h\) spine in (1.4) remains
the canonical first deepest spine. That extra assertion is the exact point
at which the retracted proof fails.

## 2. Formal shift and its exact canonicality criterion

Starting with the sectors in (1.1), define the formal arrays

\[
 \widehat B_i^{(j)}=
 \begin{cases}
   B_{i+j},&i+j<h,\\
   \varnothing,&i+j\ge h,
 \end{cases}
 \tag{2.1}
\]

and

\[
 \widehat A_i^{(j)}=
 \begin{cases}
   B_{j-1-i},&0\le i<j,\\
   A_{i-j},&j\le i<h.
 \end{cases}
 \tag{2.2}
\]

These are the arrays asserted, without the needed hypotheses, in the
retracted sector-shift lemma.

### Theorem 2.1 (full-cycle protected-spine criterion)

For every \(0\le j\le h\), the arrays (2.1)--(2.2) are the canonical
first-deepest-spine sectors of \(\tau^jD\) if and only if

\[
 \boxed{
 A_i=\varnothing\quad(0\le i<h),
 \qquad
 \operatorname{ht}(B_t)\le t\quad(0\le t<h).}
 \tag{2.3}
\]

In particular (2.3) forces \(B_0=\varnothing\), hence \(d(D)=1\).

#### Proof: necessity

Assume (2.1)--(2.2) are canonical through time \(h\). Fix
\(0\le k<h\), and take \(j=h-1-k\). Formula (2.2) places the original
forest \(A_k\) in the last pre-spine sector:

\[
 \widehat A_{h-1}^{(h-1-k)}=A_k.
\]

For every canonical first-deepest-spine decomposition the last pre-spine
forest is empty: any child before the final spine child would itself be a
leaf at depth \(h\), reached earlier. Hence \(A_k=\varnothing\).

At time \(j=h\), formula (2.2) places \(B_t\) at pre-spine depth
\(h-1-t\):

\[
 \widehat A_{h-1-t}^{(h)}=B_t.
\]

The first inequality in (1.2), applied at that depth, gives

\[
 \operatorname{ht}(B_t)
 \le h-(h-1-t)-1=t.
\]

This proves (2.3).

#### Proof: sufficiency

Assume (2.3). At formal time \(j\), every nonempty pre-spine sector is a
transported \(B_t\), where \(t=j-1-i\) and \(i\) is its new attachment
depth. Its greatest possible total depth is

\[
 i+\operatorname{ht}(B_t)
 \le i+t=j-1<h.
 \tag{2.4}
\]

Thus no formal pre-spine forest reaches height \(h\), while the displayed
spine does. It is therefore the first deepest spine.

For completeness, a formal post-spine forest at depth \(i\) is
\(B_{i+j}\). The original canonical bound in (1.2) gives

\[
 i+\operatorname{ht}(B_{i+j})
 \le i+h-(i+j)=h-j\le h,
 \tag{2.5}
\]

so no sector exceeds the displayed height. Applying the exact one-step
identity (1.4) now advances the formal arrays by one step. Induction on
\(j\) proves that (2.1)--(2.2) are canonical through \(j=h\). \(\square\)

Call the roots satisfying (2.3) the **protected-spine class**
\(\mathcal P_r\).

## 3. The corrected zero-winding theorem

### Theorem 3.1 (protected-spine return)

If \(D\in\mathcal P_r\) has height \(h\), then its omitted coordinate has
its first return at gap

\[
 \boxed{2h+1,}
 \tag{3.1}
\]

and the return has zero winding.

#### Proof

Put \(D_j=\tau^jD\) and

\[
 C_j=\sum_{t=0}^{j-1}d(D_t).
\]

In this section \(|B_t|\) denotes the number of forest edges, so its
contour word has length \(2|B_t|\).

Theorem 2.1 and (1.3) give, for \(0\le j\le h\),

\[
 C_j=j+2\sum_{t<j}|B_t|,
 \qquad
 \delta(D_j)=h+2\sum_{t<j}|B_t|.
 \tag{3.2}
\]

Therefore the exact difference is

\[
 \boxed{\delta(D_j)-C_j=h-j.}
 \tag{3.3}
\]

It is positive for \(j<h\) and zero for \(j=h\). Also, since all
\(A_i\) vanish,

\[
 r=h+\sum_{t=0}^{h-1}|B_t|,
 \qquad
 C_h=2r-h<N.
 \tag{3.4}
\]

After \(j\) two-step moves the spatial phase is \(u-C_j\), and the next
odd move adds \(\delta(D_j)\). Equations (3.3)--(3.4) exclude every
earlier odd congruence and every earlier positive even congruence modulo
\(N\), while equality at \(j=h\) gives the zero-winding return. \(\square\)

This is the strongest theorem justified by the advertised fixed-spine
iteration. It is not a theorem about all roots with \(B_0=\varnothing\).

## 4. The protected class is not Catalan-positive

There is first an exact enumeration which makes the loss of the primitive
Catalan family transparent. Let \(C_L(z)\) be the generating function for
Dyck forests of height at most \(L\), normalized by

\[
 C_0(z)=1,
 \qquad
 C_L(z)=\frac1{1-zC_{L-1}(z)}.
 \tag{4.0}
\]

If \(p_{r,h}\) is the number of protected roots of semilength \(r\) and
height \(h\), then

\[
 \boxed{
 p_{r,h}=[z^{r-h}]
   \prod_{k=1}^{h-1}C_{\min(k,h-k)}(z).}
 \tag{4.1}
\]

Indeed a protected root is uniquely

\[
 1^h0B_{h-1}0B_{h-2}\cdots0B_1 0,
\]

and \(B_k\) has height at most \(k\) by protection and at most \(h-k\)
by its original attachment depth. Formula (4.1) follows by distributing
the remaining \(r-h\) edges independently among these forests.

### Theorem 4.1 (stretched-exponential Catalan deficit)

There are absolute constants \(c,C>0\) such that

\[
 |\mathcal P_r|\le C B_r e^{-c r^{1/3}}
 \tag{4.2}
\]

for all sufficiently large \(r\).

#### Proof

If \(D\in\mathcal P_r\) has height \(h\), then all \(A_i\) are empty,
so (1.1) begins with \(1^h\). Let \(F_r(h)\) denote the number of
semilength-\(r\) Dyck paths of height at most \(h\). The path-graph
spectral formula and \(\cos x\le e^{-x^2/2}\) give

\[
 F_r(h)
 \le \left(2\cos\frac{\pi}{h+2}\right)^{2r}
 \le 4^r\exp\!\left(-\frac{\pi^2r}{(h+2)^2}\right).
 \tag{4.3}
\]

Independently, after the forced prefix \(1^h\), forgetting the Dyck and
height restrictions gives

\[
 |\{D:D\text{ begins with }1^h\}|
 \le \binom{2r-h}{r-h}.
 \tag{4.4}
\]

Since

\[
 B_r=\frac1{r+1}\binom{2r}{r},
\]

the ratio in (4.4) satisfies

\[
 \frac{\binom{2r-h}{r-h}}{B_r}
 =(r+1)\prod_{a=0}^{h-1}\frac{r-a}{2r-a}
 \le(r+1)2^{-h}.
 \tag{4.5}
\]

Use also the Wallis lower bound \(B_r\ge c_0 4^r r^{-3/2}\).
Set \(R=\lfloor r^{1/3}\rfloor\). Summing (4.3) over \(h\le R\)
and dividing by \(B_r\) gives at most

\[
 C Rr^{3/2}e^{-c_1r^{1/3}}
 \le C'e^{-c_2r^{1/3}}.
 \tag{4.6}
\]

For \(h>R\), summing (4.5) gives at most

\[
 (r+1)\sum_{h>R}2^{-h}
 \le2(r+1)2^{-R}
 \le C'e^{-c_3r^{1/3}}.
 \tag{4.7}
\]

Combining the two ranges proves (4.2). \(\square\)

### Corollary 4.2 (literal individual repair is already negligible)

Uniformly for \(H=O(\sqrt r)\),

\[
 H^2N|\mathcal P_r|=o(W).
 \tag{4.8}
\]

Indeed (4.2) and \(W=NB_r\) make the ratio in (4.8) at most
\(O(r e^{-cr^{1/3}})=o(1)\). Thus the already audited endpoint-capped
literal repair, even charged separately at \(O(H^2)\) for every physical
protected-spine occurrence, has \(o(W)\) overhead. No shared braid is
needed to repair this class. More precisely, any modification whose changed
physical occurrences are confined to these protected roots has \(o(W)\)
support. This does not exclude using a protected root merely as an anchor
for a genuinely nonlocal braid with macroscopic support elsewhere.

## 5. Exact primitive counterexample and literal port obstruction

Take

\[
 D_0=1110011000.
 \tag{5.1}
\]

It is primitive, has semilength five and height three, and therefore has
terminal root forest \(B_0=\varnothing\). Its first-deepest sectors have
all \(A_i=\varnothing\), but

\[
 B_1=1100,
 \qquad \operatorname{ht}(B_1)=2>1,
 \tag{5.2}
\]

so it fails precisely the protection condition in Theorem 2.1.

Direct canonical factorizations give

\[
\begin{array}{c|c|c|c}
j&D_j=\tau^jD_0&\delta(D_j)&d(D_j)\\ \hline
0&1110011000&3&1\\
1&1110001100&3&5\\
2&1100111000&7&1.
\end{array}
 \tag{5.3}
\]

Moreover \(\tau D_2=D_0\). Thus the accumulated deficits at the two
proper odd tests are

\[
 1\ne3,
 \qquad
 1+5=6\ne7,
 \tag{5.4}
\]

and at the alleged height-three endpoint they give

\[
 1+5+1=7\not\equiv\delta(D_3)=3\pmod {11}.
 \tag{5.5}
\]

Starting with omitted coordinate \(u\), the alleged time-seven endpoint
therefore omits

\[
 u-7+3=u-4\pmod {11},
 \tag{5.6}
\]

not \(u\). Every coordinate permutation sends these two distinct labels
to two distinct labels. Hence independently conjugating the factor cannot
turn (5.6) into a return port.

For completeness, the true first return on this example has gap thirteen.
The accumulated deficits and terminal first-maximum positions through six
two-step moves are

\[
\begin{array}{c|rrrrrrr}
j&0&1&2&3&4&5&6\\ \hline
C_j&0&1&6&7&8&13&14\\
\delta(D_j)&3&3&7&3&3&7&3.
\end{array}
 \tag{5.7}
\]

No positive \(C_j\) with \(j<6\) is zero modulo eleven, and no proper
odd comparison is equal modulo eleven. At \(j=6\), however,
\(C_6=14\equiv3=\delta(D_6)\pmod {11}\). This confirms that the failed
gap-seven port is not an indexing convention: it is a genuinely different
return interval.

This is a literal obstruction, not merely a counting objection. A splice
which identifies the start and alleged terminal port for every primitive
root would identify two different omitted coordinates on (5.1), and so
would not be a legal PBBS/MTF fusion. One may insert a genuine bridge
between those states, but its existence, support, and cost require a new
construction; they do not follow from the terminal-sector argument.

## 6. Why a shared primitive-sector braid cannot be extracted

The retracted construction used the following implication:

\[
 B_0=\varnothing
 \Longrightarrow
 \text{a common length-}(2h+1)\text{ zero-winding packet}.
 \tag{6.1}
\]

Equation (5.5) disproves (6.1). Theorem 2.1 shows that the fixed sector
atlas can certify (6.1) only on \(\mathcal P_r\), and Theorem 4.1 shows
that this certified atlas has vanishing, indeed stretched-exponentially
small, Catalan density.

Accordingly neither proposed economy can be invoked:

* there are not \(\Theta(B_r)\) certified terminal-sector packets whose
  physical lifts can share one phase-deck braid;
* there is no common terminal port for all primitive roots, even before
  checking Johnson seams, MTF states, flags, or component count.

An arbitrary global braid might leave the fixed-spine atlas, recompute the
first deepest sector after every transport, and connect distinct ports.
Nothing here rules that out. But such a braid is not a fusion supplied by
the named decomposition, and no \(o(H^2)\)-per-cut or \(o(W)\) estimate
has been proved for it.

## 7. Corrected exact target

For \(D_j=\tau^jD\), write the canonical factorization at every dynamic
time as

\[
 D_j=P_j1R_j0S_j,
 \qquad
 d_j=|S_j|+1,
 \qquad
 \delta_j=|P_j|+1.
 \tag{7.1}
\]

The genuine zero-winding starts of odd gap \(2s+1\) are exactly

\[
 \mathcal Z_{r,s}
 =\left\{D:
   \sum_{j=0}^{s-1}d_j=\delta_s,
   \quad
   \sum_{j=0}^{t-1}d_j\not\equiv\delta_t\pmod N
   \ (0\le t<s)
  \right\},
 \tag{7.2}
\]

with the analogous nonreturn conditions at positive even times. The
canonical first deepest spine in (7.1) is allowed to change.

Zero winding is only the subcase in which the terminal congruence is a
literal equality. The full family of actual consecutive odd returns is

\[
 \mathcal R_{r,s}
 =\left\{D:
   \sum_{j=0}^{s-1}d_j\equiv\delta_s\pmod N,
   \quad
   \sum_{j=0}^{t-1}d_j\not\equiv\delta_t\pmod N
   \ (0\le t<s),
   \quad
   \sum_{j=0}^{t-1}d_j\not\equiv0\pmod N
   \ (1\le t\le s)
  \right\}.
 \tag{7.3}
\]

Equivalently, the terminal integer equation can be

\[
 \sum_{j=0}^{s-1}d_j=\delta_s+aN
\]

with winding \(a\ge0\). Nothing here forces \(a=0\) in a Gaussian time
window.

The theorem-level alternatives are now:

1. prove that the long-cycle edge-disjoint packing generated by
   \(\bigcup_{0\le s\le H-1}\mathcal R_{r,s}\) is
   \(o_A(B_r/N)\), which proves \((\mathrm{RP}_A)\); or
2. prove a critical lower packing from actual solutions of (7.3), and
   only then construct a literal shared braid for their true endpoint
   states.

Terminality \(B_0=\varnothing\) alone can appear in neither conclusion.

## 8. Implication scope and documentary correction

The exact current logical boundary is:

* the one-step sector transport (1.4) is valid;
* the full-cycle shift and primitive converse in the named source are
  retracted;
* the lower half of
  `PBBS_HEIGHT_STRATIFIED_PACKING_MATCHING_OBSTRUCTION_20260725.md`
  reuses that converse and therefore does not establish
  \(\nu_H(P_r)=\Theta_A(B_r\sqrt r)\);
* the height invariance and height-stratified upper estimates do not by
  themselves disprove \((\mathrm{RP}_A)\); and
* Section 23 of `PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md` correctly
  records \((\mathrm{RP}_A)\) as neither proved nor disproved.

Thus the requested assertion “\((\mathrm{RP}_A)\) is false” is not a
frozen theorem compatible with the cited source. The rigorous advance in
this report is the exact protected-spine characterization, its negligible
mass, and the resulting literal no-port obstruction for an all-primitive
sector fusion.

## 9. Internal adversarial audit

1. **The report does not infer \((\mathrm{RP}_A)\).** It only retracts an
   invalid disproof and identifies the corrected sector subclass.

2. **The criterion is an iff for the advertised atlas, not for all actual
   returns.** Accidental solutions of (7.2) may exist outside
   \(\mathcal P_r\).

3. **The \(B_t\)-height bound is at the transported depth.** At time
   \(h\), \(B_t\) sits at depth \(h-1-t\); the strict pre-spine allowance
   is exactly \(t\), not \(h-t\).

4. **The entropy estimate does not assume independence.** It combines an
   exact height-confinement bound with the deterministic forced-prefix
   count and splits at \(r^{1/3}\). The exact product (4.1) is not needed
   for the upper bound.

5. **The cost implication is deliberately generous.** It permits
   \(O(H^2)\) cost for every one of the \(N|\mathcal P_r|\) physical
   occurrences; polynomial loss is swallowed by (4.2).

6. **Conjugation cannot repair the failed port.** A bijection of
   coordinates preserves distinctness. This does not rule out a bridge
   using additional Johnson/MTF owners; it proves that such a bridge is
   new work rather than the alleged zero-winding identification.

7. **No broad global-braid no-go is claimed.** Dynamic-spine,
   cross-orbit, cross-parity, or distant-port constructions remain open.
