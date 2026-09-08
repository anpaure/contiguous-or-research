# Independent audit of the fixed-core orbit/reset-socket interface

**Date:** 2026-08-02  
**Status:** PASS for the stated reduction and counterexamples.  The rooted
socket-bank existence lemma remains open.

## 1. Items checked independently

The audit re-derived the following without using aggregate matrix zeros as a
proof.

1. Substitution in the four literal long-row normal forms makes every
   decreasing flag transition repeat either the lower target \(L\) or the
   second target \(M\).  Exact target ownership and the strict owner increment
   exclude distinct-row and self transitions.  Hence
   \(\alpha\leq\beta\) pointwise.

2. The anonymous interval reset minimum is

   \[
   \rho(D)=D_0+(D_1-D_0)_+ +(D_2-D_1)_+
          =\max\{D_0,D_1,D_2,D_0+D_2-D_1\}.
   \]

3. For a prescribed partial matching \(P\), completion is exactly Hall in
   the graph obtained by deleting the used left and right vertices.  A
   residual type flow is equivalent only when every residual type-pair graph
   is still biregular.

4. If type neighborhoods do not change, the residual type cut is exactly

   \[
   q(N(X))-p(X)\leq\sigma_\tau(X).
   \]

5. The \(C_8\) example in the theorem is a literal counterexample to
   count-only type subtraction.  After protecting \(l_1r_1,l_4r_3\), the
   two remaining left vertices \(l_2,l_3\) both have sole residual neighbor
   \(r_2\).

## 2. K19/K21 arithmetic

For K19,

\[
3{19\choose9}-(2^{18}-1)=14\,991.
\]

The fixed blocks miss \(15\) and \(14\,976\) of the \(W\) chains.  Their
missing-chain sets have intersection \(x\in[0,15]\), so their union, the
short-chain set, has size \(14\,991-x\).  Therefore

\[
14\,976\leq S\leq14\,991.
\]

For K21,

\[
3{21\choose10}-(2^{20}-1)=9\,573.
\]

The first two blocks miss \(837\) and \(8\,736\) chains.  With overlap
\(x\in[0,837]\),

\[
S=9\,573-x,\qquad 8\,736\leq S\leq9\,573.
\]

These counts are potential short roles.  They do not assert distinct socket
ports or address-compatible states.

## 3. Deterministic chronology counterexample

The H100 diagnostic at

    /home/amodo/or15/work/root_allk_fixed_core_nextfit_flow_20260802

constructs the logarithmic fixed core, sorts orbit types by
rank/fixed-mask/outside-rank, packs them next-fit into \(W\)-capacity blocks,
and runs the exact product-order type max-flow.

The frozen summary reports:

| \(k\) | supply | matched | deficiency | Hall shore |
|---:|---:|---:|---:|---:|
| 17 | 65,535 | 65,249 | 286 | 37,323 versus 37,037 |
| 19 | 262,143 | 262,143 | 0 | — |
| 21 | 1,048,575 | 1,039,071 | 9,504 | 493,000 versus 483,496 |

Thus the failure is scoped to that deterministic chronology.  It is not a
K17 or K21 static no-go, and it does not contradict the custom K19/K21
splits.  It proves that the within-rank orbit order is a joint construction
variable, not harmless preprocessing.

Frozen diagnostic hashes:

    summary 65fb165a51553f912c56642754e49f5d529bc5675b2f19b7ca93ae5db87e56a8
    cuts    09a9a2a1a5e0e22da2300df8174b695c1009bae71244f2033ff356723464d3fc
    source  123247ec0eb0936d435b976559bf1b2f8e70ba26f111dd850639d7dc54c5a56d

The local source currently bearing the same filename is a later version and
does not have the frozen remote source hash.  The verdict above is bound to
the remote manifest and output, not inferred from the local filename.

## 4. Scope verdict

The correct prospective quantifier order is

\[
\exists\,(\tau,\text{chain factor},\text{literal states},P)
\]

subject jointly to product-order flow, exact target/owner ownership, flag
reset equations, and residual Hall.  Neither

\[
\forall\tau\ \exists P
\qquad\text{nor}\qquad
\exists\tau\ \forall P
\]

is proved.

The K19/K21 orbit theorem closes only the unprotected static factor for its
custom chronology.  The exact next row is the cut-safe, address-compatible
rooted orbit-reset bank.  Residence, all upper decks, topology/opening,
common-cap, and compiler closure remain separate.

