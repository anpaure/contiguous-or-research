# Independent audit of the isolated-reset ABKV ceiling

Date: 2026-07-24

## Verdict

The submitted implication is valid as a ceiling on the following specific
proof architecture:

1. use full, fixed-radius queue atoms;
2. emit every selected atom with its own canonical initialization/reset;
3. retain the original real band vertices through dummy completion and
   sparsification; and
4. apply the Alon--Bollobas--Kim--Vu theorem directly to the resulting
   unsplit uniform hypergraph.

Under those assumptions,

\[
 |A_m|=W+o(W)
 \quad\Longrightarrow\quad
 \frac hH\longrightarrow0,
 \qquad
 K=H(2h+1)\le \left(\frac12+o(1)\right)\log m,
\]

and consequently

\[
 \boxed{h^2=o(\log m).}
\]

This is an architecture ceiling, not a retraction of the economical-cover
theorem.  In particular, high-order clustering does not invalidate the ABKV
cover theorem: its stated hypotheses involve near-regular vertex degrees and
maximum **pair** codegree, not higher codegrees.

Throughout,

\[
 W=\binom{2m}{m}.
\]

## 1. Isolated-reset word accounting

A constant-radius-`h` queue atom with `H` starts has the canonical word

* one initial complement literal;
* `2h` singleton update literals; and
* `H` terminal minimum literals.

Thus its canonical literal length is exactly

\[
 H+2h+1.
\tag{1.1}
\]

Every atom exposes exactly `H` distinct middle masks.  If `p` selected atoms
cover the full middle row, then necessarily

\[
 pH\ge W.
\tag{1.2}
\]

In the isolated-reset architecture the atom words are concatenated without
sharing their initializations.  Therefore their contribution to the word
length is

\[
 p(H+2h+1)
 \ge W\left(1+\frac{2h+1}{H}\right).
\tag{1.3}
\]

Consequently, a total length `W+o(W)` forces

\[
 \frac hH=o(1).
\tag{1.4}
\]

There are two necessary scope qualifications.

* The general monotone-profile construction is sometimes recorded as having
  length *at most* `H+2h+1`.  An upper bound cannot prove the necessity
  (1.4).  Here (1.4) is justified by the exact canonical constant-radius word
  and the rule that each selected atom pays its own reset.
* For a matching that leaves `o(W)` middle masks for a separately charged
  repair, (1.2) becomes `pH=W-o(W)`, which gives the same conclusion.  An
  argument allowing an uncharged macroscopic middle remainder would not.

Shared resets, deletion or compression of canonical literals, and splicing
several nominal atoms into one longer path are outside the audited ceiling.

## 2. The nested-pair codegree lower bound

Let

\[
 \mathcal L=\{S\subseteq[2m]:|S|=m-1\},
 \qquad
 N_1=|\mathcal L|=\binom{2m}{m-1}=W\frac{m}{m+1}.
\]

There are exactly

\[
 N_1(m+1)=Wm
\tag{2.1}
\]

nested adjacent pairs `(S,T)` with `|S|=m-1`, `|T|=m`, and `S\subset T`.
Every occurrence of a real lower-row vertex `S` in a queue atom has its
same-start middle superset `T` in that atom.  Hence every lower-row
vertex-edge incidence supplies at least one incidence of an edge with one of
the pairs in (2.1).

Suppose the ABKV input has degree scale `D`, all but `o(W)` real lower-row
vertices have degree `(1-o(1))D`, and the exceptional incidences are
`o(WD)`.  Summing over all nested pairs gives

\[
 \sum_{S\subset T}d(S,T)
 \ge (1-o(1))N_1D.
\tag{2.2}
\]

Dividing by (2.1) shows that the maximum pair codegree `C` satisfies

\[
 C\ge(1-o(1))\frac{D}{m+1},
 \qquad
 \boxed{\frac CD\ge\frac{1-o(1)}m.}
\tag{2.3}
\]

This proof uses the degree lower bound, not a heuristic about a typical
pair.

### 2.1 Dummy completion

The submitted dummy completion only fills inactive signed-row slots.  It
does not replace, clone, or split a real lower or middle vertex, and it does
not remove the same-start pair from an atom.  Therefore it cannot dilute the
old--old incidence count (2.2).

There is also a fractional version of the argument.  If `x_e` is the
dummy-completed fractional perfect matching, every real lower vertex has
fractional degree one.  Choosing the canonical same-start pair for each
such incidence gives total witness mass exactly `N_1`.  The sum of all
nested pair-codegrees can only be larger, so

\[
 \sum_{S\subset T}\sum_{e\supset\{S,T\}}x_e\ge N_1,
\]

so some nested pair has weighted codegree at least

\[
 \frac{N_1}{Wm}=\frac1{m+1}.
\tag{2.4}
\]

### 2.2 Bernoulli support sparsification

In the simple-support version, each distinct support `e` is retained
independently with probability `Lambda x_e`, where `Lambda=m^8` for the
submitted parameters.  Apply (2.4) to a fixed pair attaining the fractional
maximum.  Its sampled codegree has mean at least

\[
 \frac{\Lambda}{m+1}=m^{7+o(1)}.
\]

A Chernoff lower-tail bound therefore gives codegree at least
`(1-o(1))Lambda/(m+1)` with overwhelmingly high probability.  At the same
time every vertex degree is `D=(1+o(1))Lambda`.  These events may be
intersected with the already used degree and upper-codegree concentration
events.  Hence (2.3) holds in the same deterministic realization to which
ABKV is applied.

