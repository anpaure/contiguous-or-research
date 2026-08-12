# Audit: fixed-factor cap-two LP, switch energy, and occupied hexagons

**Date:** 2026-08-03  
**Audited theorem:**
MATH_THEOREM_FIXED_FACTOR_CAPTWO_LP_ENERGY_AND_C6_APPLICABILITY_20260803.md  
**Method:** independent symbolic replay of every count and implication. No
computation or finite search is used.

## 0. Verdict

**GO at the theorem's stated scopes.**

The uniform fractional point, two-stage rainbow equivalence, general
quadratic switch identity, consolidated Boolean-\(C_6\) descent formula,
directed-\(3\)-cycle applicability criterion, linear occupied-support
bound, and abstract \(C_8\) integrality obstruction are all correct.

The theorem proves neither a Boolean cap-two second matching nor a
counterexample to one. The local pointer and \(C_8\) obstructions are
explicitly scoped.

## 1. Fractional LP audit

The graph \(H=G-F_0\) is \((m-1)\)-regular at every tail and every head.
Every upper-colour class has \(m+1\) arcs. Therefore
\[
 x_e=\frac1{m-1}
\]
gives unit tail and head loads and colour load
\[
 \frac{m+1}{m-1}=1+\frac2{m-1}\in[1,2].
\]
The binomial ratio
\[
 \frac{|\mathcal M|}{|\mathcal U|}
 =\frac{m+1}{m-1}
\]
implies
\[
 |\mathcal M|-|\mathcal U|
 =\frac2{m-1}|\mathcal U|
 =\operatorname{Cat}_m.
\]
Thus all equalities in Theorem 1.1 are correct.

An integral nonnegative point satisfying unit tail equations has exactly
one selected arc at every tail; the head equations make those arcs a
perfect matching. The colour box is exactly the upper-surjective cap-two
condition. Hence the LP's integral interpretation is exact.

## 2. Rainbow decomposition audit

Given a cap-two perfect matching \(F\), choosing one selected arc from
every colour produces a matching \(Q\) of size \(|\mathcal U|\). The
remainder \(P=F-Q\) is vertex-disjoint from \(Q\), has size
\(|\mathcal M|-|\mathcal U|\), and is rainbow because a colour occurred at
most twice in \(F\).

Conversely, if \(Q\) uses every colour once, \(P\) is rainbow, and their
vertex-disjoint union is perfect, then every colour appears once or twice.
The colours of \(P\) are precisely the duplicated colours. This proves
both directions without assuming a prescribed duplicate design.

## 3. Alternating-cycle energy audit

For
\[
 f(z)=\frac{(z-1)(z-2)}2,
\]
direct expansion gives
\[
 f(\mu+\delta)-f(\mu)
 =\mu\delta+\frac{\delta^2-3\delta}{2}.
\]
An alternating cycle inserts and removes equally many edges, so
\(\sum_R\delta_R=0\). Summation cancels the \(-3\delta_R/2\) terms and
gives
\[
 \Delta(F')-\Delta(F)
 =\sum_R\mu_R\delta_R+\frac12\sum_R\delta_R^2.
\]
If the inserted and removed colour sets are disjoint, simple, and each has
size \(\ell\), there are \(2\ell\) nonzero signed entries of square one.
This gives formula (3.3).

The identity remains correct for coincident colours only after all signed
changes are consolidated, exactly as stated.

## 4. Boolean-hexagon overlap audit

Full support gives
\[
 x_a,x_b,x_c\notin\{a,b,c\}.
\]
Each old or new upper colour is therefore determined by its two-element
subset of \(\{a,b,c\}\) and one external pointer. Within either phase the
three two-element subsets differ, so all three colours are distinct.

An old-new equality can occur only when the two-element subset agrees.
The three possibilities are exactly
\[
 x_a=x_b,\qquad x_b=x_c,\qquad x_c=x_a
\]
in the positions listed in (4.2). Cancelling the common colours leaves
\(3-\kappa\) inserted and \(3-\kappa\) removed colours. Applying the
simple-support switch identity yields (4.3). Since all quantities are
integral, strict negativity is equivalent to (4.4). If inserted colours
are holes and removed colours have multiplicity at least two, the change
is at most \(-(3-\kappa)\).

## 5. Occupied-support audit

At a fixed core \(C\), the second matching chooses at lower vertex \(C+a\)
one owner \(C+a+g_C(a)\). Disjointness from \(F_0\) gives
\[
 g_C(a)\ne f_C(a).
\]

The phase
\[
 (C+a,C+ab),\ (C+b,C+bc),\ (C+c,C+ca)
\]
is selected precisely when
\[
 g_C(a)=b,\quad g_C(b)=c,\quad g_C(c)=a.
\]
The other phase is the reverse directed \(3\)-cycle. Thus an occupied
hexagon is exactly a directed \(3\)-cycle of the functional digraph
\(g_C\) whose complementary phase survives \(F_0\).

Directed cycles of a function are vertex-disjoint, so at most
\(\lfloor(m+1)/3\rfloor\) such triples exist at one core. The cyclic local
model
\[
 g_C(a)=a+1,\qquad f_C(a)=a+2
\]
on \(\mathbb Z/(m+1)\mathbb Z\) has disjoint selected/deleted pointers but
no directed \(3\)-cycle for \(m+1\ge4\). For \(m\ge7\), the separate
potential-support theorem still gives \(\Omega(m^3)\) full supports for
\(f_C\). The theorem correctly labels this only a local pointer model,
not a globally extendable Boolean factor pair.

## 6. Abstract \(C_8\) obstruction audit

The edges
\[
 e_i=L_iM_i,\qquad h_i=L_iM_{i+1}
\]
form one \(8\)-cycle, hence have exactly the two perfect matchings
\(E=\{e_i\}\) and \(J=\{h_i\}\).

With red edges \(e_0,e_1,e_2,h_3\) and blue edges
\(e_3,h_0,h_1,h_2\), every tail has one outgoing arc of each colour and
each colour has four arcs. The half-edge vector has unit tail/head loads
and colour load two.

Red has heads \(M_0,M_0,M_1,M_2\), while blue has
\(M_1,M_2,M_3,M_3\), so distinct head representatives exist; distinct tail
representatives are immediate. Yet \(E\) has colour counts \((3,1)\) and
\(J\) has \((1,3)\). Thus neither integral cycle cover is cap-two.

This validates the claimed abstract integrality gap. Its vertex counts are
not the Boolean \(m=3\) layer counts, so it is not a Boolean counterexample.

## 7. Sufficient-condition audit

The rainbow completion criterion is Theorem 2.1 in constructive form.
For the descent criterion, every full occupied \(C_6\) switch preserves
perfectness. Under (4.4) it strictly decreases the nonnegative integer
\(\Delta\). Repetition must terminate, and the zero set of
\(\Delta=\sum_R f(\mu_R)\) is exactly
\(\mu_R\in\{1,2\}\) for every colour.

The occupied-support theorem shows that cubic potential support does not
establish the premise. Longer alternating cycles, multi-core changes, or a
separate rainbow-completion argument remain necessary.

## 8. Proof-safe conclusion

The verified status is
\[
\boxed{
\begin{array}{c}
\text{canonical cap LP feasible}\\
\Downarrow\quad\text{integrality open}\\
\text{cap-two Boolean second factor}.
\end{array}}
\]

The exact local gradient and exact \(C_6\) applicability gate are now
known. No unconditional fixed-factor selector theorem is claimed.
