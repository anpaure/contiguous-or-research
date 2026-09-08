# Audit and exact joint state for odd-diamond occurrence coherence

Date: 2026-07-31  
Status: independent mathematical audit and exact recursive-state refinement;
no new `K17` carrier or word is claimed

## 0. Verdict

The occurrence ledger in
`MATH_THEOREM_ODD_DIAMOND_OCCURRENCE_COHERENCE_20260731.md` is correct.
Its central consequence is stronger than two marginal lower bounds:
residence clauses, upper-provider rewards and the future macro-port demand
are functions of the **same** one-occurrence-per-depth-two-colour choice.
They must be selected jointly before the residual `b`-flow is formed.

For the authenticated first parent the exact marginal pair is

\[
          (D_{\rm up}^{\min},D_{\rm res}^{\min})=(505,180),
                                                               \tag{0.1}
\]

whereas for the separate octahedral `r2` parent it is

\[
                         (405,150).                   \tag{0.2}
\]

Thus `150` does not revise the certified `180` optimum: it belongs to a
different parent chronology.  Neither pair asserts that its two marginal
minima are attained by one common transversal.

## 1. Exact occurrence variables

Let (E) be the physical trace-edge occurrences and, for every required
rank-((r-2)) depth-two colour (Z), let

\[
                         F_Z=\{e\in E:Z_e=Z\}.       \tag{1.1}
\]

The occurrence transversal is a zero-one vector (x\in\{0,1\}^E) with

\[
                         \sum_{e\in F_Z}x_e=1
                         \qquad\text{for every }Z.   \tag{1.2}
\]

Let (A\subseteq E) be the physical edges whose parent upper union occurs
nowhere else.  The number of destroyed unique internal upper witnesses is

\[
                         D_{\rm up}(x)
                 =\sum_{e\in A}(1-x_e).             \tag{1.3}
\]

For a minimum parent run (R\), let (S_R\subseteq E) be its physical
trace-edge collar.  Its short `A`-shore child run remains wholly internal
exactly when every collar edge is retained.  Hence

\[
                         D_{\rm res}(x)
                 =\sum_R\prod_{e\in S_R}x_e,        \tag{1.4}
\]

and flat residence is exactly the hyperclause system

\[
                         \sum_{e\in S_R}(1-x_e)\ge1
                         \qquad\text{for every }R.   \tag{1.5}
\]

Equations (1.2), (1.3) and (1.5) are the exact joint occurrence problem.
They are not three successive construction stages.

## 2. Exact marginal upper debt

For one fibre define (u_Z=|A\cap F_Z|).  Since (1.2) retains at most one
of those (u_Z) edges,

\[
                         D_{\rm up}(x)
                  \ge\sum_Z(u_Z-1)^+.               \tag{2.1}
\]

Equality is attained fibre by fibre: retain an edge in (A\cap F_Z) when
that set is nonempty, and otherwise retain any member of (F_Z).  Therefore

\[
                 \boxed{\min_xD_{\rm up}(x)=
                        \sum_Z(u_Z-1)^+.}            \tag{2.2}
\]

This is an exact count of destroyed **internal unique witnesses**, not an
upper-hole lower bound.  A later macro port may recreate the same upper
target.

For the first parent,

\[
 u_Z:0^{1835}1^{2685}2^{465}3^{20},
 \qquad D_{\rm up}^{\min}=465+2\cdot20=505.          \tag{2.3}
\]

For the octahedral `r2` parent,

\[
 u_Z:0^{1735}1^{2865}2^{405},
 \qquad D_{\rm up}^{\min}=405.                      \tag{2.4}
\]

Both profiles sum to `5005` fibres, as required.

## 3. Why marginal optimization does not compose

The failure already occurs with two fibres.  Take

\[
 F_1=\{a,a'\},\qquad F_2=\{b,b'\},\qquad A=\{a,b\}, \tag{3.1}
\]

