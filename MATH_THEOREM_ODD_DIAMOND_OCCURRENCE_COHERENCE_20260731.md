# The odd-diamond occurrence transversal couples residence and upper service

Date: 2026-07-31  
Status: exact dimension-uniform ledger and authenticated `K15` censuses;
no all-(k) construction is claimed

## 1. Setup

Let \(T\) be a lower-rainbow Johnson 2-factor. On each oriented component
put

\[
 C_i=T_i\cap T_{i+1},\qquad
 Z_i=C_i\cap C_{i+1},\qquad
 U_i=T_i\cup T_{i+1}.                              \tag{1.1}
\]

The parent-induced odd-diamond construction groups physical trace edges by
their lower depth-two colour \(Z_i\), and retains exactly one occurrence of
every required \(Z\). This occurrence transversal has two simultaneous
effects.

1. Its deleted edges cut the residual macros and decide which minimum
   coordinate runs remain internal.
2. Its retained edges decide which parent upper colours \(U_i\) remain
   available as internal one-tag child witnesses.

These are not independent choices.

## 2. Exact unique-provider loss

Call a physical edge \(i\) an **upper-unique provider** when its colour
\(U_i\) occurs on no other parent edge. For each depth-two colour \(Z\), let

\[
 u_Z=\#\{i:Z_i=Z\text{ and }U_i\text{ is upper-unique}\}. \tag{2.1}
\]

> **Lemma 2.1.** Among all one-occurrence-per-\(Z\) transversals, the
> minimum number of deleted upper-unique provider edges is exactly
> \[
>                         \sum_Z (u_Z-1)^+.          \tag{2.2}
> \]

### Proof

Within one \(Z\)-fibre at most one physical edge can be retained. Hence at
least \((u_Z-1)^+\) of its upper-unique edges are deleted. Conversely, if
\(u_Z>0\), retain any one upper-unique edge in that fibre; if \(u_Z=0\),
retain any occurrence. The fibres are disjoint, so these choices attain
the sum independently. \(\square\)

Equation (2.2) measures destroyed *internal* witnesses. Some colours may be
recreated later at macro ports, so it is not by itself a child upper-hole
lower bound. It is the exact debt presented to the port-turn problem.

## 3. Joint occurrence hypergraph

Residence gives a second family of constraints on the same variables. A
minimum parent run produces a trace pattern \(0,1^d,0\); its short child
image is avoided iff at least one of its \(d+1\) physical trace edges is
not selected. Thus the occurrence problem consists of

* one partition constraint selecting one edge in every \(Z\)-fibre;
* negative hyperedges for minimum-run packets; and
* rewards for selecting upper-unique providers.

This is the first genuine integral-correlation gate in the odd recurrence.
Solving lower depth two, residence, and upper preservation one after
another can be strictly suboptimal even though every marginal problem is
easy.

## 4. Authenticated `K15` values

For the `6390+45` parent used by the first parent-induced `K17` carrier,
the parent upper multiplicities are

\[
                         1^{3675}2^{1230}3^{100}.
\]

Among the `5005` depth-two fibres, the upper-unique counts have profile

\[
 u_Z:\qquad 0^{1835}1^{2685}2^{465}3^{20}.
\]

Therefore (2.2) is

\[
                             465+2\cdot20=505.       \tag{4.1}
\]

The better saved octahedral parent

```text
scratch/k15_octahedral_translation_descent_r2.factor.json
```

has the same complete depth-two and upper palettes but profile

\[
 u_Z:\qquad0^{1735}1^{2865}2^{405},
\]

and hence exact unique-provider debt

\[
                                  405.               \tag{4.2}
\]

The latter parent also lowers the exact occurrence-transversal internal
residence debt from `180` to `150`. The two improvements point in the same
direction, but neither closes the child: a port completion, deeper service,
and the compiler remain.

## 5. Recursive consequence

An odd-diamond regenerative state must carry the occurrence transversal
jointly with

\[
  (\text{minimum-run compensation},\quad
   \text{upper-unique preservation},\quad
   \text{macro endpoint/port demands}).             \tag{5.1}
\]

The central owner/lower-`q1` flow theorem begins only after this state is
chosen. A construction that selects an arbitrary lower depth-two
transversal and plans to repair residence and upper service independently
has discarded exactly the correlation measured by (2.1)--(2.2).
