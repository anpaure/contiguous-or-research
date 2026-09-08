# Period \(2q+1\) is a biresident pure rail, and central wreaths factor its full shell

**Date:** 2026-08-13  
**Status:** unconditional correction and exact owner-factor consequence.
The period lower bound \(N\ge2q+2\) used in later absorber catalogues is
stronger than the physical residence requirement. A central period
\(2q+1\) rail is positive- and zero-resident at depth \(q=d+1\).

## 1. Literal construction

Let (q=d+1\ge2), and let

\[
 |C|=c,\qquad
 T=\{x_0,\ldots,x_{2q}\},
\]

with \(C\cap T=\varnothing\). Use the cyclic singleton-toggle source

\[
 A_i=C\cup\{x_i\},\qquad i\in\mathbb Z_{2q+1}.
\tag{1.1}
\]

Its rank-\((c+q)\) owner row is

\[
 O_i=C\cup\{x_i,x_{i+1},\ldots,x_{i+q-1}\}.
\tag{1.2}
\]

### Theorem 1.1 (central rail legality)

The source (1.1) has:

1. \(2q+1\) distinct rank-\((c+q)\) owners forming a simple Johnson
   cycle;
2. simple immediate lower and upper rows
   \[
   C\cup I_i^{q-1},\qquad C\cup I_i^{q+1};
   \]
3. a simple proper interval deck \(C\cup I_i^j\) for every
   \(1\le j<2q+1\);
4. for every toggle coordinate, one owner one-run of length \(q\) and
   one zero-run of length \(q+1\); and
5. exact cyclic regeneration and zero whole-component trace boundary.

Hence it satisfies strict positive and dual residence at deadline
\(d\), whose run threshold is \(D=d+1=q\).

#### Proof

A proper cyclic interval of a cyclic order of distinct labels determines
its start and length. This proves owner and proper-deck simplicity.
Shifting (1.2) deletes \(x_i\) and inserts \(x_{i+q}\), which are
distinct, so the owner row is a Johnson cycle. Intersections and unions
of consecutive owners give the displayed \(q-1\) and \(q+1\) rows.

The unique source occurrence of \(x_i\) belongs to exactly the \(q\)
owner windows whose source intervals contain it. Thus its cyclic trace is
a shift of

\[
 1^q0^{q+1}.
\]

Both runs have length at least \(q\). Core coordinates have the constant
one trace and unused coordinates the constant zero trace, each on a
physical cycle of length \(2q+1\ge q\). The source is cyclic, proving
regeneration and zero boundary. \(\square\)

## 2. What the older \(2q+2\) hypothesis actually bought

The unified queue proof assumed

\[
 N\ge2(d+2)=2q+2
\]

and then recorded the stronger gap \(N-q\ge q+2\). Strict dual residence
only needs \(N-q\ge q\), equivalently \(N\ge2q\). In fact, for
\(q\ge2\), the same bare cyclic-window argument also makes period
\(N=2q\) a simple biresident unprotected rail. This note singles out
period \(2q+1\) because that is the central shell on which the
M\"utze--Standke--Wiechert factor applies.

Some later local gadgets genuinely use two exterior toggle labels. For
example, the adjacent-transposition port which places two disjoint
\(q\)-rays in one order assumes \(N\ge2q+2\). That is a port-supply
condition, not a residence axiom. No reviewed physical compiler theorem
requires the extra two zero positions for an unmodified closed central
rail.

## 3. Exact central-shell factor

The Mütze--Standke--Wiechert theorem factors the odd graph

\[
 KG(2q+1,q)
\]

into \(C_{2q+1}\)'s. Every minimum odd cycle is the family of all cyclic
\(q\)-windows of one order on its \(2q+1\) points. Therefore:

### Corollary 3.1 (integral shell factor)

For every fixed disjoint pair

\[
 |C|=c,\qquad |T|=2q+1,
\]

the complete shell

\[
 \{C\cup Q:Q\in\tbinom Tq\}
\]

has an exact partition into legal period-\((2q+1)\) biresident pure
rails. The number of rails is

\[
 \frac1{2q+1}\binom{2q+1}{q}
 =\operatorname{Cat}_q.
\]

Each rail also has both simple immediate palettes and a simple proper
interval deck.

This is a genuine positive owner factor, not a signed or fractional
statement.

## 4. Exact scope

Corollary 3.1 factors one \((2q+1)\)-point shell. It does not decompose
the full fixed-core fibre on a toggle ground of size \(M>2q+1\). Such a
decomposition would first need a partition of
\(\binom{[M]}q\) into central shells (or a more general overlapping-shell
allocation). Moreover, every rail in the fixed-core fibre gives each
toggle point degree divisible by \(q\), so the necessary condition

\[
 q\mid\binom{M-1}{q-1}
\]

persists even after period \(2q+1\) is admitted.

Thus the correction supplies an exact positive factor at the central
shell scale and makes MSW wreaths admissible resident rail columns. It
does not remove the global need for overlapping cores when fixed-core
divisibility fails, nor does it supply compulsory lower flags, global
fusion, or the common-cap router.