and one residence packet (S_R=\{a,b\}).  The upper marginal optimum is
zero, attained only by selecting (a,b).  Residence marginal optimum zero
is also attainable, for example by selecting (a',b').  But no transversal
attains both: preserving both unique providers selects the whole forbidden
packet.

This is the smallest possible nonseparability witness: one fibre alone has
no cross-fibre residence hyperedge.  It remains an obstruction even if the
future macro-port signature is declared constant.  Consequently no theorem
which combines only the two marginal optimum values can prove a recursive
child.

## 4. The exact exported state

For a transversal (x), let

* ({\cal R}(x)=\{R:S_R\subseteq\operatorname{supp}(x)\}) be its surviving
  minimum-run debt;
* ({\cal A}(x)=A\cap\operatorname{supp}(x)) be its retained unique-provider
  occurrence set; and
* (sigma(x)) be the occurrence-labelled residual macro state: path
  interiors, endpoint colours and the induced port degree demand.

Define the exact coherence frontier

\[
 \Phi_T(r,\sigma)=
   \min\{D_{\rm up}(x):x\text{ satisfies (1.2)},
          |{\cal R}(x)|\le r,
          \sigma(x)=\sigma\}.                       \tag{4.1}
\]

An empty feasible set has value (+\infty).  The collection of finite
triples

\[
                 (|{\cal R}(x)|,D_{\rm up}(x),\sigma(x))            \tag{4.2}
\]

is the exact scalar Pareto projection.  The weakest literal lossless state
is instead

\[
                    ({\cal R}(x),{\cal A}(x),\sigma(x)),             \tag{4.3}
\]

because downstream port service is target-specific.  Replacing either set
in (4.3) by its cardinality is safe only under an additional target-symmetry
hypothesis.  No such symmetry is available in the literal compiler.

### Theorem 4.1 (correct construction order)

Within the parent-induced odd-diamond template, a child package exists if
and only if there is one transversal (x) satisfying (1.2) for which:

1. every member of ({\cal R}(x)) is accepted by the declared nonflat or
   cut/facet compensation mechanism;
2. every destroyed upper occurrence required by the child is re-provided
   internally or at a literal port; and
3. the residual macro state (sigma(x)) admits the prescribed-degree
   integral `U`-port flow, its one-cycle closure, and the downstream shadow
   and compiler rows.

In particular, the residual `b`-flow is chosen **after** (x).  A flow for
one occurrence transversal cannot in general be transplanted to another.

#### Proof

Necessity follows because (1.2) determines the retained trace edges, hence
all three data in (4.3), before a port edge exists.  For sufficiency, build
the residual macros from (x), apply the declared compensation to
({\cal R}(x)), then install the certified flow and the literal upper and
compiler witnesses.  These operations are precisely the parent-induced
construction, in dependency order. \(\square\)

Theorem 4.1 is an interface theorem, not an existence proof for a finite
point of (Phi_T) satisfying all downstream rows.

## 5. Authenticated calibration and remaining boundary

For the first parent, the solver-free forced-packet floor is `165`, while
the exact coupled residence optimum is `180=12\cdot15`.  Its upper marginal
debt is `505`.  For the octahedral `r2` parent, the corresponding exact
reported figures are residence `150` and upper marginal debt `405`; its
factor artifact has SHA-256

```text
13c5ecaddc94bd4a240c9b2ce348f5db4508cb340658b2b0f4797b8c80472dfb
```

The simultaneous coherence frontiers (Phi_T) of the two parents have not
been computed.  Therefore it is proved that the octahedral parent improves
both marginal optima, but it is not proved here that one common octahedral
transversal simultaneously attains `(405,150)`, admits a connected port
flow, preserves deeper shadows, or compiles.

The reusable conclusion is exact: an odd regenerative state must export an
occurrence-labelled transversal together with residence compensation,
surviving upper providers and macro-port demand.  Exporting only the parent
factor or only the scalar pair of debts loses essential correlation.
