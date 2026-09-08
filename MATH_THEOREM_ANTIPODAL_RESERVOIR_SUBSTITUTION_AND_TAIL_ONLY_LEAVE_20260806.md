# Antipodal dwell substitution leaves only a subexponential protected trace bank

**Date:** 2026-08-06  
**Method:** literal target accounting and monotonicity of protected-factor
extension; no computation or search  
**Status:** unconditional consequence of the protected antipodal-ear theorem.
The central dwell bank replaces the old common-core witness path for every
central external trace.  After retaining the hinge occurrences needed by
the rethread, the only separate common-core witness paths which remain are
the two binomial tails.  This does not join those tail paths or control the
unprotected components of a spanning factor completion.

## 1. Setting

Use

\[
 K\mathbin{\dot\cup}E=[2m-1],\qquad |K|=m-1,\quad |E|=m,
\tag{1.1}
\]

and let `d=O(sqrt(m))`.  Put

\[
 \mathcal B=\{T\subseteq E:2d+1\le |T|\le m-2d-1\}
\tag{1.2}
\]

and

\[
 \mathcal T=2^E\setminus\mathcal B.
\tag{1.3}
\]

The two forbidden traces `emptyset,E` may be omitted when target paths are
indexed; retaining them in the upper bound below is harmless.  The elementary
binomial estimate gives

\[
 |\mathcal T|
 \le2\sum_{j=0}^{2d}\binom mj
 \le2(2d+1)\left({em\over2d}\right)^{2d}
 =2^{o(m)}.
\tag{1.4}
\]

Let `R` be the protected common-core upper-damage reservoir.  Its targets
have the form

\[
                         Z_T=K\cup T,
\tag{1.5}
\]

where `T` is a nonempty proper subset of `E` containing one of the selected
hinge pairs.  Let `A` be the protected central antipodal dwell-and-ear bank
of Theorem 14.3 in
`MATH_THEOREM_ANTIPODAL_EAR_RESERVED_HALOS_AND_PORT_QUANTIFIER_GATE_20260806.md`.

For every `T in mathcal B`, the bank `A` contains an intact opened dwell

\[
                 \mathcal V_T=(T\cup W_0,\ldots,T\cup W_{m-2}),
\tag{1.6}
\]

where the cyclic windows `W_j` cover `K`.

## 2. Literal substitution

### Theorem 2.1 (central reservoir substitution)

For every `T in mathcal B`, the contiguous owner interval `mathcal V_T`
has union

\[
                         \bigcup\mathcal V_T=K\cup T.
\tag{2.1}
\]

Consequently every old common-core damage target whose external trace is
central remains witnessed after deleting its separate path from `R`.

#### Proof

The external trace of every owner in (1.6) is exactly `T`.  The cyclic
window family covers every coordinate of `K`, so

\[
 \bigcup_j(T\cup W_j)=T\cup\bigcup_jW_j=T\cup K.
\]

The ear attached at either port lies outside the displayed internal dwell
interval and therefore does not alter this occurrence.  This is exactly
(2.1).  Every target of `R` is indexed by its unique external trace, so the
last assertion follows. \(\square\)

Let `H` denote the `O(m)` distinguished hinge incidences (or, if desired,
their `O(m^2)` complete top paths) required by the common-history cyclic
rethread.  Define

\[
 R_{\rm tail}
 =H\cup\{Q_T\in R:T\in\mathcal T\}.
\tag{2.2}
\]

### Corollary 2.2 (tail-only protected upper bank)

The bank

\[
                         P'=A\cup J\cup R_{\rm tail}
\tag{2.3}
\]

still contains a literal owner-union witness for every target in the full
common-core hinge-damage family.  Here `J` is the complete low rolling-collar
cycle.  Moreover

\[
 |E(R_{\rm tail})|=2^{o(m)}.
\tag{2.4}
\]

#### Proof

For a central trace use Theorem 2.1.  For a tail trace retain its old path
`Q_T`.  The hinge incidences in `H` remain literal, so the rethread has not
lost its selected switch occurrences.

Every path in `R` has `O(m)` incidences.  Equations (1.4) and (2.2) therefore
give

\[
 |E(R_{\rm tail})|\le O(m)|\mathcal T|+O(m^2)=2^{o(m)}.
\]

The cycle `J` concerns the separate strict-lower source tickets and is
unchanged. \(\square\)

## 3. Exact factor consequence

### Theorem 3.1 (the reduced bank still has an exact `q1` completion)

The protected bank `P'` extends to a spanning two-factor of the
middle-levels incidence graph.  It retains:

1. every central dwell and ordinary antipodal ear;
2. all central residence halos and both immediate palettes;
3. every low rolling-collar source ticket;
4. every common-core damage witness; and
5. every distinguished common-history hinge occurrence.

#### Proof

Theorem 14.3 supplies a spanning two-factor containing

\[
                         A\cup J\cup R.
\]

The reduced bank (2.3) is a literal subgraph of that protected bank.  The
same spanning two-factor therefore contains `P'`.  The five listed families
are precisely the retained subobjects identified in Theorem 2.1 and
Corollary 2.2. \(\square\)

No new Ore calculation is needed: extendability is monotone under deleting
protected requirements, even though arbitrary completion properties are not.

## 4. Protected component count

Delete the tail traces from the cyclic antipodal trace word.  Every
remaining maximal interval is joined internally by the ordinary central
ears.  Hence the number of central protected path components is at most

\[
                         |\mathcal T|.
\tag{4.1}
\]

The cycle `J` contributes one component.  Every retained tail witness path
contributes at most one, and the optional complete hinge paths contribute
only `O(m)`.  Therefore

\[
 \boxed{\#\operatorname{Comp}(P')=2^{o(m)}.}
\tag{4.2}
\]

This is only the component count of the **protected** subgraph.  The
unprotected edges supplied by an arbitrary spanning two-factor completion
can create exponentially many additional components.  Thus (4.2) must not
be cited as a bounded-component completion theorem.

## 5. Remaining gate

The exponential collection of separate common-core witness paths is no
longer part of the topology problem.  The protected chronological leave is
now exactly:

\[
 \boxed{\text{at most }2^{o(m)}\text{ tail paths and splice ports, plus one
 low-source cycle and the fixed hinge bank}.}
\]

What remains is to attach those tail paths to the central chronology with
resident, halo-private splices, and then to choose the **residual** factor
completion so that the PBBS all-width section, global residence, bounded
topology, and terminal compiler interface coexist.  None of those residual
properties follows from Theorem 3.1 alone.