Equivalently, once near-regularity of the real lower vertices is known, the
deterministic double count (2.2) proves the lower bound without singling out
a pair before sampling.

### 2.3 Label lift and cleaning

A one-vertex label lift adds a label to each occurrence but leaves every
old--old pair incidence unchanged.  The submitted collision cleaning deletes
only polynomially many lifted edges.  Each deleted edge destroys at most
`H` certified lower/middle pair incidences, whereas (2.2) has order `WD`.
Since `W` is exponential and the submitted `H,D` are subexponential,

\[
 \operatorname{poly}(m)H=o(WD).
\]

Re-averaging after cleaning therefore still gives (2.3).  It is not
necessary to assume that the particular pair selected before cleaning
survives.

The conclusion would need a new proof for a different regularization that
clones or splits real vertices, or for a cleaning that removes
`Theta(WD)` certified incidences.  Neither occurs in the submitted dummy,
Bernoulli, or label-lift constructions.

## 3. Exact ABKV hypothesis

The primary source is Alon--Bollobas--Kim--Vu,
[*Economical covers with geometric applications*](https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf).
Equation (8) assumes, for a `k`-uniform hypergraph of maximum pair codegree
`C`,

\[
 D-f(D)\le d(v)\le D,
 \qquad
 C=o\left(\frac{D}{e^{2k}\log D}\right),
 \tag{3.1}
\]

where

\[
 f(x)=20(x^2C\log x)^{1/3}.
\tag{3.2}
\]

Theorem 3.7 gives the economical cover conclusion when (3.1) holds outside
a set `B` of low-degree vertices, with an additive `|B|` term.  For `k>4`,
the formal codegree condition is exactly

\[
 \boxed{e^{2k}C\log D=o(D).}
\tag{3.3}
\]

Theorem 3.9 gives the corresponding matching conclusion.  The paper treats
nonconstant `k`; this is not a diagonal use of a theorem stated only for
fixed uniformity.  If a label vertex is appended, the theorem's uniformity
is `k=K+1`, not `K`; the extra constant factor `e^2` in (3.3) has no effect
on the asymptotic ceiling.

Merely checking an upper degree `D` is insufficient.  The near-regular lower
degree bound, the maximum pair-codegree bound, the small exceptional set,
and (3.3) all have to hold.  They are precisely the facts used in the
submitted Bernoulli realization.

## 4. The uniformity and radius ceilings

Insert (2.3) into (3.3), with `k=K` for the simple Bernoulli support route:

\[
 e^{2K}\frac{C}{D}\log D
 \ge(1-o(1))\frac{e^{2K}\log D}{m}
 \longrightarrow0.
\]

Taking logarithms gives the stronger relation

\[
 2K+\log\log D-\log m\longrightarrow-\infty.
\tag{4.1}
\]

In particular,

\[
 \boxed{K\le\left(\frac12+o(1)\right)\log m.}
\tag{4.2}
\]

For a full fixed-radius atom,

\[
 K=H(2h+1).
\tag{4.3}
\]

If `h>0`, (1.4) yields

\[
 \frac{K}{h^2}
 =\frac Hh\left(2+\frac1h\right)
 \longrightarrow\infty.
\tag{4.4}
\]

Combining (4.2) and (4.4) proves `h^2=o(log m)`.  If `h` is bounded (or
zero), that conclusion is immediate.

This is only the ceiling imposed by the formal direct-ABKV hypothesis.  To
obtain a quantitatively negligible residual from the matching conclusion,
one must also make the displayed Theorem 3.9 error tend to zero; that can
impose a stronger restriction.  Conversely, Corollary 3.8's edge-splitting
cover argument is a different architecture and does not preserve, without
additional work, the interpretation of one selected edge as one isolated
queue atom.

## 5. High-order clustering does not retract the cover theorem

The suggested retraction does not follow.

High-order rectangle clustering is a real obstruction to black boxes whose
hypotheses control all `j`-codegrees or a full-codegree parameter, and it can
make a complete-atom matching nibble ineffective.  ABKV Theorem 3.7 has no
such hypothesis.  Its equation (8) asks for the vertex-degree window and
maximum pair codegree in (3.1).  Once those conditions hold, higher-order
clusters are permitted by the theorem.

Nor does clustering expose a failure in the submitted simple Bernoulli
regularization:

* distinct augmented supports are sampled as distinct edges;
* the support bound ensures `Lambda x_e=o(1)` in the submitted growing
  parameter regime, so these are valid Bernoulli probabilities;
* every augmented vertex has expected degree `Lambda`, and simultaneous
  concentration supplies the required near-regular degree window;
* the weighted pair-codegree upper bound supplies the required `C`; and
* Section 2 proves that the unavoidable lower scale of that same `C` is
  `D/m`, which creates the ceiling but not a contradiction.

Thus the high-order observation distinguishes ABKV covers from stronger
matching/full-codegree rounding routes; it does not invalidate the audited
economical cover.  A retraction would require an actual failure of
uniformity, simplicity, degree regularity, pair-codegree control, the ABKV
asymptotic condition, or the literal strip/queue realization.  High-order
clustering alone is none of these.

## Final conclusion

The valid statement is:

> Any direct, unsplit ABKV certificate made from independently reset,
> full fixed-radius queue atoms and having total word length `W+o(W)` must
> satisfy `h^2=o(log m)`.

The invalid add-on is:

> High-order clustering retracts the economical-cover theorem.

It does not.  The ceiling identifies the limit of this isolated-reset queue
architecture while leaving the already verified ABKV economical-cover
construction intact.
