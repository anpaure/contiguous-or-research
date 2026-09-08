# Active-bundle protected conveyors: the safe-root/common-key dichotomy

Date: 2026-07-31  
Lane: A, pure mathematics  
Status: unconditional exact theorem for one-cut full PBBS fragments.  It
does not prove that the required colour-back cycle exists in every
dimension.

## 1. Setup

Let \(F=C_1\sqcup\cdots\sqcup C_b\) be an owner-disjoint lower-rainbow
directed factor in \(J(k,r)\).  Choose one directed fixed-width old witness
\(I_Y\) for every previously covered proper upper target \(Y\).  Cut
component \(C_i\) at the directed protected wedge flank

\[
                     e_i=t_i s_i,\qquad
 c_i=t_i\cap s_i,\qquad
 \{\kappa_i\}=t_i\setminus s_i,
\tag{1.1}
\]

and let \(Q_i=(s_i,\ldots,t_i)\).  Define its complete assigned casualty
bundle

\[
             {\cal B}_i=\{Y:e_i\in\operatorname{span}(I_Y)\}.
\tag{1.2}
\]

By protected wedge geometry, every \(Y\in{\cal B}_i\) has assigned
occurrence

\[
                   (t_i,s_i,u_{i,2},\ldots,u_{i,q})
\tag{1.3}
\]

with rank increasing at every step.  Thus the single key \(\kappa_i\)
repairs the whole bundle, at every depth.

## 2. Exact conditional-key theorem

### Theorem 2.1 (active-bundle cyclic conveyor)

Order the components cyclically and suppose

\[
                    t_i\cap s_{i+1}=c_i
                    \qquad(1\le i\le b),
\tag{2.1}
\]

and impose key-forward only at active destinations:

\[
          {\cal B}_{i+1}\ne\varnothing
          \quad\Longrightarrow\quad
          \kappa_{i+1}\in t_i.
\tag{2.2}
\]

Then the cyclic braid formed by the seams \(t_i s_{i+1}\):

1. contains every middle owner exactly once;
2. has exactly the old lower \(q=1\) colour multiset; and
3. retains or literally replays the assigned witness of every previously
   covered upper target.

#### Proof

Equation (2.1) makes the outgoing seam of component \(i\) a Johnson edge of
colour \(c_i\).  The distinct deleted colours are therefore restored once
each.  The owner claim follows by joining the disjoint full component paths
cyclically.

If \(Y\notin{\cal B}_i\), its assigned occurrence remains internal to
\(Q_i\).  If \(Y\in{\cal B}_i\), the incoming endpoint \(t_{i-1}\) is a
Johnson neighbour of \(s_i\) and contains \(\kappa_i\) by (2.2).  Hence

\[
             t_{i-1}\cup s_i=s_i\cup\{\kappa_i\}
                                =t_i\cup s_i.
\tag{2.3}
\]

Replacing \(t_i\) by \(t_{i-1}\) in (1.3) preserves its entire union.  This
gives a literal seam-crossing witness for every member of
\({\cal B}_i\). \(\square\)

## 3. The dichotomy

### Theorem 3.1 (colour path and active key propagation)

Under (2.1), consecutive cut colours are distinct Johnson neighbours and

\[
                       s_{i+1}=c_i\cup c_{i+1}.
\tag{3.1}
\]

Moreover

\[
       {\cal B}_{i+1}\ne\varnothing
          \quad\Longrightarrow\quad
       \kappa_{i+1}=\kappa_i.
\tag{3.2}
\]

Consequently the keys are constant along every block of consecutive active
destinations.  If all \({\cal B}_i\) are nonempty, there is one common key
\(\kappa\), all \(c_i\) avoid \(\kappa\), and the cut colours form a cyclic
Johnson colour walk in \(J([k]\setminus\{\kappa\},r-1)\).

#### Proof

Both \(c_i=t_i\cap s_{i+1}\) and
\(c_{i+1}=t_{i+1}\cap s_{i+1}\) are rank-\((r-1)\) subsets of the rank-\(r\)
set \(s_{i+1}\).  They are distinct because the old lower palette is exact,
so they are adjacent and their union is \(s_{i+1}\), proving (3.1).

Write \(t_i=c_i\cup\{\kappa_i\}\).  Equation (2.1) implies
\(\kappa_i\notin s_{i+1}\).  At an active destination,
\(\kappa_{i+1}\in t_i\) by (2.2), while
\(\kappa_{i+1}\notin s_{i+1}\supset c_i\).  The only possible element is
\(\kappa_i\), proving (3.2).  The final assertion follows around the
cycle. \(\square\)

### Corollary 3.2 (safe-root/common-key dichotomy)

Exactly one of the following two branches applies.

1. **Inactive branch.**  Some \({\cal B}_i=\varnothing\).  Then deleting
   the incoming seam \(t_{i-1}s_i\) retains the chosen witness of every old
   upper target.  The resulting linear braid has lower ledger
   \(H=1,E=0\), with sole missing colour \(c_{i-1}\).
2. **Fully active branch.**  Every \({\cal B}_i\ne\varnothing\).  Then the
   common-key normal form of Theorem 3.1 is unavoidable.  A linear opening
   is zero-loss precisely when its removed seam has no target for which it
   is the sole remaining witness; alternate, unassigned witnesses may still
   make such a seam removable.

#### Proof

In the inactive branch, every target assigned to component \(i\) avoids
its cut and remains internal.  Targets assigned to other components are
internal or are replayed at their own, different incoming seams.  Thus the
seam into \(i\) is avoided by one selected witness for every target.  Its
deletion removes exactly its one restored lower colour.

The fully active assertion is Theorem 3.1 together with the exact cyclic
cut-kernel criterion for deleting one seam. \(\square\)

This dichotomy is the sharp scope correction to a blanket common-key claim
for the assigned old tower: inactive old-casualty bundles are legitimate
key-reset sites.  They need not be safe opening sites for the full required
universe if a source hole uses the incoming seam.  More generally there are
two distinct labels.  **Safe-opening activity** records every target whose
chosen sole witness uses that seam.  **Key activity** records only service
fibres whose literal provider requires the destination departure key.  The
two labels coincide for canonical outward-ray bundles but need not coincide
for noncanonical source-hole service.  When every destination is key-active,
common-key rigidity is an exact algebraic obstruction, not a heuristic.

## 4. Residence and the remaining gate

Strict residence can be included arcwise.  If each fragment is internally
\(d\)-clean, contains both a zero and a one in every coordinate trace, and
every selected seam has suffix-plus-prefix positive length either zero or at
least \(d+1\), the cyclic conveyor is \(d\)-resident.  Removing the safe
seam creates no new internal run.  For a non-flat deadline staircase one
must instead replay the exact position-aware transducer and terminal
threshold optimizer on the final linear order; pairwise collars or a
translation-invariant associative summary alone are not sufficient.

Thus the unresolved old-tower protected-opening subproblem is exactly:

* find an inactive safe-root conveyor; or
* in the fully active branch, find a common-key colour cycle and a seam with
  a complete alternate-witness guard bundle;

while simultaneously satisfying the residence/deadline state.  Source-hole
service and the common lower compiler remain additional ledgers and are not
asserted by this theorem.
