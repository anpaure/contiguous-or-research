# Audit of linked-band transfer and meet-core pinning

## Verdict

**PASS WITH ONE MATERIAL QUANTIFIER REPAIR.**

The linked-union formula, upper-OR transfer, common-core formula, maximal
legal-set construction, simultaneous central/lower pin theorem, and zero-free
criterion are exact.  They reproduce the already audited results in
`VARIABLE_BAND_FOUR_BOX_FACTOR.md`, `GLOBAL_PINNING.md`, and
`PINNING_THEOREM.md`.

The necessary repair is this: the condition

\[
  J_{p,q}\cap Z_b\ne\varnothing\qquad
  \bigl(b\in\bigcap_{i=p}^qT_i\bigr)
\]

forces the core OR to equal the meet for the **maximal factor**

\[
  A_j^{\max}=\{b:j\in Z_b\},
\]

and proves that a suitable factor exists.  It does not force that equality
for every arbitrary factor already realizing the central row.  For a factor
defined by chosen pin sets `H_b subseteq Z_b`, the exact condition is

\[
  J_{p,q}\cap H_b\ne\varnothing
  \qquad\bigl(b\in\bigcap_{i=p}^qT_i\bigr).
\]

## 1. Linked interval geometry

Write

\[
 I_i=[\ell_i,r_i]=[i+\alpha_i,i+\beta_i],
\]

where both offset sequences are nondecreasing and `alpha_i<=beta_i`.
Implicitly the displayed intervals must lie in `[n]`.  Then `ell_i` and
`r_i` are strictly increasing.  The link condition

\[
 \alpha_{i+1}\le\beta_i
 \iff \ell_{i+1}\le r_i+1
\]

says exactly that consecutive intervals overlap or abut.  Therefore, for
every `p<=q`,

\[
 \bigcup_{i=p}^q I_i=[\ell_p,r_q]
 =[p+\alpha_p,q+\beta_q].
\]

If one array realizes `OR(I_i)=T_i`, finite-union associativity gives

\[
 \operatorname{OR}([\ell_p,r_q])
 =\bigvee_{i=p}^qT_i.
\]

Thus the upper-join transfer is unconditional once the central equations and
linkedness hold.

The common core is likewise exactly

\[
 J_{p,q}=\bigcap_{i=p}^qI_i
 =[\ell_q,r_p]=[q+\alpha_q,p+\beta_p],
\]

with the convention that it is empty when `ell_q>r_p`.

## 2. Exact central pin theorem

For each coordinate `b`, define

\[
 Z_b=[n]\setminus\bigcup_{i:b\notin T_i}I_i.
\]

The central equations have a realization if and only if

\[
 I_i\cap Z_b\ne\varnothing\qquad(b\in T_i).
\]

Indeed, every occurrence of `b` must lie in `Z_b`, while a positive interval
must contain at least one such occurrence.  When these conditions hold,
putting `b` at every point of `Z_b` gives the maximal factor.  More generally,
one may choose `H_b subseteq Z_b` hitting every positive central interval.

## 3. The required meet-core repair

If `b` is absent from `intersection_(i=p)^q T_i`, one of the central intervals
`I_i` excludes `b`, and the core is contained in that interval.  Hence `b` is
automatically absent from every realization on the whole core.  For a common
coordinate, however, membership of a point in `Z_b` means only that `b` is
*allowed* there, not that an arbitrary factor places `b` there.

A zero-free counterexample uses

\[
 I_1=[1,2],\quad I_2=[2,3],
\]

\[
 T_1=\{b,c,e\},\qquad T_2=\{b,d,e\},
\]

and

\[
 A_1=\{b,c\},\qquad A_2=\{e\},\qquad A_3=\{b,d\}.
\]

Both central equations hold.  There is no negative central interval for
`b`, so `Z_b=[3]`, and the core `J_(1,2)={2}` meets `Z_b`.  Nevertheless the
core OR is `{e}`, not

\[
 T_1\cap T_2=\{b,e\}.
\]

Thus the correct theorem is:

* for the maximal factor, `J_(p,q) cap Z_b != empty` for every common `b` is
  necessary and sufficient;
* for a chosen factor, replace `Z_b` by its actual pin set `H_b`;
* the `Z_b` condition nevertheless proves existence, since the maximal
  factor may always be selected.

## 4. Additional lower assignments and zero-free entries

After assigning lower targets `S` to intervals `K_S`, the exact legal set is

\[
 Z_b^*=[n]\setminus\left(
   \bigcup_{i:b\notin T_i}I_i
   \cup
   \bigcup_{S:b\notin S}K_S
 \right).
\]

One word realizes all central and lower equations if and only if every
positive assigned interval meets `Z_b^*` for each required coordinate.  The
maximal assignment `A_j={b:j in Z_b^*}` proves sufficiency.  This criterion
correctly accounts for the fact that a non-core lower interval can destroy
pins in other equations.

Finally, under these positive hitting conditions, a zero-free realization
exists exactly when

\[
 \bigcup_b Z_b^*=[n].
\]

Necessity follows because every coordinate at position `j` must be legal
there.  Sufficiency follows by using the maximal factor.  For sparse chosen
pin sets, the corresponding condition is `union_b H_b=[n]`.

## 5. Scope

These statements give an exact interface from an abstract middle-row braid to
an OR factor.  They do not establish the existence of a monotone linked band,
nonempty cores for all desired lower targets, or the required pin inequalities.
Those remain construction obligations.
